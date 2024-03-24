import json
import os

class Storage:
    def __init__(self, file_name):
        os.makedirs('storage', exist_ok=True)
        self.file_name = file_name

    def read_data(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
