import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, browser):
        self.driver = browser

        self.field_login = (By.ID, "passp-field-login")
        self.button_sign_in = (By.ID, "passp:sign-in")
        self.password_button = (By.CLASS_NAME, "PasswordButton")
        self.field_password = (By.ID, "passp-field-passwd")
        self.error_element = (By.CLASS_NAME, "Textinput_state_error")
        self.error_message = (By.ID, "field:input-passwd:hint")

    @allure.step('''ui. Ввести на странице авторизации
                 в поле "логин" логин/e-mail {login_e_mail}''')
    def login_field(self, login_e_mail):
        login_box = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((self.field_login)))
        login_box.clear()
        login_box.send_keys(login_e_mail)

    @allure.step('''ui. Нажать на кнопку "Войти"''')
    def button_sign_in_one(self):
        self.driver.find_element(*self.button_sign_in).click()

    @allure.step('''ui. Нажать на кнопку "Войти с паролем"''')
    def button_password(self):
        self.driver.find_element(*self.password_button).click()

    @allure.step('''ui. Ввести на странице авторизации
                 в поле "пароль": {password_value}''')
    def password_field(self, password_value):
        password_box = self.driver.find_element(*self.field_password)
        password_box.clear()
        password_box.send_keys(password_value)

    @allure.step('''ui. Нажать на кнопку "Продолжить"''')
    def button_sign_in_two(self):
        self.driver.find_element(*self.button_sign_in).click()
        if self.driver.find_element(*self.error_element):
            hint = self.driver.find_element(*self.error_message).text
            return hint
        else:
            pass
