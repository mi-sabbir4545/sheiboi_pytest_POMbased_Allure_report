from Pages.BasePage import BasePage
from Locators.Locators import BottomNavBarLocator
from Config.config import TestData


class BottomNavBarpage(BasePage):
    def __init__(self, driver):
        self.locator = BottomNavBarLocator
        super(BottomNavBarpage, self).__init__(driver)

    def ClickFacebook(self):
        self.clickfacebook(self.locator.click_facebookicon)

    def ClickTwitter(self):
        self.clicktwitter(self.locator.click_twittericon)

    def ClickYouTube(self):
        self.clickyoutube(self.locator.click_youtubeicon)

    def ClickPlayStore(self):
        self.clickplaystore(self.locator.click_playstoreicon)

    def ClickAppStore(self):
        self.clickappstore(self.locator.click_appstoreicon)

    def ClickHelp(self):
        self.clickhelp(self.locator.click_helpbutton)