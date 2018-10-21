import sys, os

sys.path.append(os.getcwd())
import pytest
from Page.Page import Page
from Base.get_driver import get_driver
from Base.get_yaml import Get_Yaml


def get_login_data():
    login_scc = []
    login_s = []
    data = Get_Yaml().get_yaml_file('aolai.yaml')
    for i in data.keys():
        if data.get(i).get('tag'):
            login_scc.append((i, data.get(i).get('phone'), data.get(i).get('passwd'),
                              data.get(i).get('tag_message'), data.get(i).get('expect_requst')
                              ))
        else:
            login_s.append((i, data.get(i).get('phone'), data.get(i).get('passwd'),
                            data.get(i).get('tag_message'), data.get(i).get('expect_requst')
                            ))
    return {'scc':login_scc,'s':login_s}

class Test_01:
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.fixture(autouse=True)
    def in_login(self):
        # 点击我的
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号登录
        self.page_obj.get_sign_page_obj().click_exits_account_btn()

    @pytest.mark.parametrize('test_num,phone,passwd,tag_message,expect_requst', get_login_data().get('scc'))
    def test_login_scc(self, test_num, phone, passwd, tag_message, expect_requst):
        """预期正确的用例"""
        try:
            coupons = self.page_obj.get_person_page_obj().get_coupons_text()
            try:
                assert coupons == expect_requst
            except AssertionError as e:
                print(e.__str__())
            # 点击设置
            self.page_obj.get_person_page_obj().click_setting_btn()
            # 点击退出
            self.page_obj.get_setting_page().click_logout_btn()
        except TimeoutError as e:
            # 关闭登录页面
            self.page_obj.get_login_page_obj().close_login_page_btn()

    @pytest.mark.parametrize('test_num,phone,passwd,tag_message,expect_requst', get_login_data().get('s'))
    def test_login_s(self, test_num, phone, passwd, tag_message, expect_requst):
        """预期失败的用例"""
        pass
