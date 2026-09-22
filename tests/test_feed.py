import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from helpers.steps import make_order, register_and_login
from helpers.urls import FEED_PAGE
from pages.feed_page import FeedPage

@allure.epic("UI Stellar Burgers")
@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Проверка: что после заказа растёт счётчик за всё время")
    def check_all_time_orders(self, driver):
        with allure.step("Смотрим счётчик заказа за всё время"):
            driver.get(FEED_PAGE)
            feed_page = FeedPage(driver)
            before = feed_page.get_all_time_orders()

        with allure.step("Входим и делаем заказ"):
            register_and_login(driver)
            make_order(driver)

        with allure.step("Проверяем, что счётчик вырос"):
            driver.get(FEED_PAGE)
            Wait(driver, 20).until(lambda d: FeedPage(d).get_all_time_orders() > before)
            after = FeedPage(driver).get_all_time_orders()
            assert after > before

    def test_all_time_orders_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_all_time_orders(driver_chrome)

    def test_all_time_orders_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_all_time_orders(driver_firefox)

    @allure.title("Проверка: что после заказа растёт счётчик за сегодня")
    def check_today_orders(self, driver):
        with allure.step("Смотрим счётчик за сегодня"):
            driver.get(FEED_PAGE)
            feed_page = FeedPage(driver)
            before = feed_page.get_today_orders()

        with allure.step("Входим и делаем заказ"):
            register_and_login(driver)
            make_order(driver)

        with allure.step("Проверяем, что счётчик вырос"):
            driver.get(FEED_PAGE)
            Wait(driver, 20).until(lambda d: FeedPage(d).get_today_orders() > before)
            after = FeedPage(driver).get_today_orders()
            assert after > before

    def test_today_orders_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_today_orders(driver_chrome)

    def test_today_orders_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_today_orders(driver_firefox)

    @allure.title("Проверка:что номер заказа появляется в разделе В работе")
    def check_order_in_progress(self, driver):
        with allure.step("Входим и делаем заказ"):
            register_and_login(driver)
            number = make_order(driver)

        with allure.step("Открыть ленту и проверить раздел В работе"):
            driver.get(FEED_PAGE)
            feed_page = FeedPage(driver)
            Wait(driver, 20).until(lambda d: FeedPage(d).in_progress_has_number(number))
            assert feed_page.in_progress_has_number(number)

    def test_order_in_progress_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_order_in_progress(driver_chrome)

    def test_order_in_progress_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_order_in_progress(driver_firefox)