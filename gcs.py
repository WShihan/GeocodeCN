# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
from requests import get
from requests import Session
import json
from .utils import bd09_to_wgs84, bd09_to_gcj02, CrsTypeEnum
from qgis.PyQt.QtCore import QThread, pyqtSignal


class Geocoder:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "Referer": "https://wsh233.cn",
        }

    def search(self, address) -> tuple:
        return (0, ['NA', 'NA'])


class POI(object):
    def __init__(self, name, lon, lat, confidence, attr):
        """:arg
        name: 地址名称
        lon: 经度
        lat: 纬度
        confidence: 地址理解程度
        attr: 其他字段信息
        """
        self.name = name
        self.lon = lon
        self.lat = lat
        self.attr = attr
        self.confidence = confidence


class Baidu(Geocoder):
    def __init__(self, key: str, transform=CrsTypeEnum.bd):
        """:arg
        ak: appKey
        transform: 指定坐标转换方式
        """
        super().__init__()
        self.session = Session()
        self.ua = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/88.0.4324.146 Safari/537.36 '
        )
        self.url = 'http://api.map.baidu.com/geocoding/v3/'
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

    def search(self, address) -> tuple:
        """
        :arg
        address 待获取坐标地点
        attr 其他字段信息
        """
        self.__params['address'] = address
        res = self.session.get(
            url=self.url,
            params=self.__params,
            headers={'user-agent': self.ua},
            timeout=10,
        )
        if res.status_code == 200:
            res.encoding = res.apparent_encoding
            if 'result' in json.loads(res.text):
                res_json = json.loads(res.text)['result']
                loc_raw = res_json['location']
                comprehension = res_json['comprehension']
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

    def __init__(self, proxy=None) -> None:
        super().__init__()
        self.api = 'https://nominatim.openstreetmap.org/search'
        if proxy:
            self.api = proxy

    def search(self, address: str) -> tuple:
        # 设置请求参数
        params = {
            'q': address,  # 要地理编码的地址
            'format': 'json',  # 返回格式
            'limit': 1,  # 限制返回结果数量
            'addressdetails': 1,  # 返回详细地址信息
        }
        # 发送GET请求
        response = get(self.api, headers=self.headers, params=params)
        # 检查响应状态
        if response.status_code == 200:
            # 解析JSON响应
            data = response.json()
            print(data)
            if data:
                # 返回第一个结果的坐标
                return (1, [data[0]['lon'], data[0]['lat']])
                # return {
                #     'latitude': data[0]['lat'],
                #     'longitude': data[0]['lon'],
                #     'address': data[0]['display_name'],
                # }
            else:
                print(response.text)
                return (0, ['NA', 'NA'])
        else:
            print(response.text)
            return (0, ['NA', 'NA'])


class Here(Geocoder):

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://geocode.search.hereapi.com/v1/geocode'

    def search(self, address: str) -> tuple:
        params = {
            'q': address,  # 要地理编码的地址
            'apikey': self.key,
        }
        # 发送GET请求
        response = get(self.api, headers=self.headers, params=params)
        # 检查响应状态
        if response.status_code == 200:
            # 解析JSON响应
            data = response.json()
            print(data)
            if data and data['items']:
                # 返回第一个结果的坐标
                return (
                    1,
                    [
                        data['items'][0]['position']['lng'],
                        data['items'][0]['position']['lat'],
                    ],
                )
                # return {
                #     'latitude': data['items'][0]['position']['lat'],
                #     'longitude': data['items'][0]['position']['lng'],
                #     'address': data['items'][0]['address']['label'],
                # }
            else:
                print(response.text)
                return (0, ['NA', 'NA'])
        else:
            print(response.text)
            return (0, ['NA', 'NA'])


class Mapbox(Geocoder):

    def __init__(
        self,
        key: str,
    ) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://api.mapbox.com/search/geocode/v6/forward'

    def search(
        self,
        address: str,
    ) -> tuple:
        params = {
            'q': address,  # 要地理编码的地址
            'access_token': self.key,
            'proximity': 'ip',
        }
        # 发送GET请求
        response = get(self.api, headers=self.headers, params=params)
        # 检查响应状态
        if response.status_code == 200:
            # 解析JSON响应
            data = response.json()
            print(data)
            if data['features'] and data['features'][0]:
                # 返回第一个结果的坐标
                return (
                    1,
                    [
                        data['features'][0]['geometry']['coordinates'][0],
                        data['features'][0]['geometry']['coordinates'][1],
                    ],
                )
                # return {
                #     'longitude': data['features'][0]['geometry']['coordinates'][0],
                #     'latitude': data['features'][0]['geometry']['coordinates'][1],
                #     'address': data['features'][0]['properties']['full_address'],
                # }
            else:
                print(response.text)
                return (0, ['NA', 'NA'])
        else:
            print(response.text)
            return (0, ['NA', 'NA'])


class CrsGen(QThread):
    signal = pyqtSignal(list)

    def __init__(self, reader, col_select, geocoder: Geocoder):
        super(CrsGen, self).__init__()
        self.reader = reader
        self.col_select = col_select
        self.geocoder = geocoder

    def run(self):
        for r in self.reader:
            address = r[self.col_select]
            attr = [r[i] for i in r.keys()]
            res = self.geocoder.search(address)
            if len(res) > 0:
                if res[0] == 1:
                    self.signal.emit([address, attr, res[1]])
                else:
                    self.signal.emit([])
            else:
                self.signal.emit([])


if __name__ == '__main__':
    b = Baidu(ak='')
    res = b.search("北京市")
    print(res)
