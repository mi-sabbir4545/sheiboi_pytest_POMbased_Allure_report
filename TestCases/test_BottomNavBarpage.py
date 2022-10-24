import time
# import allure

import pytest
from TestCases.BaseTest import BaseTest
from Pages.BottomNavBarpage import BottomNavBarpage


# @allure.severity(allure.severity_level.NORMAL)
class Test_BottomNavBarpage(BaseTest):

    # @allure.severity(allure.severity_level.MINOR)
    def test_clickfacebook(self):
        tf = BottomNavBarpage(self.driver)
        time.sleep(3)
        tf.ClickFacebook()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clicktwiter(self):
        tt = BottomNavBarpage(self.driver)
        time.sleep(3)
        tt.ClickTwitter()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clickyoutube(self):
        ty = BottomNavBarpage(self.driver)
        time.sleep(3)
        ty.ClickYouTube()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clickplaystore(self):
        tp = BottomNavBarpage(self.driver)
        time.sleep(3)
        tp.ClickPlayStore()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clickappstore(self):
        ta = BottomNavBarpage(self.driver)
        time.sleep(3)
        ta.ClickAppStore()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clickhelp(self):
        th = BottomNavBarpage(self.driver)
        time.sleep(3)
        th.ClickHelp()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
