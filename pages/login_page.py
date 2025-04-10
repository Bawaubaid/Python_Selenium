from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "userEmail")
    PASSWORD = (By.ID, "userPassword")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[aria-label='Incorrect email or password.']")

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)
