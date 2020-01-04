import os
import requests
import re
import bs4
# post url: https://www.taifex.com.tw/cht/3/dlOptDataDown
#  get url: https://www.taifex.com.tw/cht/3/dlOptDailyMarketView
want_fetch_url = 'https://www.taifex.com.tw/cht/3/dlOptDataDown'
download_folder_path = './test/'   # file download place
output_file_name = input("請輸入檔案名稱: ") + ".csv"


def fetch_url_content(_url):
    html = requests.get(_url).content
    return bs4.BeautifulSoup(html, 'lxml')


def post_url(_url, _data):
    _response = requests.post(_url, _data).content
    return _response


def check_folder_exist(_destination_folder: str):
    if not os.path.exists(_destination_folder):
        os.makedirs(_destination_folder)  # create folder if it does not exist
    return


def is_file_exist(_filename: str):
    if _filename in os.listdir(download_folder_path):
        return False
    else:
        return False


def output_file(_filename: str, _data: str):
    with open(_filename, 'w') as fp:
        fp.writelines(_data)
        # print(_data)
        # fp.write(_data)
        # print(_data, file=fp)
    return


data = {
    "down_type": 1,
    "commodity_id": "TXO",
    "commodity_id2": "",
    "queryStartDate": input("日期(起)："),
    "queryEndDate": input("日期(迄)：")
}

# print(data)
response = post_url(want_fetch_url, data).decode('big5')
# print(response.decode("big5"))
output_file(download_folder_path + output_file_name, response)


