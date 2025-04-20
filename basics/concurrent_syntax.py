# -*- coding: utf-8 -*-

"""
并发
- 多线程
- 多进程
- 异步
- 线程池、进程池
"""

# 多线程
# import threading
#
# def print_numbers(num: int):
#     for i in range(num):
#         print(f"线程任务执行: {i}")
#
# thread = threading.Thread(target=print_numbers, args=(10,))
# thread.start()
# thread.join()


# 多进程
# import multiprocessing
#
# def print_numbers2(num: int):
#     for i in range(num):
#         print(f"进程任务执行: {i}")
#
# if __name__== '__main__':
#     process = multiprocessing.Process(target=print_numbers2, args=(15,))
#     process.start()
#     process.join()


# 异步
# import asyncio
#
# async def print_numbers():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(1)
#
# asyncio.run(print_numbers())


# 线程池、进程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def task(n):
    time.sleep(n)
    return f"Task {n} completed"

# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(task,n) for n in range(1, 4)]
#     for future in futures:
#         print(future.result())

# if __name__== '__main__':
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         futures = [executor.submit(task, n) for n in range(1, 4)]
#         for future in futures:
#             print(future.result())