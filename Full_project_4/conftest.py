import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']
    username = testdata['username']
    password = testdata['password']
    url = testdata['api_address']


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login():
    obj_data = requests.post(url=url,
                             data={'username': username, 'password': password})
    token = obj_data.json()['token']
    return token


@pytest.fixture(scope="session")
def get_content(login):
    response = requests.get(url=testdata['api_url'], headers={'X-Auth-Token': login}, params={'owner': "notMe"})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var