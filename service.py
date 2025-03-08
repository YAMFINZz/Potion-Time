from jnius import autoclass

PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)

from time import sleep
from class_libs import *

while True:
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    print("Service Running for it's life...")
    if (DATA['set_hour'] != None) and (DATA['set_min'] != None):
        isTimeSet: bool = True
        timeCalc(DATA['set_hour'], DATA['set_min'])
    else: 
        isTimeSet: bool = False
    
    if isTimeSet and Condition().isTimeButtonReady() and (Condition().timeCon(1) or Condition().timeCon(2)):
        if Condition().isMessageReady():
            print("FUCKING MESSAGE IS SENDING")
    sleep(1)