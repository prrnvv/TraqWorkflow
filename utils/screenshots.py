import os
from datetime import datetime
from selenium import webdriver


def capture_screenshot(driver, screenshot_dir="screenshots"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    try:
        driver.save_screenshot(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"Failed to save screenshot: {str(e)}")
