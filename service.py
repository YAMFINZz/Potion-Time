from time import sleep
from class_libs import *
from jnius import autoclass
from main import sendMessage

PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)

def isTimeSet() -> bool:
    if (DATA['set_hour'] != None) and (DATA['set_min'] != None):
        timeCalc(DATA['set_hour'], DATA['set_min'])
        return True
    else: return False

def isMessageReady() -> bool:
    return (DATA['last_time_msg_sent'] == 0) or (int(time()) - (DATA['last_time_msg_sent']) > 300)

while True:
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    
    if (isTimeSet() and Condition().isTimeButtonReady()) and (Condition().timeCon(1) or Condition().timeCon(2)):
        if isMessageReady():
            sendMessage()
    sleep(5)