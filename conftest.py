# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from steps.login_steps import LoginSteps

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.amazon.com/")

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless=new")  # opcional

    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield drv
    drv.quit()

@pytest.fixture(scope="session", autouse=True)
def login_once(driver, base_url):
    """
    Se ejecuta automáticamente antes del primer test.
    - Abre Amazon
    - Verifica si ya está logueado
    - Si no, hace login usando tus Steps (AMAZON_EMAIL / AMAZON_PASSWORD)
    """
    email = os.getenv("AMAZON_EMAIL")
    password = os.getenv("AMAZON_PASSWORD")
    if not email or not password:
        raise RuntimeError("Define AMAZON_EMAIL y AMAZON_PASSWORD en variables de entorno.")

    driver.get(base_url)
    wait = WebDriverWait(driver, 20)

    def needs_login() -> bool:
        try:
            # En Amazon, este ID muestra "Hello, sign in" si NO estás logueado
            text = wait.until(
                EC.visibility_of_element_located((By.ID, "nav-link-accountList-nav-line-1"))
            ).text.strip().lower()
            return "sign in" in text or "identifícate" in text or "inicia sesión" in text
        except TimeoutException:
            # Si no aparece, intentamos loguear por si acaso
            return True

    if needs_login():
        steps = LoginSteps(driver, base_url)
        steps.open_home_and_open_sign_in()
        steps.enter_email_and_continue()
        steps.enter_password_and_click_sign_in()

    # Opcional: vuelve a Home para arrancar los tests en estado conocido
    driver.get(base_url)
