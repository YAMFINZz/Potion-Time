from time import sleep
from class_libs import *
from jnius import autoclass


PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


def isMessageReady() -> bool:
    return (DATA['last_time_msg_sent'] == 0) or (int(time()) - (DATA['last_time_msg_sent']) > 300)


def sendMessage():
    from plyer import notification
    notification.notify(chan = 0,
                        title = 'Potion TIME!!!',
                        message = '🤍Time to use your Potion!🤍'
                        )
    DATA.update({'last_time_msg_sent': int(time())})
    json.dump(DATA, open(DATA_LOCATION, 'w'))


while True:
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    
    print("Service Running")

    if (Condition().isTimeSet() and Condition().isTimeButtonReady()) and (Condition().timeCon(1) or Condition().timeCon(2)):
        if isMessageReady():
            sendMessage()
            print("MESSAGE SENDING")
    sleep(60)