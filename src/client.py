import constants

print(f"{constants.penis}大作战 v{constants.version}")

import requests, conkits, rich
from conkits import Colors256


def sendApi(type, data):
    return requests.post(
        "http://127.0.0.1:8080/api", json={"type": type, "data": data}
    ).json()


def generatePenis(name, pwd):
    name = input(f"输入{constants.penis}名称：")
    pwd = input(f"输入{constants.penis}密码：")
    sendApi("createUser", {"name": name, "pwd": pwd})
    print("生成成功！")


def connectPenis(name, pwd):
    global savedUsername, savedPassword
    name = input(f"输入{constants.penis}名称：")
    pwd = input(f"输入{constants.penis}密码：")
    result = sendApi("connectUser", {"name": name, "pwd": pwd})
    if result["status"]:
        savedUsername = name
        savedPassword = pwd
        print("连接成功！")
    else:
        print(f"连接失败：{result['message']}")


def showUserInfo(name):
    result = sendApi("getUserInfo", {"name": name})
    print(result)


savedUsername = None
savedPassword = None
selector = conkits.Choice()
selector.unchecked_ansi_code = Colors256.BACK0 + Colors256.FORE255
selector.checked_ansi_code = Colors256.BACK255 + Colors256.FORE0
selector.set_keys({"up": "H", "down": "P", "confirm": "\r"})
selector.run()
selector.set_options([f"生成{constants.penis}", f"连接到{constants.penis}"])
selector.set_methods([generatePenis, connectPenis])
selector.run()
print("")
showUserInfo(savedUsername)
