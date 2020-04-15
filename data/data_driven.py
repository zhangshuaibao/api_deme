import codecs
import json
import re
import requests
import setting


def data_processing(variate):
    """
    判断数据类型是否为字典，若不是dict则转换成dict
    :param variate:  数据
    :return:  dict
    """
    global null
    null = ''
    if isinstance(variate, str):
        return eval(variate)
    elif isinstance(variate, dict):
        return variate
    elif variate is None:
        return None


def write_data(user, pwd):
    """
    将获取的token写入文件
    :param user: 账号
    :param pwd: 密码
    :return:
    """
    url = '127.0.0.1'
    data = {
        'user': user,
        'pwd': pwd
    }
    res = requests.post(url=url, json=data)
    token = res.json()['token']
    # 需写入的内容
    t = {'token': '{}'.format(token)}
    with codecs.open(setting.TEST_JSON, 'w', encoding='utf-8') as f:
        json.dump(t, f)


def load_data(msg=False, user=None, pwd=None) -> dict:
    """
    读取文件内token
    :param msg: Ture：获取token并写入 False：读取文件内token
    :param user: 账号
    :param pwd: 密码
    :return: token
    """
    if msg:
        write_data(user, pwd)
    else:
        pass

    with open(setting.TEST_JSON, encoding='utf-8') as file_obj:
        for line in file_obj:
            token_data = json.loads(line)
            return token_data


def acquire(last_content, this_content):
    """
    判断是否调用上一个接口返回的数据当此次访问的参数
    :param last_content: 上个接口返回的数据
    :param this_content: 当前接口的请求测试数据
    :return:测试数据
    """
    # 使用正则去里面寻找带^特殊符号开头的内容
    pattern = re.compile(r"'\^([\s\S]+?)'")
    # 拿到匹配的内容 是上个接口的key值
    keys = re.findall(pattern, str(this_content))
    # 如果当前content里面没有^这个符号，则直接返回
    if len(keys) <= 0:
        return this_content
    # 承载当前匹配出来的内容
    present = []
    # 拿着这个key 去上个接口里面得到想要的内容
    for key in keys:
        a = last_content['{}'.format(key)]
        # 每次匹配出来内容都进行遍历装进list中
        present.append(a)
    # 从index 0开始  根据原值内容 直接进行替换，然后直接返回
    for i in range(0, len(present)):
        # key[i]是原来的值  present是获取的值 最后将特殊符号处理掉
        this_content = str(this_content).replace(keys[i], str(present[i])).replace('^', '')
    return this_content
