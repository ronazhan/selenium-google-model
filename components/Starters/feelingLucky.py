from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("drivers/chromedriver")

driver.get("https://www.google.com")
element = WebDriverWait(driver, 20) \
    .until(EC.visibility_of_any_elements_located((By. CSS_SELECTOR, '[name="btnI"][type="submit"]')))[0]
element.click()
time.sleep(10)

driver.close()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome("drivers/chromedriver")
# driver.get("https://www.google.com/")
#
# luckyButton = driver.find_element_by_xpath("//input[@name='btnI']")
# time.sleep(1)
# luckyButton.submit()
# luckyButton.submit()
# time.sleep(10)
#
#
# driver.close()