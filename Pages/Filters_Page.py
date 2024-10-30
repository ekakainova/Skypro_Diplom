import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FiltersPage:

    def __init__(self, browser):
        self.driver = browser

        self.MPAA_field = (By.CSS_SELECTOR, "[name='m_act[mpaa]']")
        self.genre_field = (By.ID, "m_act[genre]")
        self.content_field = (By.CSS_SELECTOR, "[name='m_act[content_find]']")
        self.search_button = (
            By.CSS_SELECTOR, "input.el_18.submit.nice_button")

    @allure.step('''ui. Выбрать в фильтрах рейтинг: {value},
                 на странице расширенного поиска''')
    def MPAA_system(self, value):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((self.MPAA_field))).click()
        wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//option[text()='{value}']"))).click()

    @allure.step('''ui. Выбрать в фильтрах жанр: {genre},
                 на странице расширенного поиска''')
    def list_of_genres(self, genre):
        box_genres = self.driver.find_element(*self.genre_field)
        box_genres.find_element(
            By.XPATH, f"//option[text()='{genre}']").click()
        return genre

    @allure.step('''ui. Выбрать в фильтрах тип фильма:
                 {video_type},
                 на странице расширенного поиска''')
    def what_looking_for(self, video_type):
        self.driver.find_element(*self.content_field).click()
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//option[text()='{video_type}']"))).click()

    @allure.step('''ui. Нажать на кнопку "Поиск"''')
    def button_search_one(self):
        self.driver.find_element(*self.search_button).click()
