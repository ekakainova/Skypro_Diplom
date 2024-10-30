import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ResultOfSearch:

    def __init__(self, browser):
        self.driver = browser

        self.result = (By.CLASS_NAME, "search_results_topText")
        self.text_result = (By.CSS_SELECTOR, "h2.textorangebig")
        self.movies_list = (By.CSS_SELECTOR, "div.info")
        self.movie_type = (By.CSS_SELECTOR, "a[data-type='film']")
        self.movie_genre = (By.CSS_SELECTOR, "span:nth-child(3)")

    @allure.step('''Получить список названий фильмов,
                 найденных в результате поиска''')
    def list_of_movies(self):
        try:
            search_result = self.driver.find_element(*self.result).text

            if search_result == "поиск: • результаты: 0":
                info_text = self.driver.find_element(*self.text_result).text
                return info_text

            else:
                info = self.driver.find_elements(*self.movies_list)
                film_set = ""
                try:
                    for element in info:
                        film = element.find_element(*self.movie_type).text
                        film_set = film_set + film + ","
                        list_film_set = film_set.split(",")

                except NoSuchElementException:
                    pass

                return list_film_set

        except NoSuchElementException:
            pass

    @allure.step('''Получить список жанров фильмов,
                 найденных в результате поиска''')
    def list_of_genres_movies(self):
        info = self.driver.find_elements(*self.movies_list)
        genres_set = ""
        try:
            for element in info:
                genre = element.find_element(*self.movie_genre).text
                genres_set = genres_set + genre + ","

        except NoSuchElementException:
            pass

        return genres_set
