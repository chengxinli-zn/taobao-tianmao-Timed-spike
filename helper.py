import datetime

WIDTH, HEGHT = 1200, 768
BEFORE_SECOND = 2  # 提前2秒开始循环点击
CLICK_FREQUENCY = 0.3  # 点击频率


def get_start_time(buy_time):
    buy_time = buy_time if buy_time else datetime.datetime.now()
    if isinstance(buy_time, str):
        buy_time = datetime.datetime.strptime(
            buy_time, '%Y-%m-%d %H:%M:%S')
    # 如果开抢时间大于当前时间，time.sleep(), 否则直接开抢
    wait_second = (buy_time - datetime.datetime.now()).seconds if \
        (buy_time - datetime.datetime.now()).days >= 0 else 0
    return wait_second