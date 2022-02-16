from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class AddPartner(BasePage):

    @property
    def add_partner_button(self):
        locator = Locator(by=By.XPATH, value="//a[@ng-click='addVendor()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_name_input(self):
        locator = Locator(by=By.XPATH, value="//input[@ng-model='newVendor.name']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_email_input(self):
        locator = Locator(by=By.XPATH, value="//input[@ng-model='newVendor.email']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def short_onboarding_checkbox(self):
        locator = Locator(by=By.XPATH, value="//div[@class='multistate-checkbox multistate-checkbox--empty']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def switch_button(self):
        locator = Locator(by=By.XPATH, value="//label[@class='switcher-line']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_to_index_button(self):
        locator = Locator(by=By.XPATH, value="//a[@ng-click='$ctrl.addVendors()']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def all_partners(self):
        locator = Locator(by=By.CLASS_NAME, value="vendor-item-name")
        return BaseElement(driver=self.driver, locator=locator)