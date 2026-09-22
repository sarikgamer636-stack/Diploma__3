from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time
from helpers.locators import *
from pages.base_page import BasePage


class MainPage(BasePage):

    def main_title_is_visible(self):
        self.find_element(MAIN_TITLE)
        return True

    def click_constructor(self):
        self.click(CONSTRUCTOR_BUTTON)

    def click_orders_list(self):
        self.click(ORDERS_LIST_BUTTON)

    def click_ingredient(self):
        self.click(INGREDIENT)

    def ingredient_details_is_visible(self):
        self.find_element(INGRIDIENTS_DETAILS)
        return True

    def close_ingredient_details(self):
        self.click(INGRIDIENTS_WINDOW_CLOSE)

    def get_ingredient_counter(self):
        ingredient = self.find_element(INGREDIENT)
        return int(ingredient.find_element(*INGREDIENT_COUNTER).text)

    def add_ingredient_to_order(self):
        source = self.find_element(INGREDIENT)
        target = self.find_element(CONSTRUCTOR_BASKET)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const data = new DataTransfer();
            data.setData('text/plain', source.href || 'ingredient');
            const event = { bubbles: true, cancelable: true, dataTransfer: data };
            source.dispatchEvent(new DragEvent('dragstart', event));
            target.dispatchEvent(new DragEvent('dragenter', event));
            target.dispatchEvent(new DragEvent('dragover', event));
            target.dispatchEvent(new DragEvent('drop', event));
            source.dispatchEvent(new DragEvent('dragend', event));
            """,
            source,
            target,
        )
        time.sleep(2)

    def click_enter_account(self):
        self.click(ENTER_ACCOUNT_BUTTON)

    def click_order(self):
        self.click(ORDER_BUTTON)

    def get_order_number(self):
        time.sleep(5)
        Wait(self.driver, 30).until(
            lambda driver: self.get_text(ORDER_NUMBER) not in ("", "9999")
        )
        return self.get_text(ORDER_NUMBER)