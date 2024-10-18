from selenium.webdriver.common.by import By


class SeriesPage:

    def __init__(self, browser):
        self.driver = browser

    def list_of_series_types(self):
        series_types = self.driver.find_elements(
            By.CSS_SELECTOR, "a.styles_root__c9qje")
        type_set = ""

        for element in series_types:
            category = element.find_element(
                By.CSS_SELECTOR, "span.styles_name__G_1mq").text
            type_set = type_set + category + ","
            list_type_set = type_set.split(",")

        return list_type_set
