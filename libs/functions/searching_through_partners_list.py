from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def searching_through_partners_list(browser):
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "vendor-item-name")))
    all_partners = browser.find_elements_by_class_name('vendor-item-name')
    all_partners_list = []

    if len(all_partners) > 0:
        for all_partners_name in all_partners:
            all_partners_list.append(all_partners_name.text)
    return all_partners_list
