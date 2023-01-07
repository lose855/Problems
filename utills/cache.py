import pickle
import os
import datetime

class Scheduler:
            
    def __init__(self):
        self.memory = []
        self.next_plan = None
    
    def add(self, date_info, content_info):
        date = datetime.datetime(year = date_info['year'],
            month = date_info['month'],
            day = date_info['day'],
            hour = date_info['hour'],
            minute = date_info['minute'],)
        self.memory.append((date, content_info))
        self.sort()
        self.next()

    def __call__(self): # Return remain plans
        return len(self.memory)
    
    def sort(self):
        self.memory.sort(key=lambda data: data[0])
    
    def next(self):
        self.next_plan = self.memory[0][0]
    
    def update(self): # Clean memory
        now = datetime.datetime.now()
        if now >= self.next_plan:
            del self.memory[0]
            self.sort()
            self.next()

class Cache:
    def __init__(self, addr):
        self.addr = addr
        self.scheduler = Scheduler()
        if os.path.isfile(self.addr):
            with open(self.addr,'rb') as file:
                self.scheduler = pickle.load(file)
    
    def __call__(self):
        return self.scheduler
    
    def save(self):
        with open(self.addr, 'wb') as file:
            pickle.dump(self.scheduler, file)