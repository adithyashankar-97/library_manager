from storage import Storage
from models import Book

class BookManager:
    """
    Manages book-related operations within the library system.

    Attributes:
        storage (Storage): An instance of the Storage class to handle data persistence.
        books (list): A list of Book objects representing all books managed by the system.
    """

    def __init__(self):
        self.storage = Storage('books.json')
        self.books = self.load_books()

    def load_books(self):
        """
        Loads book data from the storage and creates Book instances for each.

        Returns:
            list: A list of Book instances loaded from the storage file.
        """
        data = self.storage.read_data()
        return [Book(**book_data) for book_data in data]

    def save_books(self):
        """
        Saves the current state of books back to the storage.
        """
        self.storage.write_data([book.__dict__ for book in self.books])

    def add_book(self, title, author, isbn, total_copies):
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            total_copies (int): The total number of copies of the book.
        """
        new_book = Book(title, author, isbn, total_copies, total_copies)
        self.books.append(new_book)
        self.save_books()

    def update_book(self, isbn, title=None, author=None):
        """
        Updates the details of an existing book.

        Args:
            isbn (str): The ISBN of the book to update.
            title (str, optional): The new title of the book.
            author (str, optional): The new author of the book.

        Returns:
            bool: True if the book was updated successfully, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                return True
        return False

    def delete_book(self, isbn):
        """
        Deletes a book from the library.

        Args:
            isbn (str): The ISBN of the book to delete.
        """
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def search_books(self, title=None, author=None, isbn=None):
        """
        Searches for books by title, author, or ISBN.

        Args:
            title (str, optional): The title to search for.
            author (str, optional): The author to search for.
            isbn (str, optional): The ISBN to search for.

        Returns:
            list: A list of Book instances that match the search criteria.
        """
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if isbn:
            results = [book for book in results if isbn == book.isbn]
        return results
