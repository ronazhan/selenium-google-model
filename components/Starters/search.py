from selenium import webdriver
import time

driver = webdriver.Chrome("../drivers/chromedriver")
driver.get("https://www.google.com/")

searchBar = driver.find_element_by_xpath("//input[@name=\"q\"]")
searchBar.send_keys("Cloudera")
searchBar.submit()

results = driver.find_elements_by_class_name('r')
print(results[0].text)
# results[0].click()

time.sleep(20)
driver.close()