import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Program Files (x86)"
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options= options)

driver.get("https://www.globalsqa.com/demoSite/practice/progressbar/download.html")
driver.implicitly_wait(30)                       # this is to fix element not interactable issues
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()

"""progress_element = driver.find_element(By.CLASS_NAME, "progress-label")
print(f"{progress_element.text == 'Complete!'}")"""

# explicit wait exemple
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"), # Element filtrartion
        'Complete!'                        # The expected text
    )
)