import json

TIME_LIMIT_LOCATION: str = 'assets/data/time_limit.json'

class timeCalc():
    def __init__(self, hour: int, min: int) -> None:    
        self.TIME_LIMIT: dict = json.load(open(TIME_LIMIT_LOCATION, "r"))
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
        else: 
            self.TIME_LIMIT['0'].update({'0': self.time[0], '1': self.time[1] - 15})
    
    def max_time(self) -> None:
        if self.time[1]+15 >= 60:
            self.max_t[0] = self.time[0]+1
            if self.max_t[0] >= 24:
                self.max_t[0] = self.max_t[0]-24
            self.max_t[1] = self.time[1]-45
            self.TIME_LIMIT['1'].update({'0': self.max_t[0], '1': self.max_t[1]})
            del self.max_t
        else: 
            self.TIME_LIMIT['1'].update({'0': self.time[0], '1': self.time[1] + 15})