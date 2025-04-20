# -*- coding: utf-8 -*-

"""
- 闭包、nonlocal
- 装饰器(闭包应用)
"""

# 闭包
# 闭包：定义双层嵌套函数，内层函数可以访问外层函数变量，将内层函数作为外层函数的返回值，此内层函数就是闭包函数
# 优点：不定义全局变量，可以让函数持续访问和修改一个外部变量；闭包函数引用的外部变量是外层函数的内部变量，作用域封闭难以被误操作修改
# nonlocal：在闭包函数(内部函数)想要修改外部函数的变量需要使用nonlocal关键字声明外部变量
# 简单闭包
def outer(company):

    def inner(msg):
        print(f"<{company}>{msg}<{company}>")

    return inner


fn1 = outer("三体宇宙")
fn1("叶文洁")
fn1("罗辑")

# 闭包实现ATM存取款
def account_create(initial_amount=0):

    def atm(num, deposit=True):

        # 在闭包函数(内部函数)想要修改外部函数的变量需要使用nonlocal关键字声明外部变量
        nonlocal initial_amount
        if deposit: # 存款
            initial_amount += num
            print(f"存款：+{num}, 账户余额：{initial_amount}")
        else: # 取款
            initial_amount -= num
            print(f"取款：-{num}, 账户余额：{initial_amount}")

    return atm

atm = account_create(0)
atm(100, True)
atm(800, True)
atm(300, False)


# 装饰器(闭包应用)
def my_decorator(func):
    def wrapper():
        print("方法执行前记录日志")
        func()
        print("方法执行后记录日志")
    return wrapper

def func1():
    print("执行函数方法")

# 原始调用方式
fn = my_decorator(func1)
fn()

# 装饰器语法糖
@my_decorator
def func2():
    print("执行函数方法")
# 直接调用
func2()