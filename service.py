from time import sleep
from class_libs import *
from jnius import autoclass

PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)

def isTimeSet() -> bool:
    if (DATA['set_hour'] != None) and (DATA['set_min'] != None):
        timeCalc(DATA['set_hour'], DATA['set_min'])
        return True
    else: return False

def isMessageReady() -> bool:
    return (DATA['last_time_msg_sent'] == 0) or (int(time()) - (DATA['last_time_msg_sent']) > 300)

def sendMessage() -> None:
    DATA.update({'last_time_msg_sent': int(time())})
    json.dump(DATA, open(DATA_LOCATION, 'w'))
    from plyer.platforms.android.notification import AndroidNotification
    AndroidNotification().notify(title = 'Potion TIME!', message = f'📅It\'s {DATA["streak_month"]} month and {DATA["streak_day"]} day📅\n🤍Come here and Check-in🤍',app_icon = 'assets/img/icon/icon.ico')

while True:
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    
    print(f'isTimeSet() : {isTimeSet()}')
    print(f'Condition().isTimeButtonReady() : {Condition().isTimeButtonReady()}')
    print(f'(Condition().timeCon(1, 2) : {(Condition().timeCon(1) or Condition().timeCon(2))}')
    print(f'isMessageReady() : {isMessageReady()}\n')    
    
    if (isTimeSet() and Condition().isTimeButtonReady()) and (Condition().timeCon(1) or Condition().timeCon(2)):
        if isMessageReady(): 
            sendMessage()
    sleep(5)
