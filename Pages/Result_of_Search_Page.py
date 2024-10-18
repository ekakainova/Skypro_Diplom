from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ResultOfSearch:

    def __init__(self, browser):
        self.driver = browser

    def list_of_movies(self):
        try:
            search_result = self.driver.find_element(
                By.CLASS_NAME, "search_results_topText").text

            if search_result == "поиск: • результаты: 0":
                info_text = self.driver.find_element(
                    By.CSS_SELECTOR, "h2.textorangebig").text
                return info_text

            else:
                info = self.driver.find_elements(By.CSS_SELECTOR, "div.info")
                film_set = ""
                try:
                    for element in info:
                        film = element.find_element(
                            By.CSS_SELECTOR, "a[data-type='film']").text
                        film_set = film_set + film + ","
                        list_film_set = film_set.split(",")

                except NoSuchElementException:
                    pass

                return list_film_set

        except NoSuchElementException:
            pass

    def list_of_genres_movies(self):
        info = self.driver.find_elements(By.CSS_SELECTOR, "div.info")
        genres_set = ""
        try:
            for element in info:
                genre = element.find_element(
                    By.CSS_SELECTOR, "span:nth-child(3)").text
                genres_set = genres_set + genre + ","

        except NoSuchElementException:
            pass

        return genres_set
