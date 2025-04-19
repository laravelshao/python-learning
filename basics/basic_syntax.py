# -*- coding: utf-8 -*-

"""
基础语法
- 变量、数据类型、验证数据类型、数据类型转换
- 算术运算符：加(+)、减(-)、乘(*)、除(/)、整除(//)、取余(%)、幂(**)，特别：整除、幂
- 数据类型占位格式化：将内容转换为字符串放入占位位置(%s)、将内容转换为整数放入占位位置(%d)、将内容转换为浮点数放入占位位置(%f)
- 数字占位精度控制(m.n，如果m比数字小则不生效)
- (推荐)字符串格式化(f)
- 数据输入(输入的数字类型也会以字符串承载)
- 条件语句(if-elif-else)
- 组合多条件：and(与)、or(或)、not(非)
- 循环语句(while/for)、continue、break
- 函数、局部变量/全局变量、函数多返回值、参数形式(位置参数、关键字参数、缺省参数、不定长参数)、函数作为参数传递、匿名函数(lambda)
- 局部变量/全局变量(global申明)
- 列表(list)
- 元组(初始化后不可修改，但是在元祖内的列表是可以修改)
- 字符串(初始化后不可修改)
- 序列(列表/元组/字符串)、序列切片操作(序列[起始下标:结束下标:步长])
- 集合(无序唯一)
- 字典
- 文件读写
- 异常
- 模块(模块是一个 Python 文件，里面定义有函数、类、变量等)
- __name__ == '__main__' 作用：确保某些代码块仅在脚本作为主程序运行时执行，而在被导入时不执行
- 自定义包
- JSON格式转换
"""

print('hello world')
print("hello", end = '') # 不换行输出
print("world")

# 变量和数据类型
x = 10
y = 3.14
name = "alice"
is_flag = True
print(x, y, name, is_flag)

# 验证数据类型：type()
print(type(x))
print(type(y))
print(type(name))

# 数据类型转换：int()/float()/str()
num_str = str(11)
print(type(num_str), num_str)

num = int("22")
print(type(num), num)


