import json

from app import PRO_PATH


def read_data():
    login_text_data = []
    with open("{}\\data\\login_data.JSON".format(PRO_PATH),"r",encoding="utf-8") as f:
        case_data = json.load(f)
        for test_data in case_data.values():
            # print(test_data)
            data_1 = []
            for data_2 in test_data.values():
                data_1.append(data_2)
            # print(data_1)
            login_text_data.append(data_1)
        # print(login_text_data)
    return login_text_data