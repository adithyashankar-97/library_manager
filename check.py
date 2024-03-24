from models import Activity
import random
import string 
from datetime import datetime

class CheckInOutManager:
    """
    Manages the checking in and out of books within the library system.

    Attributes:
        book_manager (BookManager): The book manager with which this class interacts.
        user_manager (UserManager): The user manager with which this class interacts.
    """

    def __init__(self, book_manager, user_manager):
        """
        Initializes the CheckInOutManager with a book manager and a user manager.

        Args:
            book_manager (BookManager): The book manager of the system.
            user_manager (UserManager): The user manager of the system.
        """
        self.book_manager = book_manager
        self.user_manager = user_manager

    def check_out_book(self, isbn, user_id):
        """
        Checks out a book for a user if available.

        Args:
            isbn (str): The ISBN of the book to check out.
            user_id (str): The ID of the user checking out the book.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        # Retrieve the book and user objects
        book = next((book for book in self.book_manager.books if book.isbn == isbn), None)
        user = next((user for user in self.user_manager.users if user.user_id == user_id), None)

        # Validate book and user
        if book is None or user is None:
            print("Invalid book ISBN or user ID.")
            return False

        # Check if there are available copies to check out
        if book.available_copies < 1:
            print("No available copies of this book to check out.")
            return False

        # Process the check-out
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
        """
        Checks in a book for a user.

        Args:
            isbn (str): The ISBN of the book to check in.
            user_id (str): The ID of the user checking in the book.

        Returns:
            bool: True if the book was successfully checked in, False otherwise.
        """
        # Retrieve the book and user objects
        book = next((book for book in self.book_manager.books if book.isbn == isbn), None)
        user = next((user for user in self.user_manager.users if user.user_id == user_id), None)

        # Validate book and user
        if book is None or user is None:
            print("Invalid book ISBN or user ID.")
            return False

        # Check if all copies are already checked in
        if book.available_copies >= book.total_copies:
            print("All copies are already checked in.")
            return False

        # Process the check-in
        book.available_copies += 1
        if isbn not in user.checked_out:
            print(f"User: {user_id} has not checked out this book with ISBN: {isbn}")
            return False

        user.checked_out.remove(isbn)
        for act in user.activity:
            if act['isbn'] == isbn and act['check_in_date'] is None:
                act['check_in_date'] = datetime.now().strftime('%Y-%m-%d')
                act['fine'] = get_fine(act, book)

        print(f"Book '{book.title}' has been successfully checked in.")
        self.book_manager.save_books()
        self.user_manager.save_users()
        return True

def get_fine(act, book):
    """
    Calculates the fine for a checked-in book based on the due date and check-in date.

    Args:
        act (dict): The activity dictionary containing check-in and due date information.
        book (Book): The book object to calculate the fine for.

    Returns:
        int: The calculated fine amount.
    """
    return max(0, (datetime.strptime(act['check_in_date'],'%Y-%m-%d') - datetime.strptime(act['due_date'],'%Y-%m-%d')).days*book.per_day_fine)