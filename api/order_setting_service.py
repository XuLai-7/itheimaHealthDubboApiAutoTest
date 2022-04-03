"""
类名：OrderSettingService，继承于 BaseService
实例属性：
    服务名称：service_name，赋值为 'OrderSettingService'
实例方法：
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name

    def add(self, date_list):
        # 功能：添加预约设置
        # :param date_list:
        #     1.  日期列表，如：[{"orderDate":"2021-09-20 16:45:12","number":20}]
        #     2. 日期格式为："2021-09-20 16:45:12"，必须包括时分秒
        # :return: 设置成功返回True,  设置失败返回False

    def get_order_setting_by_month(self, date):
        # 功能：按月统计预约设置信息
        # :param date: 日期，如："2021-08"
        # :return: 列表，指定月份的预约信息

    def edit_number_by_date(self, info): 根据日期修改预约设置数量
        # 功能：根据日期修改预约设置数量
        # :param info:
        #     1. 预约设置的字典格式数据，参考接口文档填入字段数据
        #     2. 如：{"orderDate":"2021-09-19 17:45:12","number":15}
        #     3. 日期格式为："2021-09-19 17:45:12"，必须包括时分秒
        #     4. 添加 "class":"com.itheima.pojo.OrderSetting"
        # :return: 修改成功返回 True,  修改失败返回 False
验证结果：
        # 1. 实例化对象
        # 2. 通过实例对象调用实例方法
        # 2.1 添加预约设置
        # 2.2 按月统计预约设置信息
        # 2.3 根据日期修改预约设置数量
"""
import json

from api.base_service import BaseService



# 将 预约设置服务 封装成 预约设置服务类
class OrderSettingService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "OrderSettingService"

    def add(self, date_list):
        resp = self.dubbo_client.invoke(self.service_name, "add", date_list)
        if resp == "null":
            return True
        else:
            return False

    def get_order_setting_by_month(self, months):
        resp = self.dubbo_client.invoke(self.service_name, "getOrderSettingByMonth", months)
        if resp == "Failed":
            # 错误, 没有返回数据, 直接返回 None
            return None
        else:
            return json.loads(resp)

    def edit_number_by_date(self, info):
        # 自定义类型, 数据需要用 字典类型组织, 加上 class: 包名.类名 字段
        info["class"] = "com.itheima.pojo.OrderSetting"
        resp = self.dubbo_client.invoke(self.service_name, "editNumberByDate", info)
        if resp == "null":
            return True
        else:
            return False

