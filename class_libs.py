import json
from time import localtime, time

DATA_LOCATION: str = 'assets/data/data.json'
TIME_LIMIT_LOCATION: str = 'assets/data/time_limit.json'

class timeCalc():
    TIME_LIMIT: dict = json.load(open(TIME_LIMIT_LOCATION, "r"))

    def __init__(self, hour: int, min: int) -> None:    
        self.min_t, self.max_t = [[None, None], [None, None]]
        self.time = [hour, min]
        self.min_time()
        self.max_time()
        json.dump(self.TIME_LIMIT, open(TIME_LIMIT_LOCATION, 'w'))
        del self.time       
    def min_time(self) -> None:
        if self.time[1]-15 < 0:
            self.min_t[0] = self.time[0]-1
            if self.min_t[0] < 0:
                self.min_t[0] = self.min_t[0]+24
            self.min_t[1] = self.time[1]+45
            self.TIME_LIMIT['0'].update({'0': self.min_t[0], '1': self.min_t[1]})
            del self.min_t
        else: self.TIME_LIMIT['0'].update({'0': self.time[0], '1': self.time[1] - 15})
    def max_time(self) -> None:
        if self.time[1]+15 >= 60:
            self.max_t[0] = self.time[0]+1
            if self.max_t[0] >= 24:
                self.max_t[0] = self.max_t[0]-24
            self.max_t[1] = self.time[1]-45
            self.TIME_LIMIT['1'].update({'0': self.max_t[0], '1': self.max_t[1]})
            del self.max_t
        else: self.TIME_LIMIT['1'].update({'0': self.time[0], '1': self.time[1] + 15})
        
class Condition():
    DATA: dict = json.load(open(DATA_LOCATION, "r"))
    TIME_LIMIT: dict = json.load(open(TIME_LIMIT_LOCATION, "r"))

    def __init__(self) -> None:
        self.min_hour: int = self.TIME_LIMIT['0']['0']
        self.max_hour: int = self.TIME_LIMIT['1']['0']
        self.data_hour: int = self.DATA['set_hour']

    def timeCon(self, Condition: int) -> bool:
        self.Condition: int = Condition
    
        def checkHour() -> bool:
                match self.Condition:
                        case 1: return (localtime().tm_hour == self.min_hour == self.data_hour == self.max_hour)
                        case 2: return (self.min_hour == self.data_hour != self.max_hour) or (self.min_hour != self.data_hour == self.max_hour)
    
        def checkMin() -> bool:
                match self.Condition:
                        case 1: return self.TIME_LIMIT['0']['1'] <= localtime().tm_min < self.TIME_LIMIT['1']['1']
                        case 2: return ((localtime().tm_hour == self.min_hour and localtime().tm_min >= self.TIME_LIMIT['0']['1']) or
                                        (localtime().tm_hour == self.max_hour and localtime().tm_min < self.TIME_LIMIT['1']['1']))
        return (checkHour() and checkMin())
    
    def isTimeButtonReady(self) -> bool:
        return (self.DATA['last_time_btn_used'] == 0) or (int(time()) - (self.DATA['last_time_btn_used']) > 1800) #30 Min
    
    def dayStreak(self) -> None:
        if self.DATA['streak_day'] == 28: 
            self.DATA.update({'streak_day': self.DATA['streak_day'] - 28, 'streak_month': self.DATA['streak_month'] + 1})
            json.dump(self.DATA, open(DATA_LOCATION, 'w'))

    def isTimeSet(self) -> bool:
        if (self.DATA['set_hour'] != None) and (self.DATA['set_min'] != None):
            timeCalc(self.DATA['set_hour'], self.DATA['set_min'])
            return True
        else: return False

    def isMessageReady(self) -> bool:
        return (self.DATA['last_time_msg_sent'] == 0) or (int(time()) - (self.DATA['last_time_msg_sent']) > 300)

    def serviceMessageCondition(self) -> bool:
        Is_Time_Set_Condition = self.isTimeSet()
        Is_Ready_Condition = self.isTimeButtonReady() and self.isMessageReady() 
        Time_Condition = self.timeCon(1) or self.timeCon(2)
        MessageReady = Is_Time_Set_Condition and Is_Ready_Condition and Time_Condition
        return MessageReady
    
class serviceSystem():
    DATA: dict = json.load(open(DATA_LOCATION, "r"))

    def __init__(self):
        if Condition().serviceMessageCondition():
            self.sendMessage()

    def sendMessage(self):
        from plyer import notification
        notification.notify(chan = 1, title = 'Potion TIME!!!', message = '🤍Time to use your Potion!🤍')
        self.DATA.update({'last_time_msg_sent': int(time())})
        json.dump(self.DATA, open(DATA_LOCATION, 'w'))
