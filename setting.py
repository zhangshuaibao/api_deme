import os

BASE_URL = "http://127.0.0.1:8000"
BASE_URL_dev = 'http://127.0.0.1:8000'
BASE_URL_uat = 'http://127.0.0.1:8000'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

case_root = os.path.join(PROJECT_ROOT, 'database')  # 测试用例
results_root = os.path.join(PROJECT_ROOT, 'results', 'results.xlsx')  # 测试结果
LOG_PATH = os.path.join(PROJECT_ROOT, 'log', 'api_test.log')  # 日志
REPORT_PATG = os.path.join(PROJECT_ROOT, 'report', 'index.html')  # 日志
TEST_JSON = os.path.join(PROJECT_ROOT, 'database', 'test_data.txt')  # 存放接口返回数据
