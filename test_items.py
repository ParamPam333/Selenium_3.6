import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(1)
    btn=browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert len(btn)>0, 'Элемент не найден'