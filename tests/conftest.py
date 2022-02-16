import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from libs.base_page import BasePage


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = BasePage(driver)
    driver.get(page.base_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
