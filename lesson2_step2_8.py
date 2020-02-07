import os
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element_by_css_selector("input[name='firstname']")
    first_name.send_keys("Igor")

    last_name = browser.find_element_by_css_selector("input[name='lastname']")
    last_name.send_keys("Webio")

    email_field = browser.find_element_by_css_selector("input[name='email']")
    email_field.send_keys("igor@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    file_field = browser.find_element_by_css_selector("[type='file']")
    file_field.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
