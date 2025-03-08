from jnius import autoclass

PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)


from time import sleep

def messageService():
    from main import Condition, isTimeSet
    while True:
        print(f'Service Checking | isTimeSet : {isTimeSet}')
        if isTimeSet and Condition().isTimeButtonReady() and (Condition().timeCon(1) or Condition().timeCon(2)):
            if Condition().isMessageReady():
                Condition().sendMessage()
        sleep(1)

messageService()