from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
data_lenta = pd.read_csv("2.csv")
print(data_lenta.head())
links_lenta=[]
data_lenta.info()
links_lenta = data_lenta["link"]
f = open('dni_clean-2.csv', 'w')
writer = csv.writer(f)
for i in range(0,len(links_lenta)):
   current_page = 1
   url = links_lenta[i]
   req = requests.get(url)
   page_content = BeautifulSoup(req.content, 'html.parser')
   post_url = links_lenta[i]
   post_req = requests.get(post_url)
   post = BeautifulSoup(post_req.content, 'html.parser')
   post_title = post.find("h1").get_text()
   post_content = post.find("div", attrs={"class": "article__text"})
   if post_content is None:
      post_content = "none"
   else:
      for t in post_content.findAll('p'):
         post_text =[]
         post_text = t.text
   writer.writerow([post_text, '+', post_url, '+', post_title])
   print(i)
