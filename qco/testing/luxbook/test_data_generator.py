import json


def read_test_data_as_json(file_name):
    data = []
    with open(file_name, 'r') as data_file:
        data = json.loads(data_file.read())
    print(file_name + " loaded")
    return data['messages']

