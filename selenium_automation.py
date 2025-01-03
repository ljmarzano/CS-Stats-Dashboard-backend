from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_report(email, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo sin cabeza
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Usa el servicio con ChromeDriver
    service = Service("chromedriver")  # ChromeDriver ya está en el PATH

    driver = webdriver.Chrome(service=service, options=options)
    try:
        print("Navegando al formulario de inicio de sesión...")
        driver.get("https://backoffice.rayapp.io/login")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        print("Formulario cargado correctamente")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        print("Esperando redirección al dashboard...")
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        print("Redirigido al dashboard correctamente")
    except Exception as e:
        print(f"Error en la automatización: {e}")
    finally:
        driver.quit()
