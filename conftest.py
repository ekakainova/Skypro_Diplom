import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def driver():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    browser.maximize_window()
    browser.get("https://www.kinopoisk.ru/")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
