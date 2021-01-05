import asyncio
import datetime

from pyppeteer import launch

WIDTH, HEGHT = 1200, 768
BEFORE_SECOND = 2  # 提前2秒开始循环点击
CLICK_FREQUENCY = 0.1  # 点击频率


def get_start_time(buy_time):
    buy_time = buy_time if buy_time else datetime.datetime.now()
    if isinstance(buy_time, str):
        buy_time = datetime.datetime.strptime(
            buy_time, '%Y-%m-%d %H:%M:%S')
    # 如果开抢时间大于当前时间，time.sleep(), 否则直接开抢
    wait_second = (buy_time - datetime.datetime.now()).seconds if \
        (buy_time - datetime.datetime.now()).days >= 0 else 0
    return wait_second


async def get_window():
    # 开启浏览器
    browser = await launch(headless=False)
    content = await browser.createIncognitoBrowserContext()
    page = await content.newPage()
    await page.setViewport({'width': WIDTH, 'height': HEGHT})
    return browser, page


async def sleep_time(buy_time):
    # 等待时间
    wait_second = get_start_time(buy_time)
    print(f'等待{wait_second}s')
    if wait_second - BEFORE_SECOND > 0:
        await asyncio.sleep(wait_second)


async def close_window(browser):
    # 关闭浏览器
    await browser.close()

