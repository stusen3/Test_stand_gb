import pytest
import requests
import yaml

with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = my_dict['username']
password = my_dict['password']


@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data ={'username':username, 'password':password})
    token = obj_data.json()['token']
    return token

#login()