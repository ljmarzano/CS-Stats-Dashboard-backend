from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_report():
    # Configuración del navegador en Docker
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo sin cabeza
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/google-chrome"  # Ruta al binario de Chrome en Docker

    # Configurar el servicio para ChromeDriver
    service = Service("/usr/local/bin/chromedriver")  # Ubicación en Docker

    # Iniciar ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)

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
        print("Automatización completada con éxito.")
    finally:
        # Cerrar el navegador
        driver.quit()
