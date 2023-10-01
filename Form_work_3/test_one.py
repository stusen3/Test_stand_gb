import time

from testpage import OperationHelper
username = "dima11"
password = "b90ab7e1b5"
name = "Dimon"
email = "134679@bk.ru"
content = "Welcome back, Mitya!"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("dima11")
    test_page1.enter_pswd("b90ab7e1b5")
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_name("Dimon")
    test_page1.enter_email("134679@bk.ru")
    test_page1.enter_content("Welcome back, Mitya!")
    test_page1.click_button_contact()
    time.sleep(3)

    alert_text = 'Form successfully submitted'
    text = test_page1.get_alert_text()
    assert text == alert_text