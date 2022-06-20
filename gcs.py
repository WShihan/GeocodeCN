# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
import requests
import json
from .utils import  bd09_to_wgs84,bd09_to_gcj02, CrsTypeEnum
from qgis.PyQt.QtCore import QThread, pyqtSignal


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


class Baidu():
    def __init__(self, ak="9IRhgisjtSA8LBnX4RwSdyHamH2jxjxm", transform=CrsTypeEnum.bd):
        """:arg
        ak: appKey
        transform: 指定坐标转换方式
        """
        self.session = requests.session()
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
        self.url = 'http://api.map.baidu.com/geocoding/v3/'
        self.__params = {
            'address': '',
            'output': 'json',
            'ak': ak
        }
        self.trans = transform
        self.made = 0
        self.failed = 0

    @property
    def transform(self):
        return self.trans

    @transform.setter
    def transform(self, value):
        self.trans = value

    def get_one(self, address) ->POI:
        """
        获取单一坐标
        :arg
        address 待获取坐标地点
        attr 其他字段信息
        """
        self.__params['address'] = address
        try:
            res = self.session.get(url=self.url,
                                   params=self.__params,
                                   headers={'user-agent': self.ua},
                                   timeout=10
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
                    return {'status':1, "loc": location}

                else:
                    self.failed += 1
                    location = ['NA', 'NA']
                    return {'status': 0, "loc": location}
        except Exception as e:
            print(e)

    def get_many(self,**kwargs):
        """
        批量获取坐标
        """
        pass


class Crs_gen(QThread):
    signal = pyqtSignal(list)
    def __init__(self, reader,col_select, baidu:Baidu):
        super(Crs_gen, self).__init__()
        self.reader = reader
        self.col_select = col_select
        self.baidu = baidu

    def run(self):
        for r in self.reader:
            address = r[self.col_select]
            attr = [r[i] for i in r.keys()]
            res = self.baidu.get_one(address)
            if res['status'] == 1:
                self.signal.emit([address, attr, res['loc']])
            else:
                self.signal.emit([])


if __name__ == '__main__':
    b = Baidu()
    res = b.get_one("北京市")
    print(res)

