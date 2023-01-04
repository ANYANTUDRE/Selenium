import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Program Files (x86)"
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options= options)
driver.get("https://syntaxprojects.com/basic-first-form-demo.php")

driver.implicitly_wait(5)

# if we meet an ad we can skip it by this wait:
try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except:
    print('No elements with this class name. Skipping.....')


sum1 = driver.find_element(By.ID, "sum1")
sum2 = driver.find_element(By.ID, "sum2")
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

bto = driver.find_element(By.CSS_SELECTOR, value='button[onclick="return total()"]')