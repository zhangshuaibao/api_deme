import codecs
import json
import re
import setting
from lib.Random import Random


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

def return_function_data(data):
    """
    返回随机生成的的数据
    :return:
    """
    # 返回随机名字
    if data == 'name':
        return Random().return_name()
    # 返回随机身份证
    elif data == 'ssn':
        return Random().return_ssn()

def load_data(msg) -> dict:
    """
    返回test_data内的数据
    :return:
    """
    if msg.startswith('^'):
        data = msg.replace('^', '')
        return return_function_data(data)

    for line in open(setting.TEST_JSON):
        if data_processing(line).get(msg) is not None:
            return data_processing(line).get(msg)

    return False


def return_extracted_data(result, name, rule):
    """
    处理数据，使用rule匹配规则匹配数据并且返回
    :param result:  返回数据
    :param name:  变量名（返回数据的健）
    :param rule: 获取值的匹配规则
    :return: 完整数据
    """
    extracted_data = eval('{}'.format(result) + rule)  # 通过匹配规则匹配出需要的数据格式
    data = str({'{}'.format(name): extracted_data})
    return data

def write_data(msg, name, result, rule):
    if msg == 'res':
        # 为1：将内容写进test_data文件用来替换下个接口的参数
        if load_data(name) is False:
            with codecs.open(setting.TEST_JSON, 'a+', encoding='utf-8') as f:
                f.write(return_extracted_data(result, name, rule))
                f.write('\r\n')


def data_association(request_data):
    """
    判断是否调用上一个接口返回的数据当此次访问的参数，并返回数据
    :param replace_data: 上个接口返回的数据
    :param request_data: 当前接口的请求测试数据
    :return:请求参数 dict格式
    """
    # 正则表达式带^特殊符号开头的内容
    pattern = re.compile(r"'\$([\s\S]+?)'")
    # 拿到匹配的内容 key列表内的值为replace_data的键
    keys = re.findall(pattern, str(request_data))
    # 如果request_data内没有^，直接返回原数据
    if len(keys) <= 0:
        return request_data
    # 当前匹配出来的内容
    present = []
    # 拿着这个key 去上个接口里面得到想要的内容
    for key in keys:
        key = str(key).replace('{', '').replace('}', '')
        a = load_data(key)
        # 每次匹配出来内容都进行遍历装进list中
        present.append(a)
    # 从index 0开始  根据原值内容 直接进行替换，然后直接返回
    for i in range(0, len(present)):
        # key[i]是原来的值  present是获取的值 最后将特殊符号处理掉
        request_data = str(request_data).replace(keys[i], str(present[i])).replace('$', '')
    return request_data


if __name__ == '__main__':
    """
    用test_data数据{'code': 0, 'msg': 'ok', 'value': 3}中的code,value的值分别代替data内的code,value
    """
    data = {'a': '^code', 'b': '^value'}
    print('test_data内的数据:', load_data())  # test_data内的数据（接口1返回的结果）
    print('替换前的参数:', data)  # 未替换前的参数
    print('替换后的参数:', data_association(load_data(), data))  # 替换完成后的参数（接口2的请求数据）
