import allure
from helpers.urls import FEED_PAGE, MAIN_PAGE
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Основной функционал")
class TestMain:

    @allure.title("Проверка: перехода по клику на Конструктор")
    def check_constructor_button(self, driver):
        with allure.step("Открыть ленту заказов"):
            driver.get(FEED_PAGE)
            main_page = MainPage(driver)

        with allure.step("Нажать Конструктор"):
            main_page.click_constructor()

        with allure.step("Возвращаемся на главную и сверяем URL"):
            assert main_page.main_title_is_visible()
            assert MAIN_PAGE in main_page.get_url()

    def test_constructor_button_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_constructor_button(driver_chrome)

    def test_constructor_button_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_constructor_button(driver_firefox)

    @allure.title("Переход по клику на Лента заказов")
    def check_orders_list_button(self, driver):
        with allure.step("Открыть главную"):
            driver.get(MAIN_PAGE)
            main_page = MainPage(driver)

        with allure.step("Нажать Лента заказов"):
            main_page.click_orders_list()
            feed_page = FeedPage(driver)

        with allure.step("Проверить переход в ленту"):
            assert feed_page.orders_list_is_visible()
            assert FEED_PAGE in feed_page.get_url()

    def test_orders_list_button_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_orders_list_button(driver_chrome)

    def test_orders_list_button_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_orders_list_button(driver_firefox)

    @allure.title("По клику на ингредиент открывается окно с деталями")
    def check_ingredient_details(self, driver):
        with allure.step("Открыть главную и кликнуть ингредиент"):
            driver.get(MAIN_PAGE)
            main_page = MainPage(driver)
            main_page.click_ingredient()

        with allure.step("Проверить окно деталей"):
            assert main_page.ingredient_details_is_visible()

    def test_ingredient_details_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_ingredient_details(driver_chrome)

    def test_ingredient_details_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_ingredient_details(driver_firefox)

    @allure.title("Окно с деталями закрывается по крестику")
    def check_ingredient_details_close(self, driver):
        with allure.step("Открыть детали ингредиента"):
            driver.get(MAIN_PAGE)
            main_page = MainPage(driver)
            main_page.click_ingredient()

        with allure.step("Закрыть окно крестиком"):
            main_page.close_ingredient_details()

        with allure.step("Проверить, что снова видна главная"):
            assert main_page.main_title_is_visible()

    def test_ingredient_details_close_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_ingredient_details_close(driver_chrome)

    def test_ingredient_details_close_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_ingredient_details_close(driver_firefox)

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def check_ingredient_orders(self, driver):
        with allure.step("Открыть главную и запомнить счётчик"):
            driver.get(MAIN_PAGE)
            main_page = MainPage(driver)
            before = main_page.get_ingredient_counter()

        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
            after = main_page.get_ingredient_counter()

        with allure.step("Проверить, что счётчик вырос"):
            assert after > before

    def test_ingredient_orders_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            self.check_ingredient_orders(driver_chrome)

    def test_ingredient_orders_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            self.check_ingredient_orders(driver_firefox)