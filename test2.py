import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
url = "https://www.dominos.by/discount_campaign"
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")

top_pizzas = soup.find_all("div", class_="product-card__title")
for i in  top_pizzas:
    print(top_pizzas[1])
    #list_name.append(i.text)
    
def top(**name):
	for k, v in name.items():
		print(k, v)
		
top(t1='piperoni', t2='salami', t3='chet escho')