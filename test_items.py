import time

from selenium.webdriver.common.by import By


LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(LINK)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Кнопка не найдена"



