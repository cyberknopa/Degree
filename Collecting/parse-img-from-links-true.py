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



links = []
links= df["img-true-mir"]

a=0
for i in range(0, len(links )):
    img_data = requests.get(links[i]).content
    with open(str(a) + '.jpg', 'wb') as handler:
        handler.write(img_data)
        a = a + 1
    print(i)
