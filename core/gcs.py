# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
from requests import get
from requests import Session
import json
from .utils import bd09_to_wgs84, bd09_to_gcj02, CrsTypeEnum


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

    def search(self, address) -> tuple:
        return (0, ['NA', 'NA'])


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
        self.flag = "百度地图"

    @property
    def transform(self):
        return self.trans

    @transform.setter
    def transform(self, value):
        self.trans = value

    def search(self, address) -> tuple:
        """
        :arg
        address 待获取坐标地点
        attr 其他字段信息
        """
        self.__params['address'] = address
        res = self.session.get(
            url=self.api,
            params=self.__params,
            headers=self.headers,
            timeout=10,
        )
        if res.status_code == 200:
            res.encoding = res.apparent_encoding
            if 'result' in json.loads(res.text):
                res_json = json.loads(res.text)['result']
                loc_raw = res_json['location']
                if self.trans == CrsTypeEnum.bd2wgs:
                    loc = bd09_to_wgs84(loc_raw['lng'], loc_raw['lat'])
                elif self.trans == CrsTypeEnum.bd2gcj:
                    loc = bd09_to_gcj02(loc_raw['lng'], loc_raw['lat'])
                else:
                    loc = [loc_raw['lng'], loc_raw['lat']]
                self.made += 1
                location = [loc[0], loc[1]]
                return (1, location)

            else:
                self.failed += 1
                location = ['NA', 'NA']
                return (0, location)
        else:
            return tuple()

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
        self.flag = 'OSM'
        if proxy:
            self.api = proxy

    def search(self, address: str) -> tuple:
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
                return (1, [data[0]['lon'], data[0]['lat']])
            else:
                return (0, ['NA', 'NA'])
        else:
            return (0, ['NA', 'NA'])


class Here(Geocoder):
    flag = 'Here'

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://geocode.search.hereapi.com/v1/geocode'
        self.flag = 'Here'

    def search(self, address: str) -> tuple:
        params = {
            'q': address,
            'apikey': self.key,
        }
        response = get(self.api, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data and data['items']:
                return (
                    1,
                    [
                        data['items'][0]['position']['lng'],
                        data['items'][0]['position']['lat'],
                    ],
                )
            else:
                return (0, ['NA', 'NA'])
        else:
            return (0, ['NA', 'NA'])


class Mapbox(Geocoder):
    flag = 'Mapbox'

    def __init__(
        self,
        key: str,
    ) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://api.mapbox.com/search/geocode/v6/forward'
        self.flag = 'Mapbox'

    def search(
        self,
        address: str,
    ) -> tuple:
        params = {
            'q': address,
            'access_token': self.key,
            'proximity': 'ip',
        }
        response = get(self.api, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['features'] and data['features'][0]:
                return (
                    1,
                    [
                        data['features'][0]['geometry']['coordinates'][0],
                        data['features'][0]['geometry']['coordinates'][1],
                    ],
                )
            else:
                return (0, ['NA', 'NA'])
        else:
            return (0, ['NA', 'NA'])


class Gaode(Geocoder):
    flag = '高德地图'

    def __init__(self, key: str) -> None:
        super().__init__()
        self.api = 'https://restapi.amap.com/v3/geocode/geo'
        self.flag = '高德地图'
        self.key: str = key

    def search(self, address) -> tuple:
        params = {
            "key": self.key,
            "address": address,
            "output": "json",
        }
        resp = get(self.api, headers=self.headers, params=params)
        if resp.status_code == 200:
            data = resp.json()
            if data['status'] == 1:
                return (
                    1,
                    [
                        data['geocodes'][0]['location'].split(',')[0],
                        data['geocodes'][0]['location'].split(',')[1],
                    ],
                )
            else:
                return (0, ['NA', 'NA'])
        else:
            return (0, ['NA', 'NA'])


# 地理编码器集合
GEOCODER_MAP = {
    "百度地图": Baidu,
    "高德地图": Gaode,
    "Mapbox": Mapbox,
    "Here": Here,
    "OSM": Nominatim,
}

if __name__ == '__main__':
    gaode = Gaode("您的高德地图key")
    print(gaode.search("北京市海淀区上地十街10号"))
