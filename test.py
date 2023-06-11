import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver

#def get_news():
#    with open("news.json") as file:
#        news_dict = json.load(file)
#    for k, v in news_dict.items():
#        news = f"{v['news']}\n<a href={v['ssylka'][21:]}>&#8203;</a>"
#        #await  message.answer(news)
#    #await message.delete()
#        print(news)
#
#get_news()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
url = "https://www.dominos.by/pizza"
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
#image_pizza = soup.find_all("img", class_="media-image__element product-card-media__element")

image_news = soup.find_all("div", class_="info-card__media-wrapper")

#<div class="info-card__media-wrapper" style="background-image:url(https://backend.dominos.by/media/dominos/discount_campaign/Lucky_kombo_%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80.png)"></div>

for i in image_news:
    #print(str(i).split('=')[-1][:-2])
    #print(str(i))
    string_url = '"' + (str(i).split("=")[-1][:-2])[22:][:-7] + '"'
    #string_url = '"' + string_url[22:][:-7] + '"'
    print(string_url)

image_pizza = soup.find_all("img", class_="media-image__element product-card-media__element")
for i in image_pizza:
    #list_image.append(str(i).split('=')[-1][:-2])
    print(str(i).split('=')[-1][:-2])

#< div
#class ="info-card__media-wrapper" style="background-image:url(https://backend.dominos.by/media/dominos/discount_campaign/Lucky_kombo_%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80.png)" > < /div >


image_news2 = soup.find_all("div", class_="info-card__media-wrapper")
for i in image_news2:
    print(str(i).split('=')[-1][:-2])
    string_url = string_url[22:][:-7]
    #print(str(i))