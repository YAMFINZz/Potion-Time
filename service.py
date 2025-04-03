from time import sleep, time
from class_libs import Condition

import json

from jnius import autoclass
PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


DATA_LOCATION: str = 'assets/data/data.json'
def sendMessage():
    from plyer import notification 
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    notification.notify(chan = 1, title = 'Potion TIME!!!', message = '🤍Time to use your Potion!🤍')
    DATA.update({'last_time_msg_sent': int(time())})
    json.dump(DATA, open(DATA_LOCATION, 'w'))


while True:
    if Condition().serviceMessageCondition():
        sendMessage()
    sleep(60)