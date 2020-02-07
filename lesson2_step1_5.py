import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    checkbox_field = browser.find_element_by_id("robotCheckbox")
    checkbox_field.click()

    radiobutton_field = browser.find_element_by_id("robotsRule")
    radiobutton_field.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
