from storage import Storage
from models import Activity_Logger

class Logger:
    def __init__(self):
        self.storage = Storage('logs.json')
        self.logs = self.load_logs()
    
    def load_logs(self):
        data = self.storage.read_data()
        return [Activity_Logger(**log_data) for log_data in data]
    
    def save_logs(self):
        self.storage.write_data([log.__dict__ for log in self.logs])