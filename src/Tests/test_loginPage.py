from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from config.config import TestData


class TestLogin(BaseTest):

    # def test_signup_link_visible(self):
    #     self.loginPage = LoginPage(self.driver)
    #     flag = self.loginPage.is_signup_link_exist()
    #     assert flag


    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
