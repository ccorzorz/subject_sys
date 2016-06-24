#!/usr/bin/env python
# -*-coding=utf-8-*-
# Auther:ccorz Mail:ccniubi@163.com Blog:http://www.cnblogs.com/ccorz/
# GitHub:https://github.com/ccorzorz

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import core.manage_sys

"""
管理员后台入口,测试帐号admin/admin
"""

if __name__ == '__main__':
    core.manage_sys.login()
    core.manage_sys.main()