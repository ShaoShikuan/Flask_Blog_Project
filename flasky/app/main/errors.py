# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 20:51
# @Author  : SSK
# @FileName: errors.py
# @Software: PyCharm
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
