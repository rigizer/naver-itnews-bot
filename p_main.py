#-*- coding: utf-8 -*-

from crawler import naver_itnews_crawl
from bot import send_message

def main():
    list_data = naver_itnews_crawl()

    title_list = list_data[0]
    url_list = list_data[1]
    info_list = list_data[2]

    send_message(title_list, url_list, info_list)

if __name__ == "__main__":
    main()