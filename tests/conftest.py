import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("")
    driver.maximize_window()
    yield driver
    driver.quit()
