import constants

print(f"{constants.penis}大作战 v{constants.version}")

import requests, conkits, msvcrt, sys, colorama
from conkits import Colors256
from rich import print


def sendApi(type, data={}):
    return requests.post(
        f"{savedServerAddress}/api", json={"type": type, "data": data}
    ).json()


def generatePenis():
    global savedUsername, savedPassword
    name = input(f"输入{constants.penis}名称：")
    pwd = input(f"输入{constants.penis}密码：")
    result = sendApi("createUser", {"name": name, "password": pwd})
    if result["status"]:
        savedUsername = name
        savedPassword = pwd
        print("生成成功！")
    else:
        print(f"生成失败：{result['message']}")
        block()


def connectPenis():
    global savedUsername, savedPassword
    name = input(f"输入{constants.penis}名称：")
    pwd = input(f"输入{constants.penis}密码：")
    result = sendApi("connectUser", {"name": name, "password": pwd})
    if result["status"]:
        savedUsername = name
        savedPassword = pwd
        print("连接成功！")
    else:
        print(f"连接失败：{result['message']}")
        block()


def showUserInfo(name):
    result = sendApi("getUserInfo", {"name": name})
    print(f"---- {savedUsername}的{constants.penis} ----")
    print(f"{constants.penis}长度：{result['message']['length']}cm")
    print(f"注射总量：{result['message']['dnaOut']}ml")
    print(f"总被注射：{result['message']['dnaIn']}ml，真是一群变态")
    print("")


def showUserInfoPlain():
    showUserInfo(savedUsername)


def growUp():
    result = sendApi("growNormal", {"name": savedUsername, "password": savedPassword})
    print(f"导管成功，你的{constants.penis}很满意~")
    print(f"{constants.penis}努力生长了{result['message']['grown']}cm")
    print(f"你的{constants.penis}一共有{result['message']['length']}cm了")


def fight():
    userList: list = sendApi("getUserList")["message"]["result"]
    userList.remove(savedUsername)

    def _fightWith(name):
        result = sendApi(
            "fightWith",
            {"name": savedUsername, "password": savedPassword, "target": name},
        )["message"]
        if result["result"]:
            print(f"对决成功了哦~")
            print(
                f"你的{constants.penis}增长了{result['grown']}cm了，但是对方因为不堪受辱，{constants.penis}缩小了{result['target']}cm"
            )
        else:
            print(f"对决失败了，你个废材！")
            print(
                f"你的{constants.penis}不堪受辱缩小了{result['grown']}cm了，但是对方洋洋得意，Ta的{constants.penis}当着你的面增长了{result['target']}cm"
            )
        print(f"你的{constants.penis}现在是{result['length']}cm了")

    fightMethods = []
    for user in userList:
        fightMethods.append(lambda: _fightWith(user))
    selector.set_options(userList)
    selector.set_methods(fightMethods)
    selector._current_index = 0
    print("选择你要对决的对手：")
    selector.run()


def insert():
    userList: list = sendApi("getUserList")["message"]["result"]
    userList.remove(savedUsername)

    def _insertWith(name):
        result = sendApi(
            "insertWith",
            {"name": savedUsername, "password": savedPassword, "target": name},
        )["message"]
        print("卧槽，为什么这么紧，这家伙没少被透，好熟练，你的牛牛要被夹爆了！")
        print(
            f"你损伤了{result['breaken']}cm牛子，给Ta注射了{result['dnaIn']}ml的脱氧核糖核酸~"
        )

    fightMethods = []
    for user in userList:
        fightMethods.append(lambda: _insertWith(user))
    selector.set_options(userList)
    selector.set_methods(fightMethods)
    selector._current_index = 0
    print("选择你要后入的人：")
    selector.run()


def block():
    print("按下任意键退出...")
    msvcrt.getch()
    sys.exit()


def empty():
    pass


def officialConnect():
    global savedServerAddress
    savedServerAddress = "http://154.44.26.86:8080"


def customConnect():
    global savedServerAddress
    savedServerAddress = input("输入服务器地址：")


colorama.init(autoreset=False)
savedServerAddress = None
savedUsername = None
savedPassword = None
selector = conkits.Choice()
selector.set_keys({"up": "H", "down": "P", "confirm": "\r"})
print("\n选择一个服务器线路：")
selector.set_options(["官方服务器", "自定义连接"])
selector.set_methods([officialConnect, customConnect])
selector.run()
try:
    print(f"正在连接到{savedServerAddress}")
    if sendApi("ping")["message"] != "PENIS_WARS":
        raise
except:
    print(f"无法连接到{savedServerAddress}，请检查网络连接")
    block()
finally:
    print("连接成功！\n")
selector.set_options([f"生长{constants.penis}", f"连接到{constants.penis}"])
selector.set_methods([generatePenis, connectPenis])
selector.run()
print("")
showUserInfo(savedUsername)
while True:
    selector._current_index = 0
    selector.set_options(["导管", f"查看{constants.penis}", "对决", "后入"])
    selector.set_methods([growUp, showUserInfoPlain, fight, insert])
    selector.run()
