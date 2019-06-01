from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep  

import sys

username=''
password = ''

driver = webdriver.Chrome()
driver.get("https://github.com/")
driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="login"]/form/div[3]/input[4]').click()
driver.find_element(By.XPATH, '/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a').click()
driver.find_element(By.XPATH, '//*[@id="repository_name"]').send_keys(sys.argv[1])
sleep(1)
driver.find_element(By.XPATH, '//*[@id="new_repository"]/div[3]/button').click()
driver.quit()