# 算术运算符：加(+)、减(-)、乘(*)、除(/)、整除(//)、取余(%)、幂(**)，特别：整除、幂
print("加法：1 + 1 = ", 1 + 1)
print("减法：2 - 1 = ", 4 - 3)
print("乘法：3 * 2 = ", 3 * 2)
print("除法：4 / 2 = ", 4 / 2)
print("整除：9 // 2 = ", 9 // 2)
print("取余：7 % 2 = ", 7 % 2)
print("指数：2 ** 3 = ", 2 ** 3)


# 数据类型占位格式化：将内容转换为字符串放入占位位置(%s)、将内容转换为整数放入占位位置(%d)、将内容转换为浮点数放入占位位置(%f)
company_name = "特斯拉"
setup_year = 2003
stock_price = 252.95
print("%s, 成立于：%d，今天的股价是：%f" % (company_name, setup_year, stock_price))

# 数字占位精度控制(m.n，如果m比数字小则不生效)
n1 = 12
n2 = 12.345
print("数字12宽度限制5，结果是：%5d" % n1)
print("数字12宽度限制1，结果是：%1d" % n1) # m比数字小则不生效
print("数字12.345宽度限制7，小数精度2，结果是：%7.2f" % n2)
print("数字12.345宽度不限制，小数精度2，结果是：%.2f" % n2)


# (推荐)字符串格式化(f)
print(f"{company_name}, 成立于：{setup_year}，今天的股价是：{stock_price}")


# 数据输入(输入的数字类型也会以字符串承载)
# username = input("你的用户名是？")
# print(username, type(username))


# 条件语句(if-elif-else)
age = 18
if age < 18:
    print("未成年")
elif age == 18:
    print("刚成年")
else:
    print("成年")

# 组合多条件：and(与)、or(或)、not(非)
score = 85 # 积分
is_member = True # 是否为会员
# 判断 (score >= 80 且 is_member) 或 score >= 90 有资格享受折扣
if (score >= 80 and is_member) or score >= 90:
    print("有资格享受折扣")
else:
    print("无折扣")


# 循环语句(while/for)、continue、break
# continue：结束所在循环的当次执行，直接进入下一次
# break：直接结束所在的循环

# while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# while循环打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # \t：对齐
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    i += 1
    # 换行
    print()

# for循环
for i in range(5):
    print(i)

# for循环打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end = '')
    print()


# 函数、局部变量/全局变量、函数多返回值、参数形式(位置参数、关键字参数、缺省参数、不定长参数)、函数作为参数传递、匿名函数(lambda)
# 没有返回值的函数，实际返回值为None，类型为 NoneType
def greet(name="World"):
    return f"Hello, {name}"
print(greet("Alice"))
print(greet())

# 局部变量/全局变量(global申明)
xx = 200
def m1():
    xx = 300 # 局部变量，作用域只在该方法内
    print(xx)
def m2():
    global xx # 申明为全局变量，如果未申明，即便内部的变量都是xx，内部赋值操作不会影响外部变量值
    xx = 500
    print(xx)
m1()        # 打印300
print(xx)   # 打印200
m2()        # 打印500
print(xx)   # 打印500，m2方法中变量申明为global，赋值对外部变量生效

# 函数多返回值
def multi_return():
    return 1, "hello", True
x, y, z = multi_return()
print(x, y, z)

# 参数形式(位置参数、关键字参数、缺省参数、不定长参数)
def user(name, age, gender):
    print(f"姓名：{name}，年龄为：{age}，性别为：{gender}")
# 位置形参(默认形式)
user("张三", 20, "男")
# 关键字参数(可以不按照参数定义顺序传参，和位置参数混用时位置参数需要放在前面)
user(name = "张三",gender = "男", age = 20)

# 缺省参数：gender = 男
def user2(name, age, gender = '男'):
    print(f"姓名：{name}，年龄为：{age}，性别为：{gender}")
user2("李四", 19)
user2("王五", 26, "女")

# 位置不定长参数(所有参数都会存储在元组中)
def user3(*args):
    print(f"参数内容为：{args}，类型为：{type(args)}")
user3("张三")
user3("李四", 20)

# 关键字(键值对)不定长参数(所有参数都会存储在字典中)
def user4(**kvargs):
    print(f"参数内容为：{kvargs}，类型为：{type(kvargs)}")
user4(name="赵六", age = 18)
user4(name="田七", age = 17, gender = "女")

# 函数作为参数传递(传入的是计算逻辑，而非传入数据)
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数类型为：{type(compute)}")
    print(f"计算结果为：{result}")
# 定义作为参数传递的函数
def compute(x, y):
    return x + y
# 传入函数调用
test_func(compute)
# 匿名函数(lambda)
# 格式：lambda 传入参数 : 函数体
test_func(lambda x, y: x + y)


# 列表
fruits = ["apple", "banana", "cherry"]
# 列表索引遍历：从前往后方向索引从0开始递增，从后往前方向索引从-1开始递减
print(fruits[0])    # 获取正向下标第一个元素
print(fruits[-1])   # 获取逆向下标第一个元素(-1开始)
print(type(fruits))

# 查找元素下标
print(fruits.index("banana"))
# 修改元素
fruits[2] = "lemon"
print(fruits)
# 插入元素
fruits.insert(2, "watermelon")
print(fruits)
# 追加元素(只会在最后)
fruits.append("orange")
print(fruits)
# 追加一批元素
fruits.extend(["mango", "pear"])
print(fruits)
# 删除下标为2的元素
# del fruits[2]
# 删除下标为2的元素
# fruits.pop(2)
# 移除指定元素
fruits.remove("pear")
# 清空列表
# fruits.clear()
# 统计列表长度
print(len(fruits))

# 遍历列表(for/while)
# for f in fruits:
#     print(f)
#
# list_cnt = 0
# while list_cnt < len(fruits):
#     print(fruits[list_cnt])
#     list_cnt += 1


# 元组(初始化后不可修改，但是在元祖中嵌套的列表是可以修改)
t1 = (1, "tuple", True)
t2 = ()
t3 = tuple()
t4 = ("hello", )    # 如果是单个元素，一定要加逗号分隔，不然会类型是字符串，而不是元组
t5 = ("hello")      # 单个元素如果不加逗号分隔，类型是字符串
print(f"t1的类型是：{type(t1)}, t1的值是：{t1}")
print(f"t1的类型是：{type(t2)}, t1的值是：{t2}")
print(f"t1的类型是：{type(t3)}, t1的值是：{t3}")
print(f"t1的类型是：{type(t4)}, t1的值是：{t4}")
print(f"t1的类型是：{type(t5)}, t1的值是：{t5}")

t6 = ("aaa", "bbb", "ccc", "bbb")
# 下标获取元素
print(f"元祖t6下标位置1处值是：{t6[1]}")
# 查找元素下标
print(f"元祖t6中元素ccc下标位置是：{t6.index("ccc")}")
# 统计某个元素个数
print(f"元祖t6中元素bbb个数是：{t6.count("bbb")}")
# 统计元组元素个数
print(f"元祖t6中元素个数是：{len(t6)}")

# 遍历元组(for/while)
# for e in t6:
#    print(f"元组元素：{e}")
#
# t_cnt = 0
# while t_cnt < len(t6):
#     print(f"元组元素：{t6[t_cnt]}")
#     t_cnt += 1

# 元组初始化后元素不可修改，但是在元祖中嵌套的列表元素可以修改
t7 = ("1", "22", ["aaa", "bbb"])
print(f"元组t7的元素是：{t7}")
t7[2][0] = "AAA"
t7[2][1] = "BBB"
print(f"元组t7的元素是：{t7}")


# 字符串(初始化后不可修改)
s1 = "java python go c"
# 字符串索引遍历：从前往后方向索引从0开始递增，从后往前方向索引从-1开始递减
print(s1[0])    # 结果 j
print(s1[-1])   # 结果 c
# 查找元素下标
print(f"字符串s1中go的下标是：{s1.index("go")}")
s2 = "java python go c"
# 替换元素
s3 = s2.replace("go", "c++")
print(f"字符串s2：{s2} 元素替换后是：{s3}")
# 字符串分割
cs = s2.split(" ")
print(f"字符串s2根据空格分割后是：{cs}")
s4 = "   java python go c     "
# 去除前后空格
print(f"字符串s4：{s4}, 去除前后空格后是：{s4.strip()}")
s5 = "123java python go c321"
# 去除前后指定字符串(会拆分字符进行去除，所以与顺序无关)
print(f"字符串s5：{s5}, 去除前后123后是：{s5.strip("123")}")
s6 = "java python go c go"
# 统计字符串出现次数
print(f"字符串s6中go出现次数是：{s6.count("go")}")
# 统计字符串长度
print(f"字符串s6长度是：{len(s6)}")

# 遍历字符串(for/while)
# for e in s6:
#     print(f"字符串s6元素：{e}")
#
# s6_cnt = 0
# while s6_cnt < len(s6):
#     print(f"字符串s6元素：{s6[s6_cnt]}")
#     s6_cnt += 1


# 序列(列表/元组/字符串)、序列切片操作(序列[起始下标:结束下标:步长])
# 起始下标留空表示从头开始，结束下标留空表示截取到结尾，步长为1可以省略
# 对list进行切片，从1开始，4结束，步长1
cut_list = [1, 2, 3, 4, 5, 6]
print(f"对list：{cut_list} 进行切片，从1开始，4结束，步长1，结果是：{cut_list[1:4]}")
# 对tuple进行切片，从头开始，到最后结束，步长2
cut_tuple = (1, 2, 3, 4, 5, 6)
print(f"对tuple：{cut_tuple} 进行切片，从头开始，到最后结束，步长2，结果是：{cut_tuple[::2]}")
# 对字符串进行切片，从头开始，到最后结束，步长-1(后往前遍历)
cut_str = "123456"
print(f"对字符串：{cut_str} 进行切片，从头开始，到最后结束，步长-1(后往前遍历)，结果是：{cut_str[::-1]}")


# 集合(无序唯一)
# 定义集合
my_set = {"dji", "mavic", "osmo", "inspire", "mavic", "osmo"}
# 定义空集合
empty_set = set()
print(f"my_set内容为：{my_set}, 类型为：{type(my_set)}")
print(f"empty_set内容为：{empty_set}, 类型为：{type(empty_set)}")

# 添加元素
my_set.add("avata")
my_set.add("dji") # 重复未添加成功
print(f"my_set添加元素后为：{my_set}")

# 移除元素
my_set.remove("avata")
print(f"my_set移除元素avata后为：{my_set}")
# 随机取出元素
element = my_set.pop()
print(f"my_set随机取出一个元素为：{element}")

my_set2 = {"dji", "mavic", "osmo", "inspire"}
my_set2.clear()
print(f"set2清空后为：{my_set2}")

set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 取2个集合差集
set3 = set1.difference(set2)
print(f"差集结果为：{set3}")  # 结果：{2, 3}
print(f"set1为：{set1}")  # 不变
print(f"set2为：{set2}")  # 不变

set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 消除2个集合差集(集合1被修改，集合2不变)
set1.difference_update(set2)
print(f"set1为：{set1}")  # 结果：{2, 3}
print(f"set2为：{set2}")  # 结果：{1, 5, 6}

set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 2个集合合并
set3 = set1.union(set2)
print(f"集合合并结果为：{set3}")  # 结果：{1, 2, 3, 5, 6}
print(f"set1为：{set1}")  # 不变
print(f"set2为：{set2}")  # 不变

set1 = {1, 2, 3, 4, 5, 6}
print(f"set1：{set1} 集合长度为：{len(set1)}")

# 遍历集合(for)，不能下标访问不能用while
# for e in set1:
#     print(f"set1集合元素：{e}")


# 字典
# 定义字典
my_dict1 = {"张三": 80, "李四": 90, "王五": 70}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"my_dict1内容为：{my_dict1}, 类型为：{type(my_dict1)}")
print(f"my_dict2内容为：{my_dict2}, 类型为：{type(my_dict2)}")
print(f"my_dict3内容为：{my_dict3}, 类型为：{type(my_dict3)}")

