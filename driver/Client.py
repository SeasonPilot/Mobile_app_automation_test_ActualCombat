# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/7/5 20:30
# 文件名：Client.py
# 开发工具：PyCharm

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient:
    driver:WebDriver

    @classmethod
    def restart_app(cls):
        caps = {}

        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["platformName"] = "Android"
        caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"
        # 不加 automationName 会报错
        caps["automationName"] = "UiAutomator1"

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls.driver.implicitly_wait(20)

        return cls.driver
