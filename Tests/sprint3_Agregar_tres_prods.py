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

driver = webdriver.Chrome()
driver.get("https://deliverind.com.ar")
driver.maximize_window()

time.sleep(2)

#login

# userIcon= driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[2]/i")
# userIcon.click()
# time.sleep(2)

# userName= driver.find_element(By.ID, "username")
# password= driver.find_element(By.ID, "password")
# accederButton= driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[3]/button")

# userName.send_keys('pintadogonzalo')
# password.send_keys('ha9Qe9Nj8z.M3Lv')
# accederButton.click()
# time.sleep(5)


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

searchButton = driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div[2]/form/label/button/i")

time.sleep(2)

searchButton.click()

time.sleep(2)

talle1Opciones = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/ul/li[1]")

time.sleep(2)

talle1Opciones.click()

color1Opciones = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/ul/li[14]/div")

time.sleep(2)

color1Opciones.click()

talle2Opciones = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/ul/li[1]/div")

time.sleep(2)

talle2Opciones.click()

color2Opciones = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/ul/li[14]/div")

time.sleep(2)

color2Opciones.click()

time.sleep(2)

cantInput = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form/div/input")

time.sleep(2)

cantInput.clear()

time.sleep(2)

cantInput.send_keys("3")

time.sleep(2)

addToCartButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form")

time.sleep(2)

addToCartButton.click()

time.sleep(4)

cerrarCarritoButton = driver.find_element(By.XPATH, "/html/body/div[4]/div/span")

time.sleep(2)


cerrarCarritoButton.click()


#Validamos que se encuentren 3 productos agregados en el carrito de compras

cantProdsRequired = ()
cantProdsObtained = ()

def compareCant():
    if cantProdsRequired in cantProdsObtained:
        print("PASS")
    else:
        print("FAIL")

cantProds = driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[3]/span").get_attribute('value')
print('cantProds: ' + cantProds)
cantProdsObtained = cantProds

cantProdsRequired= '3'

compareCant()

time.sleep(4)

driver.close()
