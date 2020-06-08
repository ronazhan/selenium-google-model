from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# initialize webpage
driver = webdriver.Chrome("../drivers/chromedriver")
driver.get("http://automationpractice.com/")

# Go to login page
signButton = driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/nav/div[1]/a")
signButton.click()

# Fill in user information
emailField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
emailField.send_keys("nonsense@gmail.com")
pswdField = driver.find_element_by_xpath("//*[@id=\"passwd\"]")
pswdField.send_keys("asdfasdf" + Keys.ENTER)

# Return to home page
driver.find_element_by_xpath("//*[@id=\"header_logo\"]/a/img").click()

# Open dress categories
driver.find_element_by_xpath("//*[@id=\"block_top_menu\"]/ul/li[2]/a").click()

# Add first dress
# driver.find_element_by_xpath("//*[@id=\"homefeatured\"]/li[1]/div/div[2]/div[2]/a[1]/span").click()
# # driver.find_element_by_xpath("//*[@id=\"homefeatured\"]/li[1]/div/div[2]/div[2]/a[1]")

time.sleep(10)
dresses = driver.find_elements_by_class_name('button ajax_add_to_cart_button btn btn-default')
print(dresses)

# Go to cart
# driver.find_element_by_xpath("//*[@id=\"layer_cart\"]")

time.sleep(10)
driver.close()