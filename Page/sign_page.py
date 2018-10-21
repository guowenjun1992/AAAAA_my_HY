from Base.Base import Base
import Page


class Sign_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_account_btn(self):
        """点击已有账号去登录"""
        self.click_element(Page.exits_account_id)
