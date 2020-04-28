import requests

json_data = {'a': 2, 'b': 3}

res1 = requests.get("http://127.0.0.1:8000/add", json=json_data, verify=False)
res2 = requests.post("http://127.0.0.1:8000/less", json=json_data, verify=False)

print(res1.json())
print(res2.url)
print(res2.json())
"""
运行后打印
{'code': 0, 'msg': 'ok', 'value': 3}
{'code': 1000, 'msg': 'success', 'value': 1}
"""
