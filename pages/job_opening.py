from selenium.webdriver.common.by import By

from libs.base_element import BaseElement
from libs.base_page import BasePage
from libs.locators.base_locator import Locator


class JobOpening(BasePage):

    @property
    def new_job_opening_button(self):
        locator = Locator(by=By.XPATH, value="//span[@class='btn-inner-text']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def job_title_input(self):
        locator = Locator(by=By.XPATH, value="//input[@placeholder='Job title']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def create_job_opening_button(self):
        locator = Locator(by=By.XPATH, value="//span[@ng-show='!$ctrl.formSaving && !$ctrl.jobOpening.id']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def back_to_jobs_list(self):
        locator = Locator(by=By.XPATH, value="//a[@class='nav-back']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def jobs_list(self):
        locator = Locator(by=By.XPATH, value="//a[contains(@ng-if,'column.config.getTextCellLink')]")
        return BaseElement(driver=self.driver, locator=locator)