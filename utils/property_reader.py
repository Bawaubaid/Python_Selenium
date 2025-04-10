import os

class PropertyReader:
    def __init__(self, file_path):
        self.properties = {}
        abs_path = os.path.join(os.path.dirname(__file__), "..", file_path)
        with open(abs_path, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=')
                    self.properties[key.strip()] = value.strip()

    def get(self, key):
        return self.properties.get(key)