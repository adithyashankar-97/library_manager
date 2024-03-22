from storage import Storage
from models import Book

class BookManager:
    def __init__(self):
        self.storage = Storage('books.json')
        self.books = self.load_books()

    def load_books(self):
        data = self.storage.read_data()
        return [Book(**book_data) for book_data in data]

    def save_books(self):
        self.storage.write_data([book.__dict__ for book in self.books])

    def add_book(self, title, author, isbn, total_copies):
        new_book = Book(title, author, isbn, total_copies, total_copies)
        self.books.append(new_book)
        self.save_books()

    def update_book(self, isbn, title=None, author=None):
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
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def search_books(self, title=None, author=None, isbn=None):
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if isbn:
            results = [book for book in results if isbn == book.isbn]
        return results
