import requests
import html5lib
import json
import csv
from bs4 import BeautifulSoup

def list_of_tags(tags):
    related_tags = []
    for el in tags:
        url = "https://www.instagram.com/explore/tags/"+ el +"/?__a=1"
        req = requests.get(url)
        data = json.loads(req.text)
        edges = data['graphql']['hashtag']['edge_hashtag_to_related_tags']['edges']
        for item in edges:
            related_tags.append(item['node']['name'])
        print(el, len(set(related_tags)))


URL = "https://www.all-hashtag.com/top-hashtags.php"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
temp = []
tags = []
table = soup.findAll('span', attrs = {'class' : 'hashtag'})

for d in table:
    temp.append(d.text.split("#")[1:])
tags = sum(temp, [])

list_of_tags(tags)

