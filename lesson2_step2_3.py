import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("num1").text
    
    y = browser.find_element_by_id("num2").text

    result = int(x) + int(y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
