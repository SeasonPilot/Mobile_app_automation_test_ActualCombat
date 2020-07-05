# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/7/5 22:40
# 文件名：case1.py
# 开发工具：PyCharm

import pytest
from page.Mainpage import Mainpage


class TestSelected:
    def test_price(self):
        assert Mainpage.gotoquotation().Sz() == 12433.26