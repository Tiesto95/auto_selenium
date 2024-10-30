from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

driver.maximize_window()
name_v = driver.find_element(By.ID, 'user-name')
name_v.send_keys('standard_user')
time.sleep(10)
driver.close()


