# -*- coding: utf-8 -*-

"""
面向对象
- 类定义、self、构造方法、内置魔术方法
- 封装、私有成员
- 继承
- pass 占位语句(用于保证方法或类定义的完整性，表示无内容，空的意思)
- 复写(对父类的成员属性或方法进行重新定义)
- 多态、抽象类
"""

# 类定义
# self：表示类对象本身，只有通过self成员方法才能访问类的成员变量，self必须出现在方法形参列表中，使用时不占用参数位置，可忽略
class Student:
    # 构造方法中使用过的字段已经声明可忽略
    # name = None
    # age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"大家好，我叫：{self.name}, 我今年：{self.age} 岁")

    # 其它魔术方法
    # __str__：类对象转字符串行为
    def __str__(self):
        return f"Student对象：name: {self.name}, age: {self.age}"

    # __lt__：2个类对象进行大于或小于比较
    def __lt__(self, other):
        return self.age < other.age
    # __le__：2个类对象进行大于等于或小于等于比较
    def __le__(self, other):
        return self.age <= other.age
    # __eq__：2个类对象进行相等比较
    def __eq__(self, other):
        return self.age == other.age

s1 = Student("庄颜", 19)
s1.hello()
print(s1)
s2 = Student("罗辑", 19)
print(s1 > s2)
print(s1 <= s2)
print(s1 == s2)


# 封装、私有成员
# 私有成员：私有成员变量、成员方法都以"__"作为开头，类对象无法访问私有成员，类中其它成员可以访问私有成员
class Phone:

    __current_voltage = 0.5 # 当前电压

    def __single_core_run(self):
        print("单核运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__single_core_run()
            print("电压不足，设置为单核运行")

phone = Phone()
phone.call_by_5g()

# 继承
class BasePhone:
    memory = None # 内存
    producer = "中芯国际" # 厂商

    def call(self):
        print("打电话基础功能")

# 单继承
class XiaomiPhone(BasePhone):
    rc_type = "红外遥控"

    def control(self):
        print("小米遥控开启了")

xmPhone = XiaomiPhone()
xmPhone.call()
xmPhone.control()


class NFCReader:
    nfc_type = "5"
    producer = "HW"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

# 多继承
# 多继承中，如果父类有同名方法或属性，先继承的优先级高于后继承的
class HuaweiPhone(BasePhone, NFCReader):
    satellite_frequency = 100 # 卫星频率

    def satellite_comm(self):
        print("华为卫星通话")

hwPhone = HuaweiPhone()
hwPhone.call()
hwPhone.read_card()
hwPhone.satellite_comm()

# pass 占位语句(用于保证方法或类定义的完整性，表示无内容，空的意思)
class ApplePhone(BasePhone, NFCReader):
    pass

# 复写(对父类的成员属性或方法进行重新定义)
class OppoPhone(BasePhone):

    producer = "OPPO"

    def call(self):
        print("OPPO打电话开启通话录音")
        print("OPPO打电话通话中")

opPhone = OppoPhone()
opPhone.call()
print(opPhone.producer)

# 调用父类同名成员
# 方式1：调用父类成员
# 使用成员变量：父类名.成员变量
# 使用成员方法：父类名.成员方法(self)
# 方法2：使用super()调用父类成员
# 使用成员变量：super().成员变量
# 使用成员方法：super().成员方法()
class VivoPhone(BasePhone):

    producer = "VIVO"

    def call(self):
        # 方式1：父类名调用父类成员
        print(f"父类品牌是：{BasePhone.producer}")
        # 方式1：父类名调用父类方法
        BasePhone.call(self)
        # 方式2：super()调用父类成员
        print(f"父类品牌是：{super().producer}")
        # 方式2：super()调用父类方法
        super().call()

ovPhone = VivoPhone()
ovPhone.call()
print(ovPhone.producer)


# 多态、抽象类
# 多态：同一个行为使用不同对象获得不同状态，比如定义方法时，通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态
# 抽象类：包含抽象方法的类，抽象方法是指没有具体实现的方法(pass)。抽象类用于做顶层设计，设计标准规范，以变子类做具体实现

class Animal:
    # 抽象方法
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

def speak(animal: Animal):
    animal.speak()

# 多态测试
dog = Dog()
cat = Cat()
speak(dog)
speak(cat)

