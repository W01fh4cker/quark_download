print("""
@Author:w01f
@repo:https://github.com/W01fh4cker/quark_download/
@version 1.0
@2022/4/7
___          ______          ___        ________         ____          _______
\  \        /  __  \        /  /      /   ____  \       |   |         /  ____/
 \  \      /  /  \  \      /  /       |  |   |  |       |   |     __/   /___
  \  \    /  /    \  \    /  /        |  |   |  |       |   |    /___   ___/
   \  \  /  /      \  \  /  /         |  |   |  |       |   |       |  |
    \  \/  /        \  \/  /          |  |___|  |       |   |       |  |
     \____/          \____/           \ ________/       |___|       |__|
""")
import json
import time
import requests
import os
import time
import pycurl
import certifi
url_wait = input("请输入您需要解析的夸克网盘地址：")
save_path = input("请输入您想保存的绝对地址：")
def resolution_url_query():
    url_result = "http://www.52api.cc/pan_quark/api.php?url=" + str(url_wait)
    print(url_result)
    headers = {
        'Connection': 'keep-alive',
        # 'Host': 'dl-pc-sz.drive.quark.cn',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Referer': 'http://pan.quark.cn/'
        }
    resp = requests.get(url=url_result, headers=headers)
    global res
    res = json.loads(resp.content.decode('utf-8'))
    print(res)
    code = res["code"]
    if(code==404):
        print("解析失败，请检查您的链接！")
    else:
        global download_url,filename,filesize
        download_url = res["data"][0]["file_download_url"]
        filename = res["data"][0]["file_name"]
        filesize = res["data"][0]["file_size"]
        print(download_url)
        if download_url is None:
            print("下载链接解析失败，请联系作者邮箱sharecat2022@gmail.com")
        else:
            print("下载文件名为：" + filename + "，下载文件大小为：" + filesize)
            c = pycurl.Curl()
            c.setopt(pycurl.CAINFO, certifi.where())
            c.setopt(pycurl.HTTPHEADER,["Referer: https://pan.quark.cn/","User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36","Host:dl-pc-zb.drive.quark.cn","Cookie:这里填入你的cookie","Connection:keep-alive","Sec-Fetch-Dest:iframe","Sec-Fetch-Mode:navigate","Sec-Fetch-Site:same-site","Upgrade-Insecure-Requests:1"])
            c.setopt(pycurl.URL, download_url)
            c.perform()

if __name__ == '__main__':
    resolution_url_query()
