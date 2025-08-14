class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def openWebPage(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)
