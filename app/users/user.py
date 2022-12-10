class User:
    def __init__(self, name):
        self.name = name
        self.awaited_tasks = []
        self.received_answers = []
        self.is_admin = False
    
    def check_time(self):
        return self.awaited_tasks == self.received_answers
    
    