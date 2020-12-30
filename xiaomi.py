import asyncio

from pyppeteer import launch
from helper import *


async def main(URL, buy_time):
    browser = await launch(headless=False)
    content = await browser.createIncognitoBrowserContext()
    page = await content.newPage()
    await page.setViewport({'width': WIDTH, 'height': HEGHT})
    await page.goto('https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180')
    await asyncio.sleep(30)
    wait_second = get_start_time(buy_time)
    if wait_second - BEFORE_SECOND > 0:
        await asyncio.sleep(wait_second)
    await page.goto(URL)
    while True:
        try:
            # 找到“加入购物车”，点击
            await page.click('[class="btn btn-primary"]')

            break
        except:
            await asyncio.sleep(CLICK_FREQUENCY)
    while True:
        try:
            # 找到“进入购物车”，点击
            await page.click('[class="btn btn-primary"]')
            break
        except:
            await asyncio.sleep(CLICK_FREQUENCY)
    await asyncio.sleep(100)
    await browser.close()

"""
btn btn-a btn-primary
"""
if __name__ == '__main__':
    URL = input('宝贝链接：')
    buy_time = input('请输入开售时间 【2020-02-06(空格)12:55:50】')
    asyncio.run(main(URL, buy_time))