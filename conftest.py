import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.amazon.com/")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless=new")

    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield drv
    drv.quit()
