from storage import Storage
from models import User

class UserManager:
    def __init__(self):
        self.storage = Storage('users.json')
        self.users = self.load_users()

    def load_users(self):
        data = self.storage.read_data()
        return [User(**user_data) for user_data in data]

    def save_users(self):
        self.storage.write_data([user.__dict__ for user in self.users])

    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        self.save_users()

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.save_users()
                return True
        return False

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users()

    def search_users(self, user_id=None, name=None):
        print("Searching for user ID: {} and name: {}".format(user_id, name))
        results = self.users
        if user_id:
            results = [user for user in results if user_id == user.user_id]
        if name:
            results = [user for user in results if name.lower() in user.name.lower()]
        return results
