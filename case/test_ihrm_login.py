import unittest
import requests
from parameterized import parameterized

import app
from api.login_api import UserLogin
from tools.login_tools import read_data


class TestIHRM(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.user_login = UserLogin()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_data())
    def test_login(self,mobile,password,response_code,success,code,message):

        login = self.user_login.login_into(self.session,mobile,password)
        self.assertEqual(response_code,200)
        self.assertEqual(success,login.json().get("success"))
        self.assertEqual(code,login.json().get("code"))
        self.assertIn(message,login.json().get("message"))

    def test_success_login(self):
        login = self.user_login.login_into(self.session, "13800000002", "123456")
        print(login.json())
        app.TOKEN = login.json().get("data")
        print(app.TOKEN)
        self.assertEqual(True,login.json().get("success"))
        self.assertEqual(10000,login.json().get("code"))
        self.assertIn("操作成功",login.json().get("message"))