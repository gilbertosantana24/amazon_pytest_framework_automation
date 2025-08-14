from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, condition, timeout=15):
    return WebDriverWait(driver, timeout).until(condition)

def is_element_displayed(driver, locator, timeout=15):
    # locator: (By.ID, "ap_email")
    return wait_for_element(driver, EC.visibility_of_element_located(locator), timeout)

def is_clickable(driver, locator, timeout=15):
    return wait_for_element(driver, EC.element_to_be_clickable(locator), timeout)
