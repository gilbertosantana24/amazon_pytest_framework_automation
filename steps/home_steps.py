import os
from time import sleep

from page_objects import home_page
from page_objects.base_page import BasePage
from selenium.webdriver import Keys

from page_objects.home_page import HomePage

class HomeSteps:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def search_item_in_bar(self, item_lookup):
        self.home_page.type_in_search(item_lookup)
        sleep(1)
        self.home_page.submit_search()
        sleep(1)
        #Assert search results contain the item
        page_source = self.driver.page_source
        assert item_lookup.lower() in page_source.lower(), f"'{item_lookup}' not found in search results"

    def add_to_cart_airpods(self):
        title_el = self.home_page.get_airpods_max_result()
        assert title_el is not None, "AirPods Max result not found"
        title_el.click()
        btn = self.home_page.get_add_to_cart_button()
        assert btn is not None, "Add to Cart button not found"
        btn.click()
        message_text = self.home_page.get_added_to_cart_message()
        assert "Added to cart" in message_text


