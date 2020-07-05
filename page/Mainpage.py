# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/7/5 22:09
# 文件名：Mainpage.py
# 开发工具：PyCharm
from driver.Client import AndroidClient
from page.Quotation import Quotation


class Mainpage:

    def init(self):
        AndroidClient.restart_app()

    def gotoquotation(self):
        AndroidClient.driver.find_element_by_xpath("*//[text='行情']")
        AndroidClient.driver.find_element_by_xpath("*//[text='行情']").click()


# 这里返回的是 Quotation 实例化对象
        return Quotation()
