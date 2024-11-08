# -*- coding: utf-8 -*-
"""
    @File: worker.py
    @Author:Wang Shihan
    @Date:2024/7/26
    @Description:
"""
import concurrent.futures
import time


class Worker:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        )

    def submit_task(self, func, *args, **kwargs):
        return self.executor.submit(func, *args, **kwargs)

    def shutdown(self):
        self.executor.shutdown(wait=True)

    def wait_for_completion(self, futures):
        results = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
        return results


if __name__ == "__main__":

    def task(n):
        time.sleep(2)
        return n * n, n  # 返回计算结果

    start = time.time()

    worker = Worker(10)
    futures = [worker.submit_task(task, i) for i in range(50)]
    result = worker.wait_for_completion(futures)
    print(result)
    # for i in range(100):
    #     task(i)

    end = time.time()
    print(f'time comsuming{end - start}')
