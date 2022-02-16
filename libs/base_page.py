from selenium import webdriver


class BasePage(object):
    base_URI = "https://autotest.worksuite.com"
    base_URL = base_URI + "/api/users/login/1j/ce3fbc2d7db64d6d87493bf444e7363d/"

    def __init__(self, driver: webdriver):
        self.driver = driver