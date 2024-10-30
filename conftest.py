import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.Movie_Search_Api_Page import Movie_Search
from config import kinopoisk_key, kinopoisk_url


@pytest.fixture(scope='module')
def driver():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.get("https://www.kinopoisk.ru/")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture(scope='module')
def api():
    return Movie_Search(kinopoisk_url, kinopoisk_key)
