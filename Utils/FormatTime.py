# -*- coding:utf-8 -*-
import time
import datetime


def data_time_chinese():  # 返回中文的年月日 时分秒
    return time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime())


def data_chinses():  # 返回中文的年月日
    return time.strftime("%Y年%m月%d日", time.localtime())


def time_chinese():  # 返回中文的时分秒
    return time.strftime("%H时%M分%S秒", time.localtime())


def data_time_english():  # 返回英文的年月日时分秒
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def data_time_english_no_delimiter():  # 返回无分隔符英文的年月日时分秒
    return time.strftime("%Y%m%d-%H%M%S", time.localtime())


def data_time_string():  # 返回英文的月日时分字符串
    # type: () -> object
    return time.strftime("%m%d%H%M", time.localtime())


def data_english():  # 返回英文的年月日
    return time.strftime("%Y-%m-%d", time.localtime())


def time_english():  # 返回英文的时分秒
    return time.strftime("%H:%M:%S", time.localtime())


def minute_english():  # 返回英语的分
    return time.strftime("%M", time.localtime())


def hour_english():  # 返回英文的时
    return time.strftime("%H", time.localtime())


def tomorrow_n(day):  # 返回N天后的英文年月日
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime("%Y-%m-%d")


def yestoday_n(day):  # 返回N天前的英文年月日
    return (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%d")


def later_minute(minute):  # 返回N分钟后的英文分钟
    return (datetime.datetime.now() + datetime.timedelta(minutes=minute)).strftime("%M")


if __name__ == '__main__':
    print(data_time_chinese())
    print(data_chinses())
    print(time_chinese())

    print(data_time_english())
    print(data_time_english_no_delimiter())
    print(data_english())
    print(time_english())

    print(tomorrow_n(1))
    print(yestoday_n(2))

    print(data_time_string())

    print(minute_english())
    print(hour_english())
    print(later_minute(25))
