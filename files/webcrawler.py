#Remember to install Requests and BeautifulSoup prior to first run.
#Note - still have to find out how to push it to the test page

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        print("Copying adress")
	url = "https://thenewboston.com/videos.php?cat=98&video=20144" #+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        print("Ready the soup")
	soup = BeautifulSoup(plain_text)
	print("Run the machine")
        for link in soup.findAll("a", {"class": "title"}):
	    href = link.get("href")
	    print(href)
	    #print("page")
	page = 2 #kunstigt sat stopklods
trade_spider(1)

def get_single_item_data(item_url):
    source_code = request.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll("a", {"class": "i-name"}):
        print(item_name.string)
    
