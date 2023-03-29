from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import requests
import pandas as pd

data_lenta = pd.read_csv("lenta.csv")
print(data_lenta.head())
links_lenta=[]
links_lenta = data_lenta["Column2"].str[:-2]
print(links_lenta[0])



f = open('lenta_im.csv', 'w')
writer = csv.writer(f)
for i in range(0, len(links_lenta)):
    html_page = urllib.request.urlopen(links_lenta[i])
    soup = BeautifulSoup(html_page, features="html.parser")
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    i = i + 1
    print(images)
    writer.writerow(images)