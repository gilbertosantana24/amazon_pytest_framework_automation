import os
from time import sleep
from page_objects.login_page import LoginPage

class LoginSteps:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver)

    def open_home_and_open_sign_in(self):
        self.login_page.open_home(self.base_url)
        sleep(5)
        self.login_page.go_to_sign_in()

    def enter_email_and_continue(self):
        self.login_page.fill_email(os.getenv("AMAZON_EMAIL"))
        sleep(1)
        self.login_page.click_continue()

    def enter_password_and_click_sign_in(self):
        self.login_page.fill_password(os.getenv("AMAZON_PASSWORD"))
        sleep(1)
        self.login_page.submit_sign_in()
        sleep(3)



