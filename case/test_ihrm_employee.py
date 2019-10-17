import unittest
import requests
from parameterized import parameterized

import app
from api.emp_api import EmpUser
from tools.login_tools import read_data


class TestIHRMEMP(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp = EmpUser()

    def tearDown(self):
        self.session.close()

    def test_1_emp_add(self):
        add = self.emp.emp_add(self.session, "歌姬", "17145657644","8510011")
        print(add.json())
        id_user = add.json().get("data").get("id")
        app.ID = id_user

    def test_2_emp_update(self):
        update = self.emp.emp_update(self.session,"阿离离")
        print(update.json())

    def test_3_emp_find(self):

        find = self.emp.emp_find(self.session)
        print(find.json())

    def test_4_emp_del(self):

        delete = self.emp.emp_del(self.session)
        print(delete.json())