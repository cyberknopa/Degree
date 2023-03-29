from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import requests
import pandas as pd

data_lenta_im = pd.read_csv("Lenta_img_clean.csv")
print(data_lenta_im.head())
links = []
a=0
links = data_lenta_im["Column1"]
for i in range(0, len(links)):
 img_data = requests.get(links[i]).content
 with open(str(a) + '.jpg', 'wb') as handler:
    handler.write(img_data)
    i = i + 1
    a = a + 1