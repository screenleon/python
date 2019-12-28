import os

import requests
import re
import bs4

html = requests.get('https://www.taifex.com.tw/cht/3/dlOptPrevious30DaysSalesData').content

soup = bs4.BeautifulSoup(html, 'lxml')
inputs = soup.find_all('input', id='button7')
download_folder = 'E:\\project\\python\\fetch_csv\\test'   #file download place


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
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


for input in inputs:
#   print(input['onclick'][24:-2])
    if input['onclick'][-3] == 'p':
        download_url = input['onclick'][24:-2]
        if re.findall('CSV', download_url):
            file_name = download_url[-27:]
            if file_name in os.listdir(download_folder):
                continue
#           print(download_url)
#           print(file_name)
            download(download_url, download_folder)




