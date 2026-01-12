#-*- coding: utf-8 -*-

import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

naver_itnews_url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"

header_info = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

def get_raw_content():
    document = requests.get(naver_itnews_url, headers=header_info, timeout=10)
    content = BeautifulSoup(document.text, 'html.parser')
    return content

def return_list(title_list, url_list, info_list):
    return [title_list, url_list, info_list]

def naver_itnews_crawl():
    title_list = []
    url_list = []
    info_list = []

    try:
        content = get_raw_content()

        if content is None:
            info_list.append("Error: 사이트 파싱 구조가 변경되었습니다.")
            return return_list(title_list, url_list, info_list)

        content_list = content.select(".sa_text_title")

        if not content_list:
            info_list.append("Error: 사이트 파싱 구조가 변경되었습니다.")
        else:
            for item in content_list[:10]:
                title = item.get_text(strip=True)
                url = item.get("href")

                if url and not url.startswith("http"):
                    url = f"https://news.naver.com{url}"

                title_list.append(title)
                url_list.append(url)

    except Exception as e:
        info_list.append(f"Error: {e}")

    return return_list(title_list, url_list, info_list)