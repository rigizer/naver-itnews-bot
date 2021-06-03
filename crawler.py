#-*- coding: utf-8 -*-

import requests                     # pip install requests
from bs4 import BeautifulSoup       # pip install beautifulsoup4

naver_itnews_url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"

header_info = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

def get_raw_content():
    document = requests.get(naver_itnews_url, headers=header_info)
    soup = BeautifulSoup(document.text, 'html.parser')

    content = soup.find(id="main_content")
    return content

def return_list(title_list, url_list, info_list):
    r_list = []
    r_list.append(title_list)
    r_list.append(url_list)
    r_list.append(info_list)

    return r_list

def naver_itnews_crawl():
    title_list = []     # 기사 제목
    url_list = []       # 기사 URL
    info_list = []      # 오류 메세지 목록

    try:
        content = get_raw_content()

        content_list = content.select("div.list_body > div._persist > div.cluster > div.cluster_group > div.cluster_body > ul.cluster_list > li.cluster_item:not(.as_line)")

        if len(content_list) == 0:
            info_list.append("Error: 사이트 파싱구조 변경!")
        else:
            for c_index in content_list:
                i_title = c_index.select("div.cluster_text > a")[0].get_text()
                i_url = c_index.select("div.cluster_text > a")[0].attrs["href"]

                title_list.append(i_title)
                url_list.append(i_url)
    except Exception as e:
        info_list.append("Error:", e)

    return return_list(title_list, url_list, info_list)