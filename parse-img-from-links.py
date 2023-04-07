from bs4 import BeautifulSoup
import csv
import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import requests

data = []
images = []
df = pd.read_excel("img-links.xlsx")
data = df["true-rus"]

f = open('im.csv', 'w')
writer = csv.writer(f)
"""
for i in range(0, len(data)):
    req = Request(url=data[i], headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, features="html.parser")
    images.append(soup.findAll('div', class_='picture__image-wrap'))
    f.write(str(images[i])+'+')
    print(i)
"""
"""
for i in range(0, len(data)):
    html_page = urllib.request.urlopen(data[i])
    soup = BeautifulSoup(html_page, features="html.parser")
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    print(i)
    writer.writerow(images)

"""

links = []
links= df["img-true-rus"]

a=0
for i in range(0, len(links )):
    img_data = requests.get(links [i]).content
    with open(str(a) + '.jpg', 'wb') as handler:
        handler.write(img_data)
        a = a + 1
    print(i)
