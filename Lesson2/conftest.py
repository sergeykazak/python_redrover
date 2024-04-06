import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print("\n Starting browser")
    yield driver # передаем созданный driver в тесты, которые будут использовать эту фикстуру
    print("\n Quitting from browser...")
    driver.quit()