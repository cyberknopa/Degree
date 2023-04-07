import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://lenta.ru"
CATEGORIES = [
    '/rubrics/russia/',
    '/rubrics/world/',
    '/rubrics/culture/'
]
FILE_NAME = 'lenta.csv'  # Must be created prior
PAGE_PARAM = '?page='
news = []
failed_news = []
file = open('lenta.csv', 'w', encoding='utf8', newline='')
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
for category in CATEGORIES:
    current_page = 1
    url = BASE_URL + category + PAGE_PARAM + str(current_page)
    req = requests.get(url)
    while req.status_code == 200:
        page_content = BeautifulSoup(req.content, 'html.parser')
        post_urls = [BASE_URL + a['href'] for a in page_content.findAll('a', {"class": ["card-big _longgrid", "card-mini _longgrid"]})]
        for post_url in post_urls:
            post_req = requests.get(post_url)

            if post_req.status_code != 200:
                continue
            post = BeautifulSoup(post_req.content, 'html.parser')
            post_content = post.find("p", {"class": "topic-body__content-text"})
            post_title=post.find("span", {"class": "topic-body__title"})
            if post_content:
                post_content = post_content.text.replace('\n', '').replace(u'\xa0', ' ').replace('"', '“').strip()
            else:
                failed_news.append(post_url)
            print(post_url)
            writer.writerow([post_content,'+', post_url,'+', post_title])

        print(category + ", page " + str(current_page))
        current_page += 1
        url = BASE_URL + category + PAGE_PARAM + str(current_page)
        req = requests.get(url)
print(failed_news)
file.close()
