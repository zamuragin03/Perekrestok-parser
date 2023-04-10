from bs4 import BeautifulSoup
import json


class Parser:

    def __init__(self, FILE_PATH):
        self.path = FILE_PATH

    def parse(self):
        f = open(self.path, 'r')
        html = f.read()
        f.close()
        soup = BeautifulSoup(html, 'html.parser')
        products = soup.findAll(class_="swiper-slide")
        d = []
        for product in products:
            name = product.find(class_="product-card__title")
            price = product.find(class_="price-new")
            if name is not None:
                new_price = price.text.replace(u'\xa0₽', '').replace(' ', '').replace(u',', '.')
                d.append({'name': name.text, 'price': float(new_price)})
        return d

    def save(self):
        with open('parse.json', 'w') as outfile:
            json.dump(self.parse(), outfile, ensure_ascii=False)
