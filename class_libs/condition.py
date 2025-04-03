from time import localtime, time
from timecalc import *
import json


DATA_LOCATION: str = '../assets/data/data.json'


def loadData(func):
    def wrapper(*args):
        global DATA
        DATA = json.load(open(DATA_LOCATION, "r"))
        func(args)
    return wrapper


class Condition():
    def timeCon(self, Condition: int) -> bool:
        self.TIME_LIMIT: dict = json.load(open(TIME_LIMIT_LOCATION, "r"))
        self.min_hour: int = self.TIME_LIMIT['0']['0']
        self.max_hour: int = self.TIME_LIMIT['1']['0']
        self.data_hour: int = json.load(open(DATA_LOCATION, "r"))['set_hour']

        def checkHour() -> bool:
            match Condition:
                case 1: return (localtime().tm_hour == self.min_hour == self.data_hour == self.max_hour)
                case 2: return (self.min_hour == self.data_hour != self.max_hour) or (self.min_hour != self.data_hour == self.max_hour)
    
        def checkMin() -> bool:
            match Condition:
                case 1: return self.TIME_LIMIT['0']['1'] <= localtime().tm_min < self.TIME_LIMIT['1']['1']
                case 2: return ((localtime().tm_hour == self.min_hour and localtime().tm_min >= self.TIME_LIMIT['0']['1']) or
                                (localtime().tm_hour == self.max_hour and localtime().tm_min < self.TIME_LIMIT['1']['1']))
       
        return (checkHour() and checkMin())
    
        
    def dayStreak(self) -> None:
        if DATA['streak_day'] == 28: 
            DATA.update({'streak_day': DATA['streak_day'] - 28, 'streak_month': DATA['streak_month'] + 1})
            json.dump(DATA, open(DATA_LOCATION, 'w'))


    def isTimeSet(self) -> bool:
        if (DATA['set_hour'] != None) and (DATA['set_min'] != None):
            timeCalc(DATA['set_hour'], DATA['set_min'])
            return True
        else:
            return False
    

    def isTimeButtonReady(self) -> bool:
        return (int(time()) - DATA['last_time_btn_used']) > 1800 #30 Min


    def isMessageReady(self) -> bool:
        return (int(time()) - DATA['last_time_msg_sent']) > 300


    @loadData 
    def serviceMessageCondition(self) -> bool:
        Is_Time_Set_Condition = self.isTimeSet()
        Is_Ready_Condition = self.isTimeButtonReady() and self.isMessageReady() 
        Time_Condition = self.timeCon(1) or self.timeCon(2)
        
        MessageReady = Is_Time_Set_Condition and Is_Ready_Condition and Time_Condition
        
        return MessageReady