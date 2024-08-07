import constants
from response import *
from file import *

users: dict = loadJson("data/users.json")


class ApiResponse:
    def createUser(arg):
        if arg["name"] in list(users.keys()):
            return create_response(False, f"已存在名为{arg['name']}的{constants.penis}")
        users[arg["name"]] = {"password": arg["password"], "length": 1}
        dumpJson(users, "data/users.json")
        return create_response(True)

    def connectUser(arg):
        if arg["name"] not in list(users.keys()):
            return create_response(False, f"不存在名为{arg['name']}的{constants.penis}")
        if arg["password"] != users[arg["name"]]["password"]:
            return create_response(False, "密码错误")
        return create_response(True)

    def getUserInfo(arg):
        if arg["name"] not in list(users.keys()):
            return create_response(False, f"不存在名为{arg['name']}的{constants.penis}")
        result = users[arg["name"]].copy()
        del result["password"]
        return create_response(True, result)
