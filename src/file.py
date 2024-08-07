import json

_backOpen = open


def open(path, writable=False, binary=False, encoding="utf-8"):
    return _backOpen(
        path, ("w" if writable else "r") + ("b" if binary else ""), encoding=encoding
    )


def loadJson(path):
    return json.load(open(path))


def dumpJson(obj, path):
    json.dump(obj, open(path, True), indent=4, ensure_ascii=False)
