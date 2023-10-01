# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token". Для отображения постов другого пользователя передается "owner": "notMe".

# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login

# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

import requests
import yaml
import time

with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = 'AlexeyZ1'
password = 'e23970376f'

# def login(username, password):
#     obj_data = requests.post(url=url, data ={'username':username, 'password':password})
#     #print(obj_data.json())  #
#     token = obj_data.json()['token']
#     #print(token)
#     return token

def token_auth(token):
    response=requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': "notMe"})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var

def test_step2(login):
    assert 'content' in token_auth(login)

def test_step3(login):
    time_stamp = time.time()
    description = f'Мой новый тестовый пост {time_stamp}'
    obj_data = requests.post(url=url1, headers={'X-Auth-Token': login}, data={'title': 'Тестовый тайтл', 'description': description, 'content': 'Тестовый контент'})
    response = requests.get(url=url1, headers={'X-Auth-Token': login})
    posts_data = response.json()
    for post in posts_data['data']:
        if post["description"] == description:
            return True
    return False