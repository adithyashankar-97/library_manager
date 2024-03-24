# Library Management System

This Library Management System is a simple yet flexible solution for managing a library's books and users. It supports operations such as adding, updating, deleting, and searching for books and users, as well as checking books in and out.

## Features

- Manage books:
  - Add, update, delete, and search books in the library.
  - Track the number of available copies for each book.
  - Check out and check in books with user tracking.
- Manage users:
  - Add, update, delete, and search for users.
  - Track user activity and checked-out books.
- Activity logging:
  - Record each check-out and check-in activity.
  - Calculate fines for late returns based on a predefined daily rate.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory and run `python main.py` to start the system.

## Usage

The system is accessed through a command-line interface (CLI). Follow the on-screen prompts to interact with the system:

1. **Manage Books**: Select this option from the main menu to add, update, delete, or search for books. You can also view a list of all books in the library.
2. **Manage Users**: Choose this option to add, update, delete, or search for users. You can also view a list of all registered users.
3. **Check Out Book**: This option allows you to check out a book to a user. You will need the book's ISBN and the user's ID.
4. **Check In Book**: Use this option to check in a book. You'll need the book's ISBN and the user's ID.

## File Structure

- `main.py`: The entry point of the application.
- `book.py`: Contains the `BookManager` class for managing book-related operations.
- `user.py`: Contains the `UserManager` class for managing user-related operations.
- `check.py`: Contains the `CheckInOutManager` class for handling book check-outs and check-ins.
- `models.py`: Defines the data models (`Book`, `User`, and `Activity`) used in the system.
- `storage.py`: Manages file-based storage and retrieval of data.

## Data Storage

The system uses JSON files (`books.json` and `users.json`) for data storage. This choice simplifies the architecture and allows for easy human-readable data inspection and manual editing if necessary.