from helper import *


async def main(URL, buy_time):
    browser, page = await get_window()
    # 30s登陆时间
    await page.goto('https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180')
    await asyncio.sleep(30)

    # 选款式时间10s
    await page.goto(URL)
    await asyncio.sleep(10)

    await sleep_time(buy_time)
    old_url = page.url

    #加入购物车
    while True:
        index = 0
        try:
            print(f'重试 {index}')
            # 找到“加入购物车”，点击
            await page.click('[class="btn btn-primary"]')
            break
        except:
            index += 1
            await asyncio.sleep(CLICK_FREQUENCY)

    # 等待页面跳转
    while True:
        if page.url != old_url:
            break
        await asyncio.sleep(CLICK_FREQUENCY)

    while True:
        try:
            # 找到“进入购物车”，点击
            await page.click('[class="btn btn-primary"]')
            break
        except:
            await asyncio.sleep(CLICK_FREQUENCY)
    # 付款
    await asyncio.sleep(100)
    await close_window(browser)

if __name__ == '__main__':
    URL = input('宝贝链接：\n')
    buy_time = input('请输入开售时间 【2020-02-06(空格)12:55:50】\n')
    asyncio.run(main(URL, buy_time))