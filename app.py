# 封装资源路径前缀
import os

BASE_URL="http://182.92.81.159/"
TOKEN = None
ID = None
# 获取项目绝对路径
ABS_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(ABS_PATH)
# print("当前文件 app.py 的绝对路径:",ABS_PATH)
# print("当前项目的绝对路径:",PRO_PATH)