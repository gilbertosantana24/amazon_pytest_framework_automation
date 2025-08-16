from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from utils.waits import is_element_displayed, is_clickable


class HomePage(BasePage):
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    LOOK_UP_BUTTON = (By.ID, "nav-search-submit-button")
    AIRPODS_MAX_TITLE = (By.XPATH, "//div[@data-component-type='s-search-result']//h2[contains(@aria-label,"
                                   " 'AirPods Max')]")
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    ADDED_TO_CART = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")

#ACTIONS
    def get_search_bar(self):
        return is_element_displayed(self.driver, self.SEARCH_BAR)

    def type_in_search(self, text: str):
        el = self.get_search_bar()
        el.click()
        el.send_keys(text)

    def submit_search(self):
        is_clickable(self.driver, self.LOOK_UP_BUTTON).click()

    def get_airpods_max_result(self):
        return is_element_displayed(self.driver, self.AIRPODS_MAX_TITLE)

    def get_add_to_cart_button(self):
        return is_clickable(self.driver, self.ADD_TO_CART)

    def scroll_to_item(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_added_to_cart_message(self):
        el = is_element_displayed(self.driver, self.ADDED_TO_CART)
        return el.text
