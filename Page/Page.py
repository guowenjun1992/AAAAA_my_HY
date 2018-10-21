from Page.home_page import Home_Page
from Page.sign_page import Sign_Page
from Page.login_page import Login_Page
from Page.person_page import Person_Page
from Page.setting_page import Setting_Page


class Page():
    def __init__(self, driver):
        self.driver = driver

    def get_home_page_obj(self):
        return Home_Page(self.driver)

    def get_sign_page_obj(self):
        return Sign_Page(self.driver)

    def get_login_page_obj(self):
        return Login_Page(self.driver)

    def get_person_page_obj(self):
        return Person_Page(self.driver)

    def get_setting_page(self):
        return Setting_Page(self.driver)
＃这是一具果园果
