"""
用于生成各种各样的测试数据并可以选择把一次性生成的数据存储到Excel或者数据库
或者用的时候随时生成
"""
from faker import Faker  # 引包

class Random:
    def __init__(self):
        self.f = Faker(locale='zh_CN')  # 初始化实例

    def return_name(self):
        """
        返回随机名字
        :return:
        """
        name = '测试-' + self.f.name()
        return name

    def return_ssn(self):
        """
        返回随机身份证
        :return:
        """
        return self.f.ssn()
