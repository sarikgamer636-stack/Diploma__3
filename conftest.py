import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from helpers.urls import API_USER

def delete_user(driver):
    token = getattr(driver, "access_token", None)
    if token:
        requests.delete(API_USER, headers={"Authorization": token}, timeout=20)


@pytest.fixture
def driver_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    delete_user(driver)
    driver.quit()


@pytest.fixture
def driver_firefox():
    options = Options()
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("browser.formfill.enable", False)
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    delete_user(driver)
    driver.quit()