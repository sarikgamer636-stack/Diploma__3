import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait as Wait
from helpers.locators import MODAL_OVERLAY

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return Wait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def close_modal(self):
        overlays = self.driver.find_elements(*MODAL_OVERLAY)
        for overlay in overlays:
            self.driver.execute_script("arguments[0].remove();", overlay)

    def click(self, locator):
        self.close_modal()
        time.sleep(3)
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        self.set_value(locator, text)

    def set_value(self, locator, text):
        self.close_modal()
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_url(self):
        return self.driver.current_url