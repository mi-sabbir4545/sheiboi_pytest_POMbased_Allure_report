from Pages.BasePage import BasePage
from Locators.Locators import LoginLocators
from Config.config import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginLocators
        super(LoginPage, self).__init__(driver)

    def ClickLoginIcon(self):
        self.clickloginicon(self.locator.click_login_icon)

    def ClickLoginButton(self):
        self.clickloginbutton(self.locator.click_login_button)

    def EnterUserName(self):
        self.enterusername(self.locator.textbox_username_xpath, TestData.USERNAME)

    def EnterPassword1(self):
        self.enterpassword1(self.locator.textbox_password1_xpath)

    def EnterPassword2(self):
        self.enterpassword2(self.locator.textbox_password2_xpath, TestData.PASSWORD)

    def ClickLogin(self):
        self.clicklogin(self.locator.button_login_xpath)




        # self.enter_at(self.locator.userNameTextBox, TestData.USER_NAME)

    # def click_login_button(self):
    #     self.click_element(self.locator.loginButton)

    # def clickLoginIcon(self):
    #     self.Find_Element(*self.locator.click_login_icon).click()


    # def enter_user_name(self):
    #     self.enter_at(TestData.USER_NAME, *self.locator.userNameTextBox)

    # def enter_password(self):
    #     self.enter_at(TestData.PASSWORD, *self.locator.passwordTextBox)
    #