# 获取值
print(f"从my_dict1中获取李四的成绩为: {my_dict1["李四"]}")
# 新增元素
my_dict1["赵六"] = 85
print(f"my_dict1中新增元素后为: {my_dict1}")
# 删除元素
my_dict1.pop("赵六")
print(f"my_dict1中删除赵六后为: {my_dict1}")
# 清空字典
my_dict1.clear()
print(f"my_dict1清空后为: {my_dict1}")
# 获取全部keys
my_dict4 = {"张三": 80, "李四": 90, "王五": 70}
keys = my_dict4.keys()
print(f"获取my_dict4的全部key为：{keys}，类型为：{type(keys)}")
# 统计字典元素数量
print(f"my_dict4元素数量为：{len(my_dict4)}")

# 遍历字典
for key in my_dict4:
    print(f"key：{key}，对应的值为：{my_dict4[key]}")



# 文件读写
# 打开文件
# f = open("../file_read_test.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取指定字符，未传则读取全部内容
# print(f"读取10个字符是：{f.read(10)}")   # 读取10个字符
# print(f"读取全部内容是：{f.read()}")     # 读取全部内容
# 按行读取全部内容，返回行内容列表
# lines = f.readlines()
# print(f"读取到lines的类型是：{type(lines)}")
# print(f"读取到lines的内容是：{lines}")
# 一次读取一行内容
# line = f.readline()
# print(f"一次读取一行内容是：{line}")
# line = f.readline()
# print(f"一次读取一行内容是：{line}")

