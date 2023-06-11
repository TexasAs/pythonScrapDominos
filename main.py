import json
import requests
from bs4 import BeautifulSoup

def get_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    url = "https://www.dominos.by/discount_campaign"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    list_title = []
    list_news = []
    list_link = []
    title_news = soup.find_all("div", class_="info-card__content-title")
    for i in title_news:
        list_title.append(i.text)
    text_news = soup.find_all("div", class_="info-card__content-description")
    for i in text_news:
        list_news.append(i.text)

    link_news = soup.find_all("div", class_="info-card__media-wrapper")
    for i in link_news:
       string_url = '"' + (str(i).split("=")[-1][:-2])[22:][:-7] + '"'
       list_link.append(string_url)

    dict_news = {}

    for i in range(len(list_title)):
        dict_news[list_title[i]] = {
            "news": list_news[i],
            "link_image": list_link[i]
        }

    with open("news.json", "w") as file:
        json.dump(dict_news, file, indent=4, ensure_ascii=False)


def get_pizza():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    url = "https://www.dominos.by/pizza"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    list_name = []
    list_cosht = []
    list_consist = []
    list_image = []
    dict_pizza = {}

    name_pizza = soup.find_all("div", class_="product-card__title")
    for i in name_pizza:
        list_name.append(i.text)
    cosht_pizza = soup.find_all("span", class_="product-card__min-price")
    for i in cosht_pizza:
        list_cosht.append(i.text)
    consist_pizza = soup.find_all("div", class_="product-card__description")
    for i in consist_pizza:
        list_consist.append(i.text)
    image_pizza = soup.find_all("img", class_="media-image__element product-card-media__element")
    for i in image_pizza:
        list_image.append(str(i).split('=')[-1][:-2])

    for i in range(len(list_name)):
        dict_pizza[list_name[i]] = {
            "name": list_name[i],
            "consist": list_consist[i],
            "image": list_image[i],
            "cosht": list_cosht[i]
        }

    with open("pizza.json", "w") as file:
        json.dump(dict_pizza, file, indent=4, ensure_ascii=False)

def main():
    get_news()
    get_pizza()


if __name__ == "__main__":
    main()
