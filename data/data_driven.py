import codecs
import json

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
