from time import sleep
from class_libs import *
from jnius import autoclass


PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)



def sendMessage():
    from plyer import notification
    notification.notify(chan = 0, title = 'Potion TIME!!!', message = '🤍Time to use your Potion!🤍')
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    DATA.update({'last_time_msg_sent': int(time())})
    json.dump(DATA, open(DATA_LOCATION, 'w'))



if __name__ == "__main__":
    while True:
        if Condition().isTimeSet(): 
            if Condition().isTimeButtonReady():
                if Condition().timeCon(1) or Condition().timeCon(2):
                    if Condition().isMessageReady():
                        sendMessage()
        sleep(60)