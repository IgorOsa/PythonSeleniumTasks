import time
from selenium import webdriver

# initialize the browser driver. 
# this command open a new browser window
driver = webdriver.Chrome()

# the time.sleep command sets a pause of 5 seconds 
# so that we can see what is happening in the browser
time.sleep(5)

# The get method tells the browser to open the site using the specified link.
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# The find_element_by_css_selector method allows you to find the desired item on the site 
# by specifying the path to it. We'll discuss ways to find items later.
# Searching for a text input field
textarea = driver.find_element_by_css_selector(".textarea")

# write response into text found field
textarea.send_keys("get()")
time.sleep(5)

# Find the button that sends solution
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Let's tell the driver that you need to click on the button. 
# After this command we should see a message about the correct answer
submit_button.click()
time.sleep(5)

# After completing all the steps, we must not forget to close the browser window
driver.quit()
