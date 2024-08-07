import sys, os, importlib, threading

projectRoot = os.path.dirname(__file__)
sys.path.append(projectRoot)
os.chdir(projectRoot)
os.chdir("server")
threading.Thread(target=lambda: importlib.import_module("server")).start()
os.chdir(projectRoot)
os.chdir("client")
importlib.import_module("client")
