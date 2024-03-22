class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies


class User:
    def __init__(self, user_id, name, checked_out = []):
        self.user_id = user_id
        self.name = name
        self.checked_out = []