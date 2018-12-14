# -*- coding: utf-8 -*-  
import sys  
reload(sys)                      
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice
import traceback

# 文章的url地址
url = "https://blog.csdn.net/m0_37313888/article/details/84941527"


def trin():
    # 设置代理头
    user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
    ]
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.loadImages"] = False  # 不载入图片，加快爬取加载速度
    dcap["phantomjs.page.settings.userAgent"] = choice(user_agent)  # 从user_agent列表中随机选一个浏览器头，伪装浏览器
    driver = webdriver.PhantomJS(desired_capabilities=dcap)

    # 设置时间
    driver.set_page_load_timeout(20)
    try:
        print u'尝试打开网页'
        driver.get(url)

        # 网页截图
        driver.save_screenshot('test.png')
        print u'图片已保存'

        # 关闭网页
        driver.quit()
        print u"网页已关闭"

        # 设置休眠时间，防止访问过于频繁
        time.sleep(5)

    except Exception:
        # 抛出异常并指出具体在哪一行
        traceback.print_exc()


for i in range(50):
    # 访问10次
    trin()