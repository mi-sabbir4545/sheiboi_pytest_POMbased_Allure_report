from Pages.BasePage import BasePage
from Locators.Locators import LogoutLocators
from Config.config import TestData


class LogoutPage(BasePage):
    def __init__(self, driver):
        self.locator = LogoutLocators
        super(LogoutPage, self).__init__(driver)

    def ClickWelcome(self):
        self.clickwelcome(self.locator.button_logout_xpath)

    def ClickLogout(self):
        self.clicklogout(self.locator.logout_link_xpath)