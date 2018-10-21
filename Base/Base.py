# 用来封装常用的方法，给它的子类使用
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位单个元素
        :loc：元祖 定位类型（By.ID,ID属性值)（By.CLASS,CLASS属性值)（By.XPATH,XPATH属性值)
        :timeout: 查找元素超时时间
        :poll_frequency: 搜索间隔
        :return：返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位一组元素
        :loc：元祖 定位类型（By.ID,ID属性值)（By.CLASS,CLASS属性值)（By.XPATH,XPATH属性值)
        :timeout: 查找元素超时时间
        :poll_frequency: 搜索间隔
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def send_element(self, loc,text, timeout=15, poll_frequency=1.0):
        """
        输入文本内容
        :loc：元祖 定位类型（By.ID,ID属性值)（By.CLASS,CLASS属性值)（By.XPATH,XPATH属性值)
        :timeout: 查找元素超时时间
        :poll_frequency: 搜索间隔
        """
        # 定位输入框
        input_element = self.search_element(loc, timeout, poll_frequency)
        # 清空
        input_element.clear()
        # 输入文本
        input_element.send_keys(text)

    def click_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        点击一个元素
        :loc：元祖 定位类型（By.ID,ID属性值)（By.CLASS,CLASS属性值)（By.XPATH,XPATH属性值)
        :timeout: 查找元素超时时间
        :poll_frequency: 搜索间隔
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def scree_scroll(self, tag=1):
        """
        swipe屏幕滑动
        :tag：滑动方向 tag=1向上 tag=1向下 tag=1向左 tag=1向右
        """
        # 获取屏幕分辨率，返回一个字典
        data = self.driver.get_window_size()
        # 取出高和宽的值
        width = data.get('width')
        height = data.get('height')
        # 判断tap，做出相应滑动
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    def get_toast_text(self, mess):
        """定位错误提示信息 还回toast的文本信息
        """
        # xpath语句
        toast_xpath = "//*[contains(@text,'{}')]".format(mess)
        # 定位并返回toast信息的文本
        toast_message = self.search_element((By.XPATH, toast_xpath), timeout=5, poll_frequency=0.5).text
        return toast_message
