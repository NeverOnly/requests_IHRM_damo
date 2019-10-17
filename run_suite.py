import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from app import PRO_PATH

import tkinter.messagebox

from case.test_ihrm_employee import TestIHRMEMP
from case.test_ihrm_login import TestIHRM

top = tkinter.Tk()
top.title("hello world")
# 设置窗口大小
top.geometry("300x200")
# 设置窗口是否可以改变宽高
top.resizable(width=False,height=False)
def runtest():

    suite = unittest.TestSuite()
    suite.addTest(TestIHRM("test_success_login"))
    suite.addTest(unittest.makeSuite(TestIHRMEMP))


    report_path = "{}/report/test_emp.html".format(PRO_PATH))

    with open(report_path,"wb") as f:
        runner = HTMLTestRunner(f, title="测试报告")
        runner.run(suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

btn = tkinter.Button(top,text = "执行测试用例",command = runtest).place(x=105,y=70)


# 将按钮放置在窗口中
# btn.pack()

# 进入消息循环
top.mainloop()



