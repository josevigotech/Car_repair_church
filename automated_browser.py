from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Configura el navegador (asegúrate de tener ChromeDriver o el controlador correspondiente)
driver = webdriver.Chrome(executable_path="C:/ruta/a/tu/chromedriver.exe")  # Cambia la ruta al chromedriver

# Abre la página web
driver.get("http://127.0.0.1:5000/")

# Espera explícita para asegurarse de que la página cargue correctamente
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))

# Completar el formulario
driver.find_element(By.ID, "name").send_keys("Juan Pérez")
driver.find_element(By.ID, "phone").send_keys("123456789")
driver.find_element(By.ID, "email").send_keys("juan.perez@example.com")

# Si el campo de género es un <select> (desplegable)
gender_select = Select(driver.find_element(By.ID, "gender"))
gender_select.select_by_visible_text("Masculino")

driver.find_element(By.ID, "problem").send_keys("Cambio de aceite")
driver.find_element(By.ID, "car_brand").send_keys("Toyota")
driver.find_element(By.ID, "car_model").send_keys("Corolla")
driver.find_element(By.ID, "car_year").send_keys("2020")

# Selecciona la casilla de oración si es necesario
driver.find_element(By.ID, "prayer_request").click()

# Enviar el formulario (si el formulario tiene un botón de envío)
driver.find_element(By.XPATH, "//form").submit()

# Espera unos segundos para ver el resultado
time.sleep(3)

# Cierra el navegador
driver.quit()
