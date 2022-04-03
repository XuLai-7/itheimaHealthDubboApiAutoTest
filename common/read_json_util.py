import json


# 定义函数，读取 data/xxx.json 文件
def read_json_data(filname):
    # with open("../data/ihrm_login.json", "r", encoding="utf-8") as f:
    with open(filname, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            tmp = tuple(item.values())
            list_data.append(tmp)

    # 这个 返回，坚决不能在 for 内
    return list_data


if __name__ == '__main__':
    ret = read_json_data()
    print(ret)