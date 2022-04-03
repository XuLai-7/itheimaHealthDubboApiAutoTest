"""
基础服务类: 创建 dubboclient 实例
"""
from dubboclient import DubboClient


class BaseService:
    # 实例属性写在 __init__ 方法中
    # 创建该类的实例, 就有该属性
    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)
