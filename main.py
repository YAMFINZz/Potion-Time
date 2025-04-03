from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivy.lang import Builder

from class_libs import *
from time import time
import json

BG_MAIN, BG_MAIN_ON_TIME = ['assets/img/bg/bg.png', 'assets/img/bg/bg_ontime.png']
BG_HOME_UNREADY, BG_HOME_READY = ['assets/img/bg/bg_home_unready.png', 'assets/img/bg/bg_home_ready.png']

DATA_LOCATION: str = 'assets/data/data.json'
DATA: dict = json.load(open(DATA_LOCATION, "r"))

class Manager(ScreenManager):
    def __init__(self):
        super().__init__()
        self.transition = NoTransition()
        if Condition().isTimeSet():
            timeCalc(DATA['set_hour'], DATA['set_min'])
            self.current = 'main'
        else:
            self.current = 'home'

class Home(Screen):
    set_hour, set_min = [StringProperty(), StringProperty()]
    eye_btn_disabled = BooleanProperty()
    
    background_home = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_home = BG_HOME_UNREADY
        self.eye_btn_disabled = True
    
    def on_enter(self):
        self.setHintText()
    
    def setHintText(self):
        if DATA['set_hour'] == None: self.set_hour = 'Hours ---> 0 - 23'
        else: self.set_hour = f'Now set at hour : {DATA["set_hour"]}'
            
        if DATA['set_min'] == None: self.set_min = 'Minutes ---> 0 - 59'
        else: self.set_min = f'Now set at minute : {DATA["set_min"]}'
    
    def checkSetTime(self):
        if ((self.ids['Hours'].text != '') and (self.ids['Minutes'].text != '')):
            self.background_home = BG_HOME_READY
            self.eye_btn_disabled = False
        else:
            self.background_home = BG_HOME_UNREADY
            self.eye_btn_disabled = True
    
    def setTimeOutOfBound(self, sender):
        try:
            match sender:
                case 1:
                    if int(self.ids['Hours'].text) > 23: self.ids['Hours'].text = '23'
                    elif int(self.ids['Hours'].text) < 0: self.ids['Hours'].text = '0'
                case 2:
                    if int(self.ids['Minutes'].text) > 59: self.ids['Minutes'].text = '59'
                    elif int(self.ids['Minutes'].text) < 0: self.ids['Minutes'].text = '0'            
        except ValueError:
            pass
    
    def setTimeInJSON(self):
        DATA.update({'set_hour': int(self.ids['Hours'].text), 'set_min': int(self.ids['Minutes'].text)})
        json.dump(DATA, open(DATA_LOCATION, 'w'))
        timeCalc(DATA['set_hour'], DATA['set_min'])
        self.ids['Hours'].text, self.ids['Minutes'].text = ['', '']

class Main(Screen):
    time_btn_disabled = BooleanProperty()
    time_btn_transparent = ObjectProperty()

    background_main = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setNormal()

    def on_pre_enter(self):
        self.updater = Clock.schedule_interval(self.Check_Time, 1)
        self.updater()

    def setNormal(self) -> None:
        self.time_btn_transparent = 0
        self.time_btn_disabled = True
        self.background_main = BG_MAIN

    def Check_Time(self, *args) -> None:
        if Condition().isTimeButtonReady() and (Condition().timeCon(1) or Condition().timeCon(2)):
            self.time_btn_transparent = 1
            self.time_btn_disabled = False
            self.background_main = BG_MAIN_ON_TIME
        else:
            self.setNormal()
        
    def Streak(self) -> None:
        self.setNormal()
        DATA.update({'streak_day': DATA['streak_day'] + 1, 'last_time_btn_used': int(time())})
        json.dump(DATA, open(DATA_LOCATION, 'w'))
        Condition().dayStreak()

class PotionTime(App):
    def on_start(self):
        from kivy.utils import platform
        if platform == 'android':
            self.start_service()

    def on_stop(self):
        Main().updater.cancel()
        
    def build(self):
        self.title = "Potion TIME!"
        self.icon = "assets/img/icon/icon.png"
        Builder.load_file('main.kv')
        return Manager()
    
    @staticmethod
    def start_service():
        from jnius import autoclass
        service = autoclass("org.yamfinzz.potiontime.ServicePotiontime")
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        service.start(mActivity, "")
        return service

PotionTime().run()