import os
import pytest
import configparser
from selenium import webdriver
from utils.property_reader import PropertyReader

config = configparser.ConfigParser()
abs_config_path = os.path.join(os.path.dirname(__file__), "config", "config.ini")
config.read(abs_config_path)

properties = PropertyReader(os.path.join("config/global.properties"))

@pytest.fixture()
def setup(request):
    browser = properties.get("browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    driver.get(config['DEFAULT']['base_url'])
    request.cls.driver = driver
    yield driver
    driver.quit()
