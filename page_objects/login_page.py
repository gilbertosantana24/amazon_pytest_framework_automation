from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.waits import is_element_displayed, is_clickable

class LoginPage(BasePage):
    HELLO_SIGN_IN = (By.ID, "nav-link-accountList-nav-line-1")
    EMAIL_INPUT_CELL = (By.ID, "ap_email_login")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_INPUT_CELL = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")

#GETTERS
    @property
    def hello_sign_in(self):
        return is_element_displayed(self.driver, self.HELLO_SIGN_IN)

    @property
    def email_login(self):
        return is_element_displayed(self.driver, self.EMAIL_INPUT_CELL)

    @property
    def continue_button(self):
        return is_clickable(self.driver, self.CONTINUE_BUTTON)

    @property
    def password_input(self):
        return is_element_displayed(self.driver, self.PASSWORD_INPUT_CELL)

    @property
    def sign_in_submit(self):
        return is_clickable(self.driver, self.SIGN_IN_BUTTON)

#ACTIONS
    def open_home(self, base_url: str):
        self.openWebPage(base_url)

    def go_to_sign_in(self):
        self.hello_sign_in.click()

    def fill_email(self, email: str):
        self.email_login.click()
        self.email_login.send_keys(email)

    def click_continue(self):
        self.continue_button.click()

    def fill_password(self, password: str):
        self.password_input.click()
        self.password_input.send_keys(password)

    def submit_sign_in(self):
        self.sign_in_submit.click()

