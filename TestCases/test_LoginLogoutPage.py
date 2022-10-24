import time
# import allure
# import allure_pytest
# from allure_commons.types import AttachmentType
import pytest
from TestCases.BaseTest import BaseTest
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage


# @allure.severity(allure.severity_level.NORMAL)
class Test_LoginLogout(BaseTest):

    # @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.ClickLoginIcon()
        time.sleep(3)
        lp.ClickLoginButton()
        time.sleep(3)
        lp.EnterUserName()
        time.sleep(3)
        lp.EnterPassword1()
        time.sleep(3)
        lp.EnterPassword2()
        time.sleep(3)
        lp.ClickLogin()
        time.sleep(3)

    # allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)

    # @allure.severity(allure.severity_level.MINOR)
    def test_logout(self):
        lg = LogoutPage(self.driver)
        lg.ClickWelcome()
        time.sleep(3)
        lg.ClickLogout()
        time.sleep(3)
