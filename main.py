from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivy.lang import Builder

from time import localtime, time
import json

TITLE: str = "Potion TIME!"
ICON, ICON_MSG = ['assets/img/icon/icon.png', 'assets/img/icon/icon.ico']
BG_MAIN, BG_MAIN_ON_TIME = ['assets/img/bg/bg.png', 'assets/img/bg/bg_ontime.png']
BG_HOME_UNREADY, BG_HOME_READY = ['assets/img/bg/bg_home_unready.png', 'assets/img/bg/bg_home_ready.png']
THARMAR_BLACK: str = '#181818'
DATA_LOCATION: str = 'assets/data/data.json'
DATA: dict = json.load(open(DATA_LOCATION, "r"))

try:
    TIME_LIMIT: list[tuple] = [(DATA['set_hour'], DATA['set_min']-15), (DATA['set_hour'], DATA['set_min']+15)]
    isTimeSet: bool = True
except TypeError:
    TIME_LIMIT: list[tuple] = [(None, None), (None, None)]
    isTimeSet: bool = False

class timeCalc():
    def __init__(self, hour: int, min: int) -> None:
        self.min_t, self.max_t = [[None, None], [None, None]]
        self.time = [hour, min]
        self.min_time()
        self.max_time()
        del self.time       
    def min_time(self) -> None:
        if self.time[1]-15 < 0:
            self.min_t[0] = self.time[0]-1
            if self.min_t[0] < 0:
                self.min_t[0] = self.min_t[0]+24
            self.min_t[1] = self.time[1]+45
            TIME_LIMIT[0] = (self.min_t[0], self.min_t[1])
            del self.min_t
    def max_time(self) -> None:
        if self.time[1]+15 >= 60:
            self.max_t[0] = self.time[0]+1
            if self.max_t[0] >= 24:
                self.max_t[0] = self.max_t[0]-24
            self.max_t[1] = self.time[1]-45
            TIME_LIMIT[1] = (self.max_t[0], self.max_t[1])
            del self.max_t
class Condition():
    def __init__(self) -> None:
        self.min_hour: int = TIME_LIMIT[0][0]
        self.max_hour: int = TIME_LIMIT[1][0]
        self.data_hour: int = DATA['set_hour']
    
    def timeCon(self, Condition: int) -> bool:
        self.Condition: int = Condition
    
        def checkHour() -> bool:
                match self.Condition:
                        case 1: return (localtime().tm_hour == self.min_hour == self.data_hour == self.max_hour)
                        case 2: return (self.min_hour == self.data_hour != self.max_hour) or (self.min_hour != self.data_hour == self.max_hour)
    
        def checkMin() -> bool:
                match self.Condition:
                        case 1: return TIME_LIMIT[0][1] <= localtime().tm_min < TIME_LIMIT[1][1]
                        case 2: return ((localtime().tm_hour == self.min_hour and localtime().tm_min >= TIME_LIMIT[0][1]) or
                                        (localtime().tm_hour == self.max_hour and localtime().tm_min < TIME_LIMIT[1][1]))
        return (checkHour() and checkMin())
    
    def isTimeButtonReady(self) -> bool:
        return (DATA['last_time_btn_used'] == 0) or (int(time()) - (DATA['last_time_btn_used']) > 1800) #30 Min
    
    def isMessageReady(self) -> bool:
        return (DATA['last_time_msg_sent'] == 0) or (int(time()) - (DATA['last_time_msg_sent']) > 300) #5 Min
    
    def sendMessage(self):
        DATA.update({'last_time_msg_sent': int(time())})
        json.dump(DATA, open(DATA_LOCATION, 'w'))
        from plyer import notification
        notification.notify(title = f'{TITLE}',
                            message = f'📅It\'s {DATA["streak_month"]} month and {DATA["streak_day"]} day📅\n🤍Come here and Check-in🤍',
                            app_icon = ICON_MSG
                            )
    
    def dayStreak(self):
        if DATA['streak_day'] == 28: 
            DATA.update({'streak_day': DATA['streak_day'] - 28, 'streak_month': DATA['streak_month'] + 1})
        json.dump(DATA, open(DATA_LOCATION, 'w'))

class Manager(ScreenManager):
    def __init__(self):
        super().__init__()
        self.transition = NoTransition()
        if isTimeSet:
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
        self.sender = sender
        try:
            match self.sender:
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
        TIME_LIMIT[0], TIME_LIMIT[1] = [(DATA['set_hour'], DATA['set_min']-15), (DATA['set_hour'], DATA['set_min']+15)]
        timeCalc(DATA['set_hour'], DATA['set_min'])
        global isTimeSet
        isTimeSet = True
        self.ids['Hours'].text, self.ids['Minutes'].text = ['', '']

class Main(Screen):
    time_btn_disabled = BooleanProperty()
    time_btn_transparent = ObjectProperty()

    background_main = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setNormal()
        Clock.schedule_interval(self.Check_Time, 1)

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
        Condition().dayStreak()

class PotionTime(App):
    
    def on_start(self):
        from kivy.utils import platform
        if platform == 'android':
            self.start_service()
    
    def build(self):
        self.title = TITLE
        self.icon = ICON
        Builder.load_file('main.kv')
        return Manager()
    
    @staticmethod
    def start_service():
        from jnius import autoclass
        service = autoclass(u'org.yamfinzz.potiontime.ServicePotionTime')
        mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
        service.start(mActivity, '')
        return service
        
PotionTime().run()
