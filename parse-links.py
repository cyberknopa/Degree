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
df = pd.read_csv("panorama-economics.csv")
data = df["links"]

f = open('fake-eco.csv', 'w')
writer = csv.writer(f)
for i in range(0, len(data)):
    html_page = urllib.request.urlopen(data[i])
    soup = BeautifulSoup(html_page, features="html.parser")
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    print(i)
    writer.writerow(images)