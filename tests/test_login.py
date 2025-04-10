import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.logger import logger
from utils.property_reader import PropertyReader

properties = PropertyReader(os.path.join("config/global.properties"))

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self, setup):
        logger.info("Running: test_valid_login")
        logger.info(f"Email: {properties.get('email')}, Password: {properties.get('password')}")
        login = LoginPage(setup)
        login.login(properties.get("email"), properties.get("password"))

        WebDriverWait(setup, 5).until(EC.url_contains("dashboard"))
        logger.info(f"Post-login URL: {setup.current_url}")

        assert "dashboard" in setup.current_url

    def test_invalid_password(self, setup):
        logger.info("Running: test_invalid_password")
        login = LoginPage(setup)
        login.login(properties.get("email"), properties.get("invalid_password"))
        assert "Incorrect email or password." in login.get_error_message()

    def test_invalid_email(self, setup):
        logger.info("Running: test_invalid_email")
        login = LoginPage(setup)
        login.login(properties.get("invalid_email"), properties.get("password"))
        assert "Incorrect email or password." in login.get_error_message()