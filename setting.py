import os

BASE_URL = "http://127.0.0.1:8000"
BASE_URL_dev = 'http://127.0.0.1:8000'
BASE_URL_uat = 'http://127.0.0.1:8000'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

case_root = os.path.join(PROJECT_ROOT, 'database', 'testcase.xlsx')
results_root = os.path.join(PROJECT_ROOT, 'tesults', 'tesults.xlsx')
TEST_JSON = os.path.join(PROJECT_ROOT, 'database', 'token')
TEST_CONFIG = os.path.join(PROJECT_ROOT, 'database', 'tox.ini')
