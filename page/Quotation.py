# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/7/5 21:02
# 文件名：Quotation.py
# 开发工具：PyCharm
from driver.Client import AndroidClient


class Quotation:
    def Sz(self):

        # text后面没有括号
        price=AndroidClient.driver.find_element_by_xpath\
            ('//*[@text="深证成指"]/..//*[contains(@resource-id,"index_price")]').text

        return float(price)





