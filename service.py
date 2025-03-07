from jnius import autoclass

PythonService = autoclass(u'org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)

from kivy.clock import Clock

def messageService(*args):
    from main import Condition, isTimeSet
    
    if isTimeSet and Condition().isTimeButtonReady() and (Condition().timeCon(1) or Condition().timeCon(2)):
        if Condition().isMessageReady():
            Condition().sendMessage()

Clock.schedule_interval(messageService, 1)
