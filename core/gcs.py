# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
from requests import get
from requests import Session
import json

from .utils import bd09_to_wgs84, bd09_to_gcj02, CrsTypeEnum


class Location:
    def __init__(
        self,
        address: str,
        longitude=None,
        latitude=None,
        status: bool = True,
        msg: str = '',
    ) -> None:
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.status = status
        self.msg = msg

    def __repr__(self) -> str:
        return f'Location(address={self.address}, longitude={self.longitude}, latitude={self.latitude}, status={self.status}, msg={self.msg})'


class Geocoder:
    flag = '未知'

    def __init__(self) -> None:
        # 服务接口地址
        self.api: str = ''
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "Referer": "https://wsh233.cn",
        }

    def search(self, address) -> Location:
        try:
            return self.execute(address)
        except Exception as e:
            return Location(address, status=False, msg=str(e))

    def execute(self, address: str) -> Location:
        return Location(address, status=False, msg='未实现方法')


class Baidu(Geocoder):
    flag = "百度地图"

    def __init__(self, key: str, transform=CrsTypeEnum.bd):
        """:arg
        ak: appKey
        transform: 指定坐标转换方式
        """
        super().__init__()
        self.session = Session()
        self.api = 'http://api.map.baidu.com/geocoding/v3/'
        self.__params = {'address': '', 'output': 'json', 'ak': key}
        self.trans = transform
        self.made = 0
        self.failed = 0

    @property
    def transform(self):
        return self.trans

    @transform.setter
    def transform(self, value):
        self.trans = value

    def execute(self, address) -> Location:
        """
        :arg
        address 待获取坐标地点
        attr 其他字段信息
        """
        self.__params['address'] = address
        resp = self.session.get(
            url=self.api,
            params=self.__params,
            headers=self.headers,
            timeout=10,
        )
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            if 'result' in json.loads(resp.text):
                res_json = json.loads(resp.text)['result']
                loc_raw = res_json['location']
                if self.trans == CrsTypeEnum.bd2wgs:
                    loc = bd09_to_wgs84(loc_raw['lng'], loc_raw['lat'])
                elif self.trans == CrsTypeEnum.bd2gcj:
                    loc = bd09_to_gcj02(loc_raw['lng'], loc_raw['lat'])
                else:
                    loc = [loc_raw['lng'], loc_raw['lat']]
                self.made += 1
                location = [loc[0], loc[1]]
                return Location(address, longitude=location[0], latitude=location[1])

            else:
                raise Exception(f'错误：{resp.text}')
        else:
            raise Exception(f'错误：{resp.text}')

    def get_many(self, **kwargs):
        """
        批量获取坐标
        """
        pass


class Nominatim(Geocoder):
    flag = 'OSM'

    def __init__(self, proxy=None) -> None:
        super().__init__()
        self.api = 'https://nominatim.openstreetmap.org/search'
        if proxy:
            self.api = proxy

    def execute(self, address: str) -> Location:
        params = {
            'q': address,  # 要地理编码的地址
            'format': 'json',  # 返回格式
            'limit': 1,  # 限制返回结果数量
            'addressdetails': 1,  # 返回详细地址信息
        }
        response = get(self.api, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                return Location(
                    address, longitude=data[0]['lon'], latitude=data[0]['lat']
                )
            else:
                raise Exception(f'错误：{response.text}')
        else:
            raise Exception(f'错误：{response.text}')


class Here(Geocoder):
    flag = 'Here'

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://geocode.search.hereapi.com/v1/geocode'

    def execute(self, address: str) -> Location:
        params = {
            'q': address,
            'apikey': self.key,
        }
        resp = get(self.api, headers=self.headers, params=params)
        if resp.status_code == 200:
            data = resp.json()
            if data and data['items']:
                return Location(
                    address,
                    longitude=data['items'][0]['position']['lng'],
                    latitude=data['items'][0]['position']['lat'],
                )
            else:
                raise Exception(f'错误：{resp.text}')
        else:
            raise Exception(f'错误：{resp.text}')


class Mapbox(Geocoder):
    flag = 'Mapbox'

    def __init__(
        self,
        key: str,
    ) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://api.mapbox.com/search/geocode/v6/forward'

    def execute(
        self,
        address: str,
    ) -> Location:
        params = {
            'q': address,
            'access_token': self.key,
            'proximity': 'ip',
        }
        response = get(self.api, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['features'] and data['features'][0]:
                return Location(
                    address,
                    longitude=data['features'][0]['geometry']['coordinates'][0],
                    latitude=data['features'][0]['geometry']['coordinates'][1],
                )
            else:
                raise Exception(f'错误：{response.text}')
        else:
            raise Exception(f'错误：{response.text}')


class Gaode(Geocoder):
    flag = '高德地图'

    def __init__(self, key: str) -> None:
        super().__init__()
        self.api = 'https://restapi.amap.com/v3/geocode/geo'
        self.key: str = key

    def execute(self, address) -> Location:
        params = {
            "key": self.key,
            "address": address,
            "output": "json",
        }
        resp = get(self.api, headers=self.headers, params=params)
        if resp.status_code == 200:
            data = resp.json()
            if data['status'] == '1':
                return Location(
                    address,
                    longitude=data['geocodes'][0]['location'].split(',')[0],
                    latitude=data['geocodes'][0]['location'].split(',')[1],
                )
            else:
                raise Exception(data['info'])
        else:
            raise Exception(f'错误：{resp.text}')


# 注册地理编码器
GEOCODER_MAP = {
    "百度地图": Baidu,
    "高德地图": Gaode,
    "Mapbox": Mapbox,
    "Here": Here,
    "OSM": Nominatim,
}

if __name__ == '__main__':
    gaode = Gaode("")
    print(gaode.search("北京市海淀区上地十街10号"))
