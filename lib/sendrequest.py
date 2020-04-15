import logging
import requests

from data.data_driven import load_data, acquire
from lib.utlis import get_test_url


def send_requests(apidata):
    """
    分析测试用例自带参数、发送请求
    :param apidata: 测试用例
    :return:
    """
    try:
        # 从读取的表格中获取响应的参数作为传递
        method = apidata["get_type"]
        url = apidata["url"]
        if apidata["header"] == '':
            header = None
        else:
            header = eval(apidata["header"])
        # 判断表内是否有测试数据
        if apidata["data"] == "":
            body_data = None
        else:
            body_data = eval(acquire(load_data(), apidata['data']))
        s = requests.session()
        re = s.request(method=method, url=get_test_url('loc') + url, headers=header,
                       json=body_data)
        return re
    except Exception as error:
        logging.error("错误信息", error)


if __name__ == '__main__':
    case_dict = {'id': 1.0, 'get_type': 'get', 'interface': '相加接口',
                 'title': '参数正常-成功', 'header': '', 'url': '/add',
                 'data': "{'a': 2, 'b': 1}",
                 'expected': "{'code': 0, 'msg': 'ok', 'value': 3}", 'code': 0,
                 'status': 200, 'msg': 'ok'}
    re = send_requests(case_dict)
    print(re.url)
    print(re.json())
