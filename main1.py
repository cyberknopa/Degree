import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://panorama.pub"
CATEGORIES = [
    '/politics',
    '/society',
    '/science',
    '/economics',
]
FILE_NAME = 'panorama.csv'  # Must be created prior
PAGE_PARAM = '?page='
news = []
failed_news = []
file = open('panorama.csv', 'w', encoding='utf8', newline='')
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
for category in CATEGORIES:
    current_page = 1
    url = BASE_URL + category + PAGE_PARAM + str(current_page)
    req = requests.get(url)
    while req.status_code == 200:
        page_content = BeautifulSoup(req.content, 'html.parser')
        post_urls = [BASE_URL + a['href'] for a in page_content.findAll('a', {"class": ["rounded-md", "hover:text-secondary"]})]
        for post_url in post_urls:
            post_req = requests.get(post_url)

            if post_req.status_code != 200:
                continue
            post = BeautifulSoup(post_req.content, 'html.parser')
            post_content = post.find("div", {"class": "entry-contents"})
            post_title = post.find('h1',{'class':'font-bold text-2xl md:text-3xl lg:text-4xl pl-1 pr-2 self-center'})
            if post_content:
                post_content = post_content.text.replace('\n', '').replace(u'\xa0', ' ').replace('"', '“').strip()
            else:
                failed_news.append(post_url)
            print(post_url)
            writer.writerow([post_content,'+', post_url, '+', post_title])

        print(category + ", page " + str(current_page))
        current_page += 1
        url = BASE_URL + category + PAGE_PARAM + str(current_page)
        req = requests.get(url)
print(failed_news)
file.close()

