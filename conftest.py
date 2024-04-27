import os
from datetime import datetime


import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# chromedriver_path = '/usr/local/bin/chromedriver-mac-arm64'

#HOST can be announced to define on which environment to run tests
# HOST = os.getenv("DEV") if os.environ["STAGE"] == "dev" else os.getenv("PROD")

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)

    driver.quit()


