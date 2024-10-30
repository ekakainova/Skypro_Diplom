import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class MainPage:

    def __init__(self, browser):
        self.driver = browser

        self.close_ads = (By.CSS_SELECTOR, "button.styles_root__EjoL7")
        self.input_search = (By.CSS_SELECTOR, "input[name='kp_query']")
        self.loupe_icon = (By.CLASS_NAME, "search-form-submit-button__icon")
        self.series_category = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]")
        self.filters = (By.CSS_SELECTOR, "a[aria-label='Расширенный поиск']")
        self.login_button_one = (By.CLASS_NAME, "styles_loginButton__LWZQp")
        self.login_button_two = (
            By.CSS_SELECTOR, "button.ZbVGA14bTNo86weQTABU")

    @allure.step('''Закрыть всплывающую рекламу,
                 если появилась''')
    def pop_up_ads(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((self.close_ads))).click()
        except TimeoutException:
            pass

    @allure.step('''Ввести в поле поиска название
                 фильма: {movie_name}''')
    def box_search(self, movie_name):
        seacrh_input = self.driver.find_element(*self.input_search)
        seacrh_input.clear()
        seacrh_input.send_keys(movie_name)
        return movie_name

    @allure.step('''Нажать на кнопку поиска (лупы)''')
    def button_search_loupe(self):
        self.driver.find_element(*self.loupe_icon).click()

    @allure.step('''Нажать на кнопку категории "Сериалы"''')
    def tv_series_category(self):
        serials = self.driver.find_element(*self.series_category)
        serials.click()

    @allure.step('''Нажать на кнопку фильтров''')
    def button_of_filters(self):
        self.driver.find_element(*self.filters).click()

    @allure.step('''Нажать на кнопку "Войти"''')
    def button_login(self):
        try:
            self.driver.find_element(*self.login_button_one).click()
        except NoSuchElementException:
            self.driver.find_element(*self.login_button_two).click()
