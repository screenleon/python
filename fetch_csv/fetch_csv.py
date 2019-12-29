import os

import requests
import re
import bs4

want_fetch_url = 'https://www.taifex.com.tw/cht/3/dlOptPrevious30DaysSalesData'
download_folder_path = 'E:\\github\\python\\fetch_csv\\test'   # file download place


def fetch_url_content(_url):
    html = requests.get(_url).content
    return bs4.BeautifulSoup(html, 'lxml')


def check_folder_exist(_destination_folder: str):
    if not os.path.exists(_destination_folder):
        os.makedirs(_destination_folder)  # create folder if it does not exist
    return


def download(_url: str, _destination_folder: str):
    filename = _url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(_destination_folder, filename)
    if filename in os.listdir(_destination_folder):
        print("exist file name", filename)
        return
    r = requests.get(_url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


def is_file_exist(_filename: str):
    if _filename in os.listdir(download_folder_path):
        return False
    else:
        return False


soup_html = fetch_url_content(want_fetch_url)
input_button7_elements = soup_html.find_all('input', id='button7')


for input_button7_element in input_button7_elements:
    if input_button7_element['onclick'][-3] == 'p':
        download_url = input_button7_element['onclick'][24:-2]
        if re.findall('CSV', download_url):
            download(download_url, download_folder_path)
#   print(input['onclick'][24:-2]