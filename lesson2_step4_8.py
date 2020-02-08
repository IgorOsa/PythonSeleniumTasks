import os
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


os.system('clear')

with Chrome() as browser:
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_css_selector("button#book")
    button.click()

    x = browser.find_element_by_css_selector("span#input_value").text
    result = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    button = browser.find_element_by_css_selector("button#solve")
    button.click()
    button.get_attribute()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