# for循环读取文件行内容
# for line in f:
#     print(f"for循环读取文件行是：{line}")

# 文件关闭，如果不关闭则会一直被占用
# f.close()

# with open 打开文件执行完毕后会自动关闭文件
# with open("../file_read_test.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"for循环读取文件行是：{line}")

# 打开文件，操作模式为"w"是如果文件存在则会覆盖，不存在则会创建文件
# f = open("../file_write_test.txt", "w", encoding="UTF-8")
# 写入内容，暂时只在内存中，还没写入磁盘
# f.write("hello world")
# 将内容刷新到磁盘
# f.flush()
# close方法包含flush功能
# f.close()

# 打开文件，操作模式为"a"是如果文件存在则会追加写，不存在则会创建文件
# f = open("../file_append_test.txt", "a", encoding="UTF-8")
# 写入内容，暂时只在内存中，还没写入磁盘
# f.write("hello world")
# f.write("你好哇")
# f.close()


# 异常
# 捕获指定异常
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(e)

# 捕获多个异常
# try:
#     print(name)
#     1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("出现异常了")

# 捕获所有异常
# try:
#     1 / 0
# except Exception as e:
#     print("出现异常了")

# 可选 else/finally
try:
    1 / 0
    # 1 / 2
except Exception as e:
    print("出现异常了")
