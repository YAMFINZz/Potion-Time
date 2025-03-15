from time import sleep
from class_libs import *
from jnius import autoclass


PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


def sendMessage():
    from plyer import notification
    notification.notify(chan = 1, title = 'Potion TIME!!!', message = '🤍Time to use your Potion!🤍')
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    DATA.update({'last_time_msg_sent': int(time())})
    json.dump(DATA, open(DATA_LOCATION, 'w'))


while True:
    print("Service Running...")
    if Condition().serviceMessageCondition():
        print("Sending Message")
    sleep(1)