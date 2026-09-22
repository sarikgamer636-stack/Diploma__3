import time
import requests

from helpers.data import NAME, PASSWORD, generate_email
from helpers.locators import ORDER_BUTTON
from helpers.urls import API_REGISTER, LOGIN_PAGE, MAIN_PAGE
from pages.login_page import LoginPage
from pages.main_page import MainPage


def register_and_login(driver):
    email = generate_email()
    response = requests.post(
        API_REGISTER,
        json={"email": email, "password": PASSWORD, "name": NAME},
        timeout=20,
    )
    driver.access_token = response.json().get("accessToken")

    login_page = LoginPage(driver)
    driver.get(LOGIN_PAGE)
    login_page.close_modal()
    login_page.set_email(email)
    login_page.set_password(PASSWORD)
    login_page.click_login()
    time.sleep(3)

    driver.get(MAIN_PAGE)
    login_page.close_modal()
    time.sleep(3)
    login_page.find_element(ORDER_BUTTON)


def make_order(driver):
    main_page = MainPage(driver)
    driver.get(MAIN_PAGE)
    main_page.close_modal()
    main_page.main_title_is_visible()
    main_page.add_ingredient_to_order()
    main_page.click_order()
    number = main_page.get_order_number()
    return number