from book import BookManager
from user import UserManager
from check import CheckInOutManager

def main_menu():
    print("\n--- Library Management System ---")
    print("1: Manage Books")
    print("2: Manage Users")
    print("3: Check Out Book")
    print("4: Check In Book")
    print("5: Exit")
    choice = input("Select an option: ")
    return choice

def manage_books(book_manager):
    while True:
        print("\n--- Manage Books ---")
        print("1: Add Book")
        print("2: Update Book")
        print("3: Delete Book")
        print("4: Search Books")
        print("5: List All Books")
        print("6: Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            total_copies = int(input("Enter total number of copies: "))
            book_manager.add_book(title, author, isbn, total_copies)
            print("Book added successfully.")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank for no change): ")
            author = input("Enter new author (leave blank for no change): ")
            total_copies = input("Enter new total copies (leave blank for no change): ")
            total_copies = int(total_copies) if total_copies.isdigit() else None
            book_manager.update_book(isbn, title, author, total_copies)
            print("Book updated successfully.")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            print("Book deleted successfully.")
        elif choice == '4':
            isbn = input("Enter ISBN to search (leave blank for no search): ")
            title = input("Enter title to search (leave blank for no search): ")
            author = input("Enter author to search (leave blank for no search): ")
            results = book_manager.search_books(isbn, title, author)
            print("Search results:")
            for book in results:
                print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Total Copies: {book.total_copies}, Checked Out: {book.checked_out}")
        elif choice == '5':
            books = book_manager.list_books()
            print("List of all books:")
            for book in books:
                print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Total Copies: {book.total_copies}, Checked Out: {book.checked_out}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def manage_users(user_manager):
    while True:
        print("\n--- Manage Users ---")
        print("1: Add User")
        print("2: Update User")
        print("3: Delete User")
        print("4: Search Users")
        print("5: List All Users")
        print("6: Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_manager.add_user(user_id, name)
            print("User added successfully.")
        elif choice == '2':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name: ")
            if user_manager.update_user(user_id, name):
                print("User updated successfully.")
            else:
                print("User not found.")
        elif choice == '3':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
            print("User deleted successfully.")
        elif choice == '4':
            print("Please Enter the user ID or the name to search or both as queried below")
            uid = input("Enter user ID: ")
            name = input("Enter the name: ")
            if uid == "" and name == "":
                print("Warning Empty query, no name or no user ID entered")
            results = user_manager.search_users(user_id=uid, name=name)
            if results:
                print("Search results:")
                for user in results:
                    print(f"User ID: {user.user_id}, Name: {user.name}")
            else:
                print("No users found matching the criteria.")
        elif choice == '5':
            print("List of all users:")
            for user in user_manager.users:
                print(f"User ID: {user.user_id}, Name: {user.name}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    book_manager = BookManager()
    user_manager = UserManager()
    check_in_out_manager = CheckInOutManager(book_manager, user_manager)

    while True:
        choice = main_menu()
        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            isbn = input("Enter the ISBN of the book to check out: ")
            user_id = input("Enter the user ID: ")
            check_in_out_manager.check_out_book(isbn, user_id)
        elif choice == '4':
            isbn = input("Enter the ISBN of the book to check in: ")
            check_in_out_manager.check_in_book(isbn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
