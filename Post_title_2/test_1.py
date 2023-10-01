import yaml
import time
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, btn_selector, btn_add_selector, title_input_selector, btn_save_selector,
               post_title_selector):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(testdata["login"])

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(testdata["password"])

    btn = site.find_element("xpath", btn_selector)
    btn.click()
    time.sleep(testdata["sleep_time"])

    btn_add = site.find_element("xpath", btn_add_selector)
    btn_add.click()
    time.sleep(testdata["sleep_time"])

    time_stamp = time.time()
    title_text = f'Мой новый тестовый пост {time_stamp}'
    title_input = site.find_element("xpath", title_input_selector)
    btn_save = site.find_element("xpath", btn_save_selector)

    title_input.send_keys(title_text)
    btn_save.click()
    time.sleep(testdata["sleep_time"])

    post_title = site.find_element("xpath", post_title_selector)

    assert post_title.text == title_text

    # x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    # err_label = site.find_element("xpath", x_selector3)
    # assert err_label.text == "401"