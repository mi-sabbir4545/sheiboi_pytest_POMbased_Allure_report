import time

import pytest
from TestCases.BaseTest import BaseTest
from Pages.TopNavBarPage import TopNavBarPage


class Test_TopNavBarPage(BaseTest):

    def test_home(self):
        hm = TopNavBarPage(self.driver)
        time.sleep(3)
        hm.ClickHomePage()
        time.sleep(3)

    def test_subject(self):
        sb = TopNavBarPage(self.driver)
        time.sleep(3)
        sb.ClickSubject()
        time.sleep(3)

    def test_the_writer(self):
        tw = TopNavBarPage(self.driver)
        time.sleep(3)
        tw.ClickTheWriter()
        time.sleep(3)

    def test_the_books(self):
        tb = TopNavBarPage(self.driver)
        time.sleep(3)
        tb.ClickTheBook()
        time.sleep(3)

    def test_search(self):
        ts = TopNavBarPage(self.driver)
        time.sleep(3)
        ts.Send_Search()
        time.sleep(3)

    def test_clicksearch(self):
        tc = TopNavBarPage(self.driver)
        time.sleep(3)
        tc.ClickSearch()
        time.sleep(3)

    def test_clickbook(self):
        te = TopNavBarPage(self.driver)
        time.sleep(3)
        te.ClickBook()
        time.sleep(3)

    def test_addcart(self):
        ta = TopNavBarPage(self.driver)
        time.sleep(3)
        ta.ClickAddCart()
        time.sleep(3)

    def test_deletecart(self):
        td = TopNavBarPage(self.driver)
        time.sleep(3)
        td.ClickCart()
        time.sleep(3)
        td.ClickDeleteCart()
        time.sleep(3)
