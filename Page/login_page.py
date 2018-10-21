from Base.Base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, user, password):
        """登录操作"""
        # 输入用户名
        self.send_element(Page.login_account_id, user)
        # 输入密码
        self.send_element(Page.login_passwd_id, password)
        # 点击登录按钮
        self.click_element(Page.login_btn_id)

    def if_login_btn_exits(self):
        # 判断登录按钮是否存在 存在返回True 不存在返回False
        try:
            self.search_element(Page.login_btn_id)
            return True
        except Exception as e:
            return False

    def close_login_page_btn(self):
        # 点击关闭登录页面按钮
        self.click_element(Page.close_login_page_btn_id)
