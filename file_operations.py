import json

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
