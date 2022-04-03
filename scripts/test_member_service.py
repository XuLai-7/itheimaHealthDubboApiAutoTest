"""
# 1. 导入unittest包
# 2. 自定义测试类
# 3. 自定义测试方法
# 注意: 必须以 test 开头(字母必须全小写, 别拼错单词, 例如: text)
"""
import unittest

from parameterized import parameterized

from api.member_service import MemberService

json_data = [{"req": "13020210001", "ass": "13020210001"},
             {"req": "13020212221", "ass": None},
             {"req": "1302021abcd", "ass": None}]


# 定义函数，读取 data/xxx.json 文件
def read_json_data(json_data):
    # with open("../data/ihrm_login.json", "r", encoding="utf-8") as f:
    list_data = []
    for item in json_data:
        tmp = tuple(item.values())
        list_data.append(tmp)

    # 这个 返回，坚决不能在 for 内
    return list_data


# 封装测试类
class TestFindByTelephone(unittest.TestCase):
    ms = None

    @classmethod
    def setUpClass(cls) -> None:
        # 创建一次MemberService类实例
        cls.ms = MemberService()

        # 根据会员手机号查询会员用户信息
        # 测试手机号用例

    # 参数化: 一个接口,一个测试方法
    # 传入 [(),(),(),...]
    # @parameterized.expand(read_json_data(json_data))
    @parameterized.expand([("13020210001", "13020210001"),
                           ("13020212221", None),
                           ("1302021abcd", None)])
    def test_find_by_telephone(self, tel, expect_data):
        resp = self.ms.find_by_telephone(tel)
        # 返回的是字典格式的数据, 直接 get 根据属性值取值
        # resp.json() 是将数据转成 json 格式
        # 这里返回的是 字典格式的数据, 不需要转, 直接用 get 取值
        # 返回的数据 是 None, 用 is, is not 来判断
        # 判断 字符串相等 用 ==, !=
        if resp is not None:
            self.assertEqual(expect_data, resp.get("phoneNumber"))
        else:
            # None 没有 get 属性 会报语法错误
            self.assertEqual(expect_data, resp)

    # ["2021.5"] [3]
    # ["2021.13"] [0]

    # 参数为 字符串列表
    # 返回值为 数值列表
    # 没有加编号,比较的是函数名的字母顺序
    # [([''].[]),([''],[]),...]
    @parameterized.expand([(['2021.5'], [5]),
                           (['2019.4'], [2])])
    def test02_find_memberCount_by_months(self, months, expect_data):
        resp = self.ms.find_member_count_by_months(months)
        print("resp ========= ", resp)
        # print("resp=",resp)
        self.assertEqual(expect_data, resp)

    # 保证手机号唯一
    # {"phoneNumber": "1302021112"}
    # {"fileNumber": "D0001", "name": "李白", "phoneNumber": "13020210002"}
    # {"fileNumber": "D0001", "name": "李白", "phoneNumber": "13020210002"}
    @parameterized.expand([({"phoneNumber": "19887654323"}, True),
                          ({"fileNumber": "D0001", "name": "李白", "phoneNumber": "19887654324"}, True),
                          ({"fileNumber": "D0001", "name": "李白", "phoneNumber": "13020210001"}, False)]
                          )
    def test03_add(self, info, expect_data):
        resp = self.ms.add(info)
        self.assertEqual(expect_data, resp)

    # # 根据会员手机号查询会员用户信息
    # # 手机号存在
    # def test01_tel_exist(self):
    #     resp = self.ms.find_by_telephone("13020210001")
    #     # 返回的是字典格式的数据, 直接 get 根据属性值取值
    #     # resp.json() 是将数据转成 json 格式
    #     # 这里返回的是 字典格式的数据, 不需要转, 直接用 get 取值
    #     self.assertEqual("13020210001", resp.get("phoneNumber"))

    # # 手机号不存在
    # def test02_tel_no_exist(self):
    #     resp = self.ms.find_by_telephone("13020212221")
    #     # 返回的是字典格式的数据, 直接 get 根据属性值取值
    #     self.assertEqual(None, resp)
    #
    # # 手机号包含特殊字符
    # def test03_tel_contain_special_char(self):
    #     resp = self.ms.find_by_telephone("1302021abcd")
    #     # 返回的是字典格式的数据, 直接 get 根据属性值取值
    #     self.assertEqual(None, resp)
