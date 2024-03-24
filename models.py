from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies, max_loan_period=14, per_day_fine=10):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.max_loan_period = max_loan_period
        self.per_day_fine = per_day_fine

class Activity:
    def __init__(self, act_id, isbn, check_out_date, check_in_date=None, max_loan_period = 14, fine=None):
        self.act_id = act_id
        self.check_out_date = check_out_date
        self.due_date = (self.check_out_date + timedelta(days=max_loan_period)).strftime('%Y-%m-%d')
        self.check_out_date = (self.check_out_date).strftime('%Y-%m-%d')
        self.isbn = isbn
        self.check_in_date = None
        self.fine = None

    def return_act(self):
        # self.due_date = self.due_
        self.return_date = datetime.today()
        self.fine = max(0, (self.return_date - self.due_date).days*self.per_day_fine)
        

class User:
    def __init__(self, user_id, name, checked_out = [], activity = []):
        self.user_id = user_id
        self.name = name
        self.checked_out = checked_out
        self.activity = activity
    
    def update_activity(self, activity):
        # find activity if exists, by id and update or by isbn 
        pass

# if __name__ == '__main__':
#     act = Activity('aksjdn', 123)
#     print(act.__dict__)
#     act.return_act()
#     print(act.__dict__)