# 此脚本可直接运行
import requests
import json
import re
import time
import pandas as pd
url = 'https://billing.virmach.com/modules/addons/blackfriday/new_plan.json'
dic_ori = {}


def get_location(locate):
    if "CA" in locate:
        return 1
    elif "NY" in locate:
        return 2
    elif "GA" in locate:
        return 3
    elif "NJ" in locate:
        return 4
    elif "TX" in locate:
        return 5
    elif "WA" in locate:
        return 6
    elif "IL" in locate:
        return 7


def format_print(jpd, price):

    model = pd.Series([2.44111567e-01, 2.46369652e-01, 5.93846195e+00, -
                       6.07453703e+00, 2.12034498e-03, 6.35691925e-04])
    predicted_price = sum(model*j_pd)
    print(predicted_price)
    if predicted_price > float(price):
        print("当前价格：{}\n比预测{}低".format(price, predicted_price))
    else:
        print("当前价格：{}\n比预测{}高".format(price, predicted_price))


json_text = requests.get(url).text
dic = json.loads(json_text)
pf = '''
当前套餐:
LOCATION地点： {}
CPU CPU:{} vCORE
HDD 硬盘：{}GB SSD (RAID 10)
BANDWIDTH月流量： {} GB/月
RAM内存： {}MB RAM
IPs IP数：{} DEDICATED IPv4'''.format(dic["location"], int(dic["cpu"]), int(dic["hdd"]), int(dic["bw"]), int(dic["ram"]), int(dic["ips"]))
print(pf)
while True:
    #    try:
    json_text = requests.get(url).text
    s += 1
    time.sleep(3)
    dic = json.loads(json_text)
   # print(dic)
    pp = r"\d+.\d+"

    j_pd = [get_location(dic["location"]), int(dic["hdd"]), int(
        dic["cpu"]), int(dic["ips"]), int(dic["ram"]), int(dic["bw"])]
    pf = '''
当前套餐:
LOCATION地点： {}
CPU CPU:{} vCORE
HDD 硬盘：{}GB SSD (RAID 10)
BANDWIDTH月流量： {} GB/月
RAM内存： {}MB RAM
IPs IP数：{} DEDICATED IPv4'''.format(dic["location"], int(dic["cpu"]), int(dic["hdd"]), int(dic["bw"]), int(dic["ram"]), int(dic["ips"]))

    price = re.findall(pp, str(dic["price"]))
    if price == []:

        continue
    price = price[0]
    # print(price)
    if dic != dic_ori:
        print(pf)
        format_print(j_pd, price)
        dic_ori = dic


#    except:
#        print("unexpected error")
