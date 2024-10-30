import allure
from selenium.webdriver.common.by import By


class SeriesPage:

    def __init__(self, browser):
        self.driver = browser

        self.series_list = (By.CSS_SELECTOR, "a.styles_root__c9qje")
        self.series_categories = (By.CSS_SELECTOR, "span.styles_name__G_1mq")

    @allure.step('''Получить список категорий сериалов''')
    def list_of_series_types(self):
        series_types = self.driver.find_elements(
            *self.series_list)
        type_set = ""

        for element in series_types:
            category = element.find_element(
                *self.series_categories).text
            type_set = type_set + category + ","
            list_type_set = type_set.split(",")

        return list_type_set
