import os
import pytest
from steps.login_steps import LoginSteps
from page_objects.login_page import LoginPage

@pytest.mark.smoke
def test_open_sign_in_page(driver, base_url):
    steps = LoginSteps(driver, base_url)
    steps.open_home_and_open_sign_in()
    steps.enter_email_and_continue()
    steps.enter_password_and_click_sign_in()

