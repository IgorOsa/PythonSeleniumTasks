import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text

    result = calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    checkbox = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    checkbox.click()

    selectbox = browser.find_element_by_css_selector('label[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", selectbox)
    selectbox.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
