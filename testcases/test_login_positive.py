import pytest
import allure
from pages.login_page import LoginPage
from utils.data_provider import get_login_data_positive
from utils.logging import setup_logging
from utils.marks import sanity, login, positive
from utils.retry import retry


@pytest.fixture
def logger():
    return setup_logging()


@pytest.mark.usefixtures("setup_teardown_actions", "logger")
class TestLoginPositive:
    @pytest.mark.parametrize("username", "password", get_login_data_positive())
    @sanity
    @login
    @positive
    @retry(max_retries=3, delay=1)
    def test_login_positive(self, setup_teardown_actions, username, password, logger):
        login_page = LoginPage(setup_teardown_actions)
        logger.info(f"Entering Username: {username}")
        login_page.enter_username(username)
        logger.info(f"Entering Password: {password}")
        login_page.enter_password(password)
        logger.info(f"Clicking on Login Button")
        login_page.click_login()

    try:
        assert "https://traq-qa.leftrightmind.com/main-areas" == setup_teardown_actions.current_url
        logger.info(f"Login successful for user: {username} and password: {password}")

    except AssertionError:
        logger.error(f"Login failed for user: {username} and password: {password}")
        allure.attach(setup_teardown_actions.get_screenshot_as_png(), name="Login Positive Failed",
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail("Login failed for positive test case")