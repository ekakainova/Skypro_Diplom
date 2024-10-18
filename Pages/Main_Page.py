from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, browser):
        self.driver = browser

    def pop_up_ads(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button.styles_root__EjoL7"))).click()

    def box_search(self, movie_name):
        seacrh_input = self.driver.find_element(
            By.CSS_SELECTOR, "input[name='kp_query']")
        seacrh_input.clear()
        seacrh_input.send_keys(movie_name)
        return movie_name

    def button_search_loupe(self):
        self.driver.find_element(
            By.CLASS_NAME, "search-form-submit-button__icon").click()

    def tv_series_category(self):
        serials = self.driver.find_element(By.XPATH,
                                           "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]")
        serials.click()

    def button_of_filters(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 "a[aria-label='Расширенный поиск']").click()

    def button_login(self):
        self.driver.find_element(
            By.CLASS_NAME, "styles_loginButton__LWZQp").click()
