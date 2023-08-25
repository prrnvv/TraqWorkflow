from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise   TimeoutError(f"Element {locator} not found within {timeout} seconds")

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_page_title(self):
        return self.driver.title

    def quit(self):
        self.driver.quit()
