from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FiltersPage:

    def __init__(self, browser):
        self.driver = browser

    def MPAA_system(self, value):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "[name='m_act[mpaa]']"))).click()
        wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//option[text()='{value}']"))).click()

    def list_of_genres(self, genre):
        box_genres = self.driver.find_element(By.ID, "m_act[genre]")
        box_genres.find_element(
            By.XPATH, f"//option[text()='{genre}']").click()
        return genre

    def what_looking_for(self, video_type):
        self.driver.find_element(By.CSS_SELECTOR,
                                 "[name='m_act[content_find]']").click()
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.element_to_be_clickable((
            By.XPATH, f"//option[text()='{video_type}']"))).click()

    def button_search_one(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 "input.el_18.submit.nice_button").click()
