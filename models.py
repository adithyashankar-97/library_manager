from datetime import datetime, timedelta

class Book:
    """
    Represents a book in the library.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book, serving as a unique identifier.
        total_copies (int): The total number of copies of the book available in the library.
        available_copies (int): The number of copies currently available for checkout.
        max_loan_period (int): The maximum number of days a book can be loaned out.
        per_day_fine (int): The fine amount charged per day after the due date.
    """
    def __init__(self, title, author, isbn, total_copies, available_copies, max_loan_period=14, per_day_fine=10):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.max_loan_period = max_loan_period
        self.per_day_fine = per_day_fine

class Activity:
    """
    Represents an activity or transaction related to a book, such as a checkout.

    Attributes:
        act_id (str): The unique identifier for the activity.
        isbn (str): The ISBN of the book involved in the activity.
        check_out_date (datetime): The date when the book was checked out.
        max_load_period (int): The maximum number of days the book can be borrowed without a fine.
        check_in_date (str): The date when the book was returned, None if not yet returned.
        fine (float): The fine amount if the book is returned late, None if not applicable or not yet calculated.
    """
    def __init__(self, act_id, isbn, check_out_date, check_in_date=None, max_loan_period = 14, fine=None):
        self.act_id = act_id
        self.check_out_date = check_out_date
        self.due_date = (self.check_out_date + timedelta(days=max_loan_period)).strftime('%Y-%m-%d')
        self.check_out_date = (self.check_out_date).strftime('%Y-%m-%d')
        self.isbn = isbn
        self.check_in_date = None
        self.fine = None        

class User:
    """
    Represents a user of the library.

    Attributes:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.
        checked_out (list): A list of book ISBNs currently checked out by the user.
        activity (list): A list of Activity instances representing the user's borrowing history.
    """
    def __init__(self, user_id, name, checked_out = [], activity = []):
        self.user_id = user_id
        self.name = name
        self.checked_out = checked_out
        self.activity = activity
    
# if __name__ == '__main__':
#     act = Activity('aksjdn', 123)
#     print(act.__dict__)
#     act.return_act()
#     print(act.__dict__)