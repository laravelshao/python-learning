






class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('/Users/sylvia/Downloads/hello.txt') as f:
    f.write("Hello, World!")




# requests 库
# import requests
#
# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.json())

# numpy 科学计算库

import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 数组运算
print(arr * 2)


# # web页面爬虫
# import requests
# from bs4 import BeautifulSoup
#
# # 发送HTTP请求
# url = 'https://example.com'
# response = requests.get(url)
#
# # 解析HTML内容
# try:
#     soup = BeautifulSoup(response.text, 'html.parser')
# except AttributeError:
#     import collections.abc
#     collections.Callable = collections.abc.Callable
#     soup = BeautifulSoup(response.text, 'html.parser')


# # 提取标题
# title = soup.title.string
# print(f"网页标题: {title}")
#
# # 提取所有链接
# for link in soup.find_all('a'):
#     print(link.get('href'))




from abc import ABC, abstractmethod

class Shape(ABC):
    # 抽象方法
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())


# 元类(Metaclasses)
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# # 异步编程
# import asyncio
#
# async def fetch_data():
#     print("Start fetching")
#     await asyncio.sleep(2)
#     print("Done fetching")
#     return {'data': 1}
#
# async def main():
#     task = asyncio.create_task(fetch_data())
#     print("Doing other work")
#     await asyncio.sleep(1)
#     print("Other work done")
#     result = await task
#     print(result)
#
# # 运行异步函数
# asyncio.run(main())





# # 单元测试
# import unittest
#
# def add(x, y):
#     return x + y
#
# class TestMathOperations(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#
# # 运行测试
# if __name__ == '__main__':
#     unittest.main()


# # web API
# from flask import Flask, jsonify
# app = Flask(__name__)
#
# @app.route('/api/hello', methods=['GET'])
# def hello():
#     return jsonify(messages="Hello World!")
#
# if __name__== '__main__':
#     app.run(debug=True)



# 生成器 yield
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))

for value in simple_generator():
    print(value)


