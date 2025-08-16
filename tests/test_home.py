# tests/test_home.py
import pytest

from page_objects import home_page
from steps.home_steps import HomeSteps

@pytest.mark.smoke
def test_search_item_in_home_page(driver):
    steps = HomeSteps(driver)
    steps.search_item_in_bar("AirPods Max")
    assert "AirPods Max" in driver.page_source, "Search results do not contain AirPods Max"
    steps.add_to_cart_airpods()