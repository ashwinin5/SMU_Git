from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserModule():


    global driver
    driver = webdriver.Firefox()

    def login():
        host = "https://10.1.25.133/v3/index.html"
        username = "manage"
        password = "!manage"

        driver.get(host)
        sleep(5)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginButton").click()

    def create_vdisk():
        sleep(8)
        driver.find_element(By.ID, "MtopicsIvolumes").click()
        sleep(4)
        driver.find_element(By.CSS_SELECTOR, "div.topicAction.buttonPrimary").click()
        sleep(3)
        driver.find_element(By.ID, "MVolumesTopicIcreateLinearVolumes").click()
        sleep(3)
        #driver.find_element(By.CLASS_NAME, "comboList").click()
        driver.find_element(By.ID, "volNum").clear()
        driver.find_element(By.ID, "volNum").send_keys("1")
        driver.find_element(By.ID, "name").clear()
        driver.find_element(By.ID, "name").send_keys("Vol001")
        driver.find_element(By.ID, "volSize").clear()
        driver.find_element(By.ID, "volSize").send_keys("200GB")
        sleep(4)
        #driver.find_element(By.CSS_SELECTOR, "div.buttonLarge.buttonHoriz.buttonPrimary").click()
        driver.find_element(By.XPATH, ".//*[@id='actionDialog']/div/div[2]/div/div/div[1]").click()
        sleep(3)
        driver.find_element(By.ID, "adp_ok").click()


    def logout():

        driver.find_element(By.ID, "logoutButton").click()
        driver.find_element(By.ID, "adp_ok").click()
   

    login()
    create_vdisk()
    logout()
        

    

        


    
