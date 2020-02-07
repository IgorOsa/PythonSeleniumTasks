import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.execute_script(
        "document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(10)
    browser.quit()
