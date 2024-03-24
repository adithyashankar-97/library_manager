from storage import Storage
from models import User

class UserManager:
    """
    Handles the operations related to user management in the library system.
    
    Attributes:
        storage (Storage): An instance of the Storage class for handling data persistence.
        users (list): A list of User objects representing all the users in the system.
    """

    def __init__(self):
        self.storage = Storage('storage/users.json')
        self.users = self.load_users()

    def load_users(self):
        """
        Loads users from the persistent storage into memory.

        Returns:
            list: A list of User objects.
        """
        data = self.storage.read_data()
        return [User(**user_data) for user_data in data]

    def save_users(self):
        """
        Saves the current list of users back to the persistent storage.
        """
        self.storage.write_data([user.__dict__ for user in self.users])

    def add_user(self, user_id, name):
        """
        Adds a new user to the system.

        Args:
            user_id (str): The unique identifier for the user.
            name (str): The name of the user.
        """
        new_user = User(user_id, name)
        self.users.append(new_user)
        self.save_users()

    def update_user(self, user_id, name=None):
        """
        Updates an existing user's details.

        Args:
            user_id (str): The user's unique identifier.
            name (str, optional): The new name of the user.

        Returns:
            bool: True if the user was found and updated, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.save_users()
                return True
        return False

    def delete_user(self, user_id):
        """
        Deletes a user from the system.

        Args:
            user_id (str): The unique identifier of the user to be deleted.
        """
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users()

    def search_users(self, user_id=None, name=None):
        """
        Searches for users by their ID or name.

        Args:
            user_id (str, optional): The user ID to search for.
            name (str, optional): The name to search for.

        Returns:
            list: A list of User objects that match the search criteria.
        """
        print("Searching for user ID: {} and name: {}".format(user_id, name))
        results = self.users
        if user_id:
            results = [user for user in results if user_id == user.user_id]
        if name:
            results = [user for user in results if name.lower() in user.name.lower()]
        return results
