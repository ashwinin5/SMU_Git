from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# switching tabs



driver = webdriver.Firefox()

host = "http://10.1.25.133/v3/index.html"
username = "manage"
password = "!manage"
driver.get(host)
sleep(5)
# Logging into the application
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "loginButton").click()
sleep(8)
driver.find_element(By.ID, "MtopicsIsystem").click()
sleep(4)
driver.find_element(By.ID, "MtopicsIvolumes").click()
sleep(4)
driver.find_element(By.ID, "MtopicsIhosts").click()
sleep(4)
#driver.find_element(By.ID, "adp_ok").click()
driver.find_element(By.ID, "logoutButton").click()
driver.find_element(By.ID, "adp_ok").click()
driver.close()


# script executed
