# -*- coding: utf-8 -*-

"""
- 单例模式
- 工厂模式
"""

# 单例模式
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)


# 工厂模式
# 工厂模式：将对象的创建由原生类本身创建转换为由特定的工厂方法来创建
class Dog:
    def speak(self):
        return "汪汪汪"

class Cat:
    def speak(self):
        return "喵喵喵"

# 工厂类
class AnimalFactory:

    def get_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

factory = AnimalFactory()
dog = factory.get_animal("dog")
print(dog.speak())
cat = factory.get_animal("cat")
print(cat.speak())