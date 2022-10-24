from Pages.BasePage import BasePage
from Locators.Locators import TopNavBarLocator
from Config.config import TestData


class TopNavBarPage(BasePage):
    def __init__(self, driver):
        self.locator = TopNavBarLocator
        super(TopNavBarPage, self).__init__(driver)

    def ClickHomePage(self):
        self.clickhomepage(self.locator.click_homepage)

    def ClickSubject(self):
        self.clicksubject(self.locator.click_subjectPage)

    def ClickTheWriter(self):
        self.clickthewriter(self.locator.click_writer)

    def ClickTheBook(self):
        self.clickthebook(self.locator.click_allbooks)

    def Send_Search(self):
        self.sendsearch(self.locator.send_searchopt, TestData.BOOKNAME)

    def ClickSearch(self):
        self.clicksearch(self.locator.click_searchopt)

    def ClickBook(self):
        self.clickbook(self.locator.click_book)

    def ClickAddCart(self):
        self.clickaddcart(self.locator.click_addtocart)

    def ClickCart(self):
        self.clickcart(self.locator.click_cart)

    def ClickDeleteCart(self):
        self.clickdeletecart(self.locator.click_deletecart)
