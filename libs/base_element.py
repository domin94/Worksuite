from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()
        self.scroll()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", self.web_element)

    def input_text(self, txt):
        self.web_element.send_keys(txt)

    def click(self):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.web_element))
        element.click()

    def attribute(self, attr_name):
        return self.web_element.get_attribute(attr_name)

    def clean(self):
        return self.web_element.clear

    @property
    def text(self):
        return self.web_element.text
