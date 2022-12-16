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

#click en el bonton Search
searchIcon = driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[1]/i")

time.sleep(4)

searchIcon.click()

time.sleep(3)

#Completar campo con la palabra remera

searchInput = driver.find_element(By.ID, "search")

time.sleep(2)

searchInput.click()

time.sleep(2)

searchInput.send_keys("Remera Oversize Crop x 2")

time.sleep(2)

#Click en el boton buscar

searchButton = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div[2]/form/label/button/i")

time.sleep(2)

searchButton.click()

time.sleep(2)

#Validamos que se encuentre nombre Remera Oversize Crop x 2 en al menos un producto de la busqueda

nameProdsRequired = ()
nameProdsObtained = ()

def compareName():
    if nameProdsRequired in nameProdsObtained:
        print("PASS")
    else:
        print("FAIL")

nameProds = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/h1").text
print('nameProds: ' + nameProds)
nameProdsObtained = nameProds

nameProdsRequired= 'Remera Oversize Crop x 2'

compareName()

time.sleep(4)

driver.close()
