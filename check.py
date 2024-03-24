from models import Activity
import random
import string 
from datetime import datetime

class CheckInOutManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager

    def check_out_book(self, isbn, user_id):
        book = next((book for book in self.book_manager.books if book.isbn == isbn), None)
        user = next((user for user in self.user_manager.users if user.user_id == user_id), None)

        if book is None or user is None:
            print("Invalid book ISBN or user ID.")
            return False

        if book.available_copies < 1:
            print("No available copies of this book to check out.")
            return False

        book.available_copies -= 1
        act_id = ''.join(random.choice(string.ascii_letters) for i in range(6))
        activity = Activity(act_id, book.isbn, datetime.now())
        user.checked_out.append(book.isbn)
        user.activity.append(activity.__dict__)
        print(f"Book '{book.title}' checked out to user '{user.name}'.")
        self.book_manager.save_books()
        self.user_manager.save_users()
        return True

    def check_in_book(self, isbn, user_id):
        book = next((book for book in self.book_manager.books if book.isbn == isbn), None)
        user = next((user for user in self.user_manager.users if user.user_id == user_id), None)

        if book is None or user is None:
            print("Invalid book ISBN or user ID.")
            return False

        if book.available_copies >= book.total_copies:
            print("All copies are already checked in.")
            return False

        book.available_copies += 1
        print(user.__dict__)
        if isbn not in user.checked_out:
            print("User: {} has not checked out this book with ISBN: {}".format(user_id, isbn))
            return False

        user.checked_out.remove(isbn)
        for act in user.activity:
            if act['isbn'] == isbn and act['check_in_date'] is None:
                act['check_in_date'] = datetime.now().strftime('%Y-%m-%d')

        print(f"Book '{book.title}' has been successfully checked in.")
        self.book_manager.save_books()
        self.user_manager.save_users()
        return True