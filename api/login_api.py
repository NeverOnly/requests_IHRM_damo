# 封装case中所需要的请求业务
import app


class UserLogin:
    # 登录请求
    def login_into(self,session,mobile,password):
        mydata = {"mobile": mobile, "password": password}
        return session.post("{}api/sys/login".format(app.BASE_URL), json=mydata)
