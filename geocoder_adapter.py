# -*- coding: utf-8 -*-
"""
@Date: 2021/8/26 15:47
@Author:Wang Shihan
"""
from qgis.PyQt.QtCore import QThread, pyqtSignal
from .core.worker import Worker
from .core.gcs import Geocoder


class GeocoderAdapter(QThread):
    row_signal = pyqtSignal(list)
    finish_signal = pyqtSignal(list)

    def __init__(self, reader, col_select, geocoder: Geocoder, concurrent=10):
        super(GeocoderAdapter, self).__init__()
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
            self.row_signal.emit([address, attr, ['NA', 'NA'], f'错误：{str(e)}'])
