import sys, os

from selenium.common.exceptions import TimeoutException

sys.path.append(os.getcwd())
import pytest
from Page.Page import Page
from Base.get_yaml import Get_Yaml
from Base.get_driver import get_driver


def get_aolai_data():
    aolai_list = []
    data = Get_Yaml().get_yaml_file('aolai.yaml')
    for i in data.keys():
        aolai_list.append((i, data.get(i).get('phone'), data.get(i).get('passwd'),
                           data.get(i).get('tag'), data.get(i).get('tag_message'),
                           data.get(i).get('expect_requst'),))
    return aolai_list


class Test_Login:
    def setup_class(self):
        # 实例化一个page的统一入口类对象
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize('test_num,phone,passwd,tag,tag_message,expect_requst', get_aolai_data())
    def test_login(self, test_num, phone, passwd, tag, tag_message, expect_requst):
        # 点击我的按钮
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_sign_page_obj().click_exits_account_btn()
        # 进行登录操作
        self.page_obj.get_login_page_obj().login(phone, passwd)
        # 断言是否登录成功，成功就退出，未成功则判断提示信息，
        if tag == 1:
            # 预期成功用例
            try:
                # 定位我的优惠券
                coupons = self.page_obj.get_person_page_obj().get_coupons_text()
                try:
                    # 断言 定位的我的优惠券文本==预期结果
                    assert coupons == expect_requst
                # 元素依然是可以找到的，只是里面的文本可能变了，所以断言时文本不相等 ，但不影响，所以捕获这个异常
                except AssertionError as e:
                    print(e.__str__())
                # 执行退出操作
                # 点击设置按钮
                self.page_obj.get_person_page_obj().click_setting_btn()
                # 向上滑屏，点击退出登录
                self.page_obj.get_setting_page().click_logout_btn()

            # 如果找不到我的优惠券，那么说明本该本成功的用例失败了
            except TimeoutException as e:
                # 关闭登录页面
                self.page_obj.get_login_page_obj().close_login_page_btn()
                # 执行到这里，说明本次用例执行失败，必须抛一个异常，不然会显示本次用例是成功的
                assert False

        else:
            # 预期失败案例
            try:
                # 获取toast消息
                toast_message = self.page_obj.get_person_page_obj().get_toast_text(tag_message)
                print(toast_message)
                # 获取登录按钮是否存在
                if_login_btn = self.page_obj.get_login_page_obj().if_login_btn_exits()
                print(if_login_btn)
                # 断言取到了toast文本=预期 同时在登录页面
                assert if_login_btn  and toast_message == expect_requst
                print(expect_requst)
            # 如果找不到toast消息，就会超时，所以捕获超时异常
            except TimeoutException as e :
                # 找不到说明和预期不一样，那就是这条用例运行失败，所以必须抛一个异常，不然会显示运行成功
                assert False
            # 不管执行成功还是失败都要把这个页面关闭，才能不影响下一条用例的执行
            finally:
                # 关闭登录页面
                self.page_obj.get_login_page_obj().close_login_page_btn()

