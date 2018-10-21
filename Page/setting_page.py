from Base.Base import Base
import Page
class Setting_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_logout_btn(self,tag=1):
        """退出操作 tag=1为确认退出操作，否则取消
        """
        # 向上滑屏
        self.scree_scroll(1)
        # 点击退出按钮
        self.click_element(Page.logout_btn_id)
        if tag==1:
            self.click_element(Page.logout_acc_btn_id)
        else:
            self.click_element(Page.log_out_miss_btn_id)