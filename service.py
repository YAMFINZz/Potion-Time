from time import sleep
from class_libs import serviceSystem
from jnius import autoclass


PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


while True:
    serviceSystem()
    sleep(60)