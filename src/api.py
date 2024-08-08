import constants, random
from response import *
from file import *

userDataPath = "../data/users.json"
users: dict = loadJson(userDataPath)


def normalLength(userLength, muiltiplier=1):
    return (random.random() * 0.01) * userLength * toFixed0(userLength) + muiltiplier


def toFixed0(num):
    return -1 if num < 0 else 1 if num > 0 else 1


class ApiResponse:
    needLogined = ["growNormal", "fightWith", "insertWith"]

    def createUser(arg):
        if arg["name"] in list(users.keys()):
            return create_response(False, f"已存在名为{arg['name']}的{constants.penis}")
        users[arg["name"]] = {
            "password": arg["password"],
            "length": 10,
            "dnaIn": 0,
            "dnaOut": 0,
        }
        dumpJson(users, userDataPath)
        return create_response(True)

    def connectUser(arg):
        if arg["name"] not in list(users.keys()):
            return create_response(False, f"不存在名为{arg['name']}的{constants.penis}")
        if arg["password"] != users[arg["name"]]["password"]:
            return create_response(False, "密码错误")
        return create_response(True)

    def getUserInfo(arg):
        result = users[arg["name"]].copy()
        del result["password"]
        return create_response(True, result)

    def growNormal(arg):
        grown = normalLength(users[arg["name"]]["length"])
        users[arg["name"]]["length"] += grown
        dumpJson(users, userDataPath)
        return create_response(
            True, {"grown": grown, "length": users[arg["name"]]["length"]}
        )

    def getUserList(arg):
        return create_response(True, {"result": list(users.keys())})

    def fightWith(arg):
        result = random.random() < 0.5
        if result:
            grown = normalLength(users[arg["name"]]["length"])
            target = normalLength(users[arg["target"]]["length"], 3)
            users[arg["name"]]["length"] += grown
            users[arg["target"]]["length"] -= target
        else:
            grown = normalLength(users[arg["name"]]["length"], 3)
            target = normalLength(users[arg["target"]]["length"])
            users[arg["name"]]["length"] -= grown
            users[arg["target"]]["length"] += target
        dumpJson(users, userDataPath)
        return create_response(
            True,
            {
                "result": result,
                "grown": grown,
                "target": target,
                "length": users[arg["name"]]["length"],
            },
        )

    def insertWith(arg):
        breaken = normalLength(users[arg["name"]]["length"])
        dnaIn = 5 + random.random() * random.choice([-1, 1])
        users[arg["name"]]["length"] -= breaken
        users[arg["target"]]["dnaIn"] += dnaIn
        users[arg["name"]]["dnaOut"] += dnaIn
        dumpJson(users, userDataPath)
        return create_response(True, {"breaken": breaken, "dnaIn": dnaIn})

    def ping(arg):
        return create_response(True, "PENIS_WARS")
