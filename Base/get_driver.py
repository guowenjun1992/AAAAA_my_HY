from appium import webdriver


def get_driver(pac,atc):
    """
    返回driver对象
    pac:包名
    atc:启动名
    """
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    # desired_caps['appPackage'] = 'com.android.mms'
    # desired_caps['appActivity'] = '.ui.ConversationList'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = atc
    # 获取toast文本信息
    desired_caps['automation'] = 'Uiautomator2'
    # 声明我们的driver对象
    return webdriver.Remote('http://192.168.45.24:4723/wd/hub', desired_caps)