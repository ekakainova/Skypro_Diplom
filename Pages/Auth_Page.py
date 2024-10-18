from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, browser):
        self.driver = browser

    def login_field(self, login_e_mail):
        login_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "passp-field-login")))
        login_box.clear()
        login_box.send_keys(login_e_mail)

    def button_sign_in_one(self):
        self.driver.find_element(By.ID, "passp:sign-in").click()

    def button_password(self):
        self.driver.find_element(By.CLASS_NAME, "PasswordButton").click()

    def password_field(self, password_value):
        password_box = self.driver.find_element(By.ID, "passp-field-passwd")
        password_box.clear()
        password_box.send_keys(password_value)

    def button_sign_in_two(self):
        self.driver.find_element(By.ID, "passp:sign-in").click()
        if self.driver.find_element(By.CLASS_NAME, "Textinput_state_error"):
            hint = self.driver.find_element(
                By.ID, "field:input-passwd:hint").text
            return hint
        else:
            pass
