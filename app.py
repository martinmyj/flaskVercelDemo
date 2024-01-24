# -*- coding: utf-8 -*-
"""
@Author: 茅祎玖 
@Date: 2024-01-24
@Function: 
"""
import flask
import random
citys = ['北京', '上海', '广州', '深圳', '成都', '重庆', '杭州', '南京', '苏州', '武汉', '天津', '西安', '长沙', '沈阳', '济南', '青岛', '大连', '福州', '厦门', '南昌', '郑州']

app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Index page!"


@app.route('/getLocation')
def get_location():
    return random.choice(citys)


if __name__ == '__main__':
    app.run(debug=True)