else:
    print("没有异常则继续执行 else")
finally:
    print("不管有没有异常，finally 都会执行")


# 模块(模块是一个 Python 文件，里面定义有函数、类、变量等)
# 模块导入方式
# 语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# 常用组合形式如：
# - import 模块名
# - from 模块名 import 类、变量、方法
# - from 模块名 import *
# - import 模块名 as 别名
# - from 模块名 import 功能名 as 别名

# import time # 导入 time 模块
# from time import sleep # 从 time 模块导入 sleep 方法
# from time import * # 从 time 模块导入全部
# import time as t
# from time import sleep as sl

# 自定义模块
import my_module
my_module.func_sum(2,3)

# __name__ == '__main__' 作用：确保某些代码块仅在脚本作为主程序运行时执行，而在被导入时不执行
# __name__ 是 Python 的一个内置变量，表示当前模块的名称。
# 如果脚本是直接运行的，__name__ 的值会被设置为 '__main__'。
# 如果脚本是被其他模块导入的，__name__ 的值会是模块的名称（即文件名去掉 .py 后缀）。

# 自定义包
from my_package import my_pkg_module1
from my_package import my_pkg_module2

# 在 "__init__" 文件中定义 "__all__" 可以控制 import * 能够导入的模块内容
# __all__ = ["my_pkg_module1", "my_pkg_module2"]
from my_package import *
my_pkg_module1.func1()
my_pkg_module2.func2()



# JSON格式转换
import json
# 列表数据转JSON
data = [{"name": "罗辑", "age": 24}, {"name": "章北海", "age": 27}, {"name": "史强", "age": 24}]
json_str = json.dumps(data, ensure_ascii=False)
print(f"json_str类型为：{type(json_str)}, 内容为：{json_str}")
# 字典数据转JSON
dd = {"name": "庄颜", "age": 19}
json_str2 = json.dumps(dd, ensure_ascii=False)
print(f"json_str2类型为：{type(json_str2)}, 内容为：{json_str2}")
# 将JSON数据转为Python数据类型
json1 = '[{"name": "罗辑", "age": 24}, {"name": "章北海", "age": 27}, {"name": "史强", "age": 24}]'
load_data = json.loads(json1)
print(f"load_data类型为：{type(load_data)}, 内容为：{load_data}")
json2 = '{"name": "庄颜", "age": 19}'
load_data2 = json.loads(json2)
print(f"load_data2类型为：{type(load_data2)}, 内容为：{load_data2}")


