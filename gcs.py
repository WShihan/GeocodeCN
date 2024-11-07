# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
from requests import get
from requests import Session
import json
from qgis.PyQt.QtCore import QThread, pyqtSignal
from .utils import bd09_to_wgs84, bd09_to_gcj02, CrsTypeEnum
from .worker import Worker


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

    def __init__(self, proxy=None) -> None:
        super().__init__()
        self.api = 'https://nominatim.openstreetmap.org/search'
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

    def __init__(self, key: str) -> None:
        super().__init__()
        self.key = key
        self.api = 'https://geocode.search.hereapi.com/v1/geocode'

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


class CrsGen(QThread):
    row_signal = pyqtSignal(list)
    finish_signal = pyqtSignal(list)

    def __init__(self, reader, col_select, geocoder: Geocoder, concurrent=10):
        super(CrsGen, self).__init__()
        self.reader = reader
        self.col_select = col_select
        self.geocoder = geocoder
        self.concurrent = concurrent

    def run(self):
        worker = Worker(self.concurrent)
        tasks = []
        for r in self.reader:
            address = r[self.col_select]
            attr = [r[i] for i in r.keys()]
            tasks.append(worker.submit_task(self.execute, address, attr))
        worker.wait_for_completion(tasks)
        self.finish_signal.emit([])

    def execute(self, address: str, attr: list):
        try:
            res = self.geocoder.search(address)
            if len(res) > 0:
                if res[0] == 1:
                    self.row_signal.emit([address, attr, res[1], ''])
                else:
                    raise Exception("无地址数据！")
            else:
                raise Exception("无地址数据！")
        except Exception as e:
            self.row_signal.emit([address, [], [], f'错误：{str(e)}'])


if __name__ == '__main__':
    b = Baidu(key='')
    res = b.search("北京市")
    print(res)
