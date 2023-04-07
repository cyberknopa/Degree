from bs4 import BeautifulSoup
import csv
import pandas as pd
from urllib.request import Request, urlopen
import urllib.request
import re
import requests

data = []
images = []
df = pd.read_csv("panorama-sscience.csv")
data = df["link"]

f = open('fake-science.csv', 'w')
writer = csv.writer(f)
for i in range(0, len(data)):
    req = Request(url=data[i], headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, features="html.parser")
    images.append(soup.findAll('div', class_='container mx-auto h-[250px] md:h-[325px] lg:h-[400px] bg-cover lg:bg-contain bg-no-repeat bg-left-top'))
    f.write(str(images[i])+'+')
    print(i)
