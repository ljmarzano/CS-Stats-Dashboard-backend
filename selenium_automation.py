from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_report():
    # Configuración del navegador en Render (cabeza sin GUI)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Iniciar ChromeDriver
    driver = webdriver.Chrome(options=options)

    try:
        # PASO 1: Iniciar sesión en el backoffice
        driver.get("https://backoffice.rayapp.io/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

        # Rellenar el formulario de inicio de sesión
        driver.find_element(By.NAME, "email").send_keys("jim@rayapp.io")
        driver.find_element(By.NAME, "password").send_keys("rayapp.io")
        driver.find_element(By.TAG_NAME, "button").click()

        # PASO 2: Navegar a métricas
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        driver.get("https://backoffice.rayapp.io/metrics")

        # Esperar hasta que el texto cambie a "Todo bien. Proceda."
        WebDriverWait(driver, 30).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(), 'Control de mision')]"), "Todo bien. Proceda.")
        )

        # PASO 3: Seleccionar empresas y fechas
        # Ajusta estos pasos según las opciones específicas de tu menú desplegable y campos de fechas
        print("Flujo completado con éxito.")
    finally:
        # Cerrar el navegador
        driver.quit()