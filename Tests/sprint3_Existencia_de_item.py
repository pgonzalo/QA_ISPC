import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-loggin'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.get("https://deliverind.com.ar")
driver.maximize_window()
time.sleep(2)

#click en la seccion Drop Deliverind

dropDeliver = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section[1]/div/div/div/div/div/div[2]/div/div/a/img")

time.sleep(2)

dropDeliver.click()

time.sleep(2)

#Validamos que se encuentre un item determinado dentro de la seccion Drop deliverlind


itemNameRequired = ()
itemNameObtained = ()

def compareCant():
    if itemNameRequired in itemNameObtained:
        print("PASS")
    else:
        print("FAIL")

itemExists = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/ul/li/div/div[2]/h2").text
print('itemName: ' + itemExists)
itemNameObtained = itemExists

itemNameRequired= 'Hoodie Dark Club'

compareCant()

time.sleep(4)

driver.close()
compareCant()

time.sleep(4)

driver.close()