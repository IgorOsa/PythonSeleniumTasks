import os
import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.trollface")
    time.sleep(1)
    button.click()

    # current_window = browser.current_window_handle
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector("span#input_value").text
    result = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(2)
    browser.quit()
