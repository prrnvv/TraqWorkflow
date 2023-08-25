import allure
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            driver = item.funcargs["setup"]
            allure.attach(driver.get_screenshot_as_png(), name="Test Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to attach screenshot: {str(e)}")