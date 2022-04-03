"""
类名：UserService，继承于BaseService
实例属性：
    服务名称：service_name，赋值为'UserService'
实例方法：
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name

    def find_by_username(self, username):
        # 功能：根据用户名查询用户信息
        # :param username: 用户名
        # :return: 1. 如果用户存在，返回用户信息 2. 如果不存在，返回 None

验证结果：
        # 1. 实例化对象
        # 2. 通过实例对象调用实例方法
"""
import json

from api.base_service import BaseService


# 封装 管理员用户 类
class UserService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "UserService"

    def find_by_username(self, usr):
        resp = self.dubbo_client.invoke(self.service_name, "findByUsername", usr)
        if resp == "null":
            # 没有结果
            return None
        else:
            # 还原成 dict 类型
            return json.loads(resp)
