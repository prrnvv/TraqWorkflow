import os
import pytest
import allure
from datetime import datetime
from selenium import webdriver
from config.config import Config


def get_chrome_options(headless_mode):
    options = webdriver.ChromeOptions()
    if headless_mode:
        options.add_argument('--headless')
    else:
        pass

    return options


@pytest.fixture(scope='function', autouse=True)
def setup_teardown_actions(request):
    browser = Config.BROWSER.lower()
    headless_mode = Config.HEADLESS

    if browser == 'chrome':
        options = get_chrome_options(headless_mode)
        url = Config.BASE_URL
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()

    yield driver
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.quit()
