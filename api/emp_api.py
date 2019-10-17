import app


class EmpUser:

    def emp_add(self,session,username,mobile,workNumber):
        add_user = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-07-01",
            "formOfEmployment": 1,
            "workNumber": workNumber,
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2019-11-30"
        }
        return session.post("{}api/sys/user".format(app.BASE_URL), json=add_user,headers ={"Authorization" :"Bearer " + app.TOKEN})

    def emp_update(self,session,username):

        update_username = {"username":username}

        return session.put("{}api/sys/user/{}".format(app.BASE_URL,app.ID), json=update_username,headers ={"Authorization" :"Bearer " + app.TOKEN})

    def emp_find(self,session):

        return session.get("{}api/sys/user/{}".format(app.BASE_URL,app.ID),headers ={"Authorization" :"Bearer " + app.TOKEN})

    def emp_del(self,session):

        return session.delete("{}api/sys/user/{}".format(app.BASE_URL,app.ID),headers ={"Authorization" :"Bearer " + app.TOKEN})