from itertools import groupby
import requests
from bs4 import BeautifulSoup

class Perecrestok:      
    def __init__(self) -> None:
        self.Perecrestok_Milk = "https://spb.perekrestok.ru/cat/c/114/moloko?filter.obem-litr=s-601-ml-do-1000-ml&priceRange=37-77"
        self.Perecrestok_Cheese = "https://spb.perekrestok.ru/cat/c/122/syr?filter.fasovka=brusok&filter.tip-syra=polutverdyj&priceRange=49-559&tags=onlyDiscount"
        self.Perecrestok_Bread = "https://spb.perekrestok.ru/cat/c/243/hleb?filter.muka=psenicnaa&filter.narezka-hleb=net&orderBy=price&orderDirection=asc&priceRange=19-64"
        self.Perecrestok_Potato = "https://spb.perekrestok.ru/cat/c/150/ovosi?orderBy=price&orderDirection=asc&priceRange=23-86#kartofel-vegetables"
    
    def P_Parse_milk(self) -> list:                  # Работает!!!!
        result = []
        seen_urls = set()

        r = requests.get(self.Perecrestok_Milk)
        soup = BeautifulSoup(r.text, "html.parser")
        Stack_of_milk_cards = soup.find_all("div", class_ = "product-card-wrapper")
        
        Milk_Href = [a.get("href") for a in soup.find_all("a", class_ = "product-card__link")]
        Milk_Image = [img.get("src") for img in soup.find_all("img", class_="product-card__image")] 

        for card, href, img in zip(Stack_of_milk_cards, Milk_Href, Milk_Image):
            if [_.text for _ in card.find("div", class_ = "sc-bQdRvg hBePYa product-card__balance-badge")] == ['В наличии много']:
                Milk_text = card.find("span", class_ ="product-card__link-text")
                Milk_Price = card.find("div", class_ = "price-new")
                if href not in seen_urls:
                    result.append((
                                    [_.text for _ in Milk_text],
                                    [_.text for _ in Milk_Price],
                                    href,
                                    img
                                    ))
                    seen_urls.add(href)
        
        return [el for el, _ in groupby(result)]

    def P_Parse_cheese(self) -> list:                  # Работает!!!!
        result = []
        seen_urls = set()

        r = requests.get(self.Perecrestok_Cheese)
        soup = BeautifulSoup(r.text, "html.parser")
        Stack_of_cheese_cards = soup.find_all("div", class_ = "product-card-wrapper")

        cheese_Href = [a.get("href") for a in soup.find_all("a", class_ = "product-card__link")]
        cheese_Image = [img.get("src") for img in soup.find_all("img", class_="product-card__image")] 

        for card, href, img in zip(Stack_of_cheese_cards, cheese_Href, cheese_Image):
            if [_.text for _ in card.find("div", class_ = "sc-bQdRvg hBePYa product-card__balance-badge")] == ['В наличии много']:
                cheese_text = card.find("span", class_ ="product-card__link-text")
                cheese_Price = card.find("div", class_ = "price-new")
                if href not in seen_urls:
                    result.append((
                                    [_.text for _ in cheese_text],
                                    [_.text for _ in cheese_Price],
                                    href,
                                    img
                                    ))
                    seen_urls.add(href)
        return [el for el, _ in groupby(result)]
    
    def P_Parse_bread(self) -> list:                  # Работает!!!!
        result = []
        seen_urls = set()
        
        r = requests.get(self.Perecrestok_Bread)
        soup = BeautifulSoup(r.text, "html.parser")
        Stack_of_bread_cards = soup.find_all("div", class_ = "product-card-wrapper")

        bread_Href = [a.get("href") for a in soup.find_all("a", class_ = "product-card__link")]
        bread_Image = [img.get("src") for img in soup.find_all("img", class_="product-card__image")] 

        for card, href, img in zip(Stack_of_bread_cards, bread_Href, bread_Image):
            if [_.text for _ in card.find("div", class_ = "sc-bQdRvg hBePYa product-card__balance-badge")] == ['В наличии много']:
                bread_text = card.find("span", class_ ="product-card__link-text")
                bread_Price = card.find("div", class_ = "price-new")
                if href not in seen_urls:
                    result.append((
                                    [_.text for _ in bread_text],
                                    [_.text for _ in bread_Price],
                                    href,
                                    img
                                    ))
                    seen_urls.add(href)
        return [el for el, _ in groupby(result)]

    def P_Parse_potato(self) -> list:                 # Работает!!!!
        result = []
        seen_urls = set()
        
        r = requests.get(self.Perecrestok_Potato)
        soup = BeautifulSoup(r.text, "html.parser")
        Stack_of_potato_cards = soup.find("div", id = "kartofel-vegetables")
        
        for card in Stack_of_potato_cards.find_all("div", class_ = "product-card-wrapper"):
            stock_status = card.find("div", class_ = "sc-bQdRvg hBePYa product-card__balance-badge")
            if stock_status and stock_status.text == 'В наличии много':
                potato_text = card.find("span", class_ ="product-card__link-text")
                potato_Price = card.find("div", class_ = "price-new")
                href = card.find("a", class_ = "product-card__link").get("href")
                img = card.find("img", class_="product-card__image").get("src")
                if href not in seen_urls:
                    result.append((
                                    [_.text for _ in potato_text],
                                    [_.text for _ in potato_Price],
                                    href,
                                    img
                                    ))
                    seen_urls.add(href)
        return [el for el, _ in groupby(result)]


class SevenSteps:
    def __init__(self) -> None:
        self.SevenSteps_Milk = "https://semishagoff.org/catalog/molochnaya-produkciya/moloko-slivki/"
        self.SevenSteps_Cheese = "https://semishagoff.org/catalog/syr-maslo-yayca/syry/"
        self.SevenSteps_Bread = "https://semishagoff.org/catalog/hlebobulochnye-ideliya/hleb-baton-lavash/"
        self.SevenSteps_Potato = "https://semishagoff.org/catalog/frukty-ovoshchi/ovoshchi/filter/price-base-from-9-to-20/apply/"
    
    def S_Parse_milk(self) -> None:
        result = []
        url = self.SevenSteps_Milk
        response = requests.get(url)
        html = response.text
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Находим все элементы с классом cat-item
        cat_items = soup.find_all('div', class_='cat-item')
        # Для каждого элемента извлекаем информацию о названии, цене, ссылке на товар и ссылке на картинку
        for cat_item in cat_items:
            # Название
            title = cat_item.find('a', class_='cat-item__title').text.strip()
            # Цена
            price = cat_item.find('div', class_='price').text.strip()
            # Ссылка на товар
            product_url = cat_item.find('a', class_='cat-item__img')['href']
            # Ссылка на картинку товара
            image_url = cat_item.find('a', class_='cat-item__img').find('img')['src']
            # Выводим информацию о товаре
            result.append((
                title,
                price,
                product_url,
                image_url
            ))
        return result        
    
    def S_Parse_cheese(self) -> None:
        result = []
        url = self.SevenSteps_Cheese
        response = requests.get(url)
        html = response.text
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Находим все элементы с классом cat-item
        cat_items = soup.find_all('div', class_='cat-item')
        # Для каждого элемента извлекаем информацию о названии, цене, ссылке на товар и ссылке на картинку
        for cat_item in cat_items:
            # Название
            title = cat_item.find('a', class_='cat-item__title').text.strip()
            # Цена
            price = cat_item.find('div', class_='price').text.strip()
            # Ссылка на товар
            product_url = cat_item.find('a', class_='cat-item__img')['href']
            # Ссылка на картинку товара
            image_url = cat_item.find('a', class_='cat-item__img').find('img')['src']
            # Выводим информацию о товаре
            result.append((
                title,
                price,
                product_url,
                image_url
            ))
        return result        

    def S_Parse_bread(self) -> None:
        result = []
        url = self.SevenSteps_Bread 
        response = requests.get(url)
        html = response.text
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Находим все элементы с классом cat-item
        cat_items = soup.find_all('div', class_='cat-item')
        # Для каждого элемента извлекаем информацию о названии, цене, ссылке на товар и ссылке на картинку
        for cat_item in cat_items:
            # Название
            title = cat_item.find('a', class_='cat-item__title').text.strip()
            # Цена
            price = cat_item.find('div', class_='price').text.strip()
            # Ссылка на товар
            product_url = cat_item.find('a', class_='cat-item__img')['href']
            # Ссылка на картинку товара
            image_url = cat_item.find('a', class_='cat-item__img').find('img')['src']
            # Выводим информацию о товаре
            result.append((
                title,
                price,
                product_url,
                image_url
            ))
        return result    
    
    def S_Parse_potato(self) -> None:
        result = []
        url = self.SevenSteps_Potato
        response = requests.get(url)
        html = response.text
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Находим все элементы с классом cat-item
        cat_items = soup.find_all('div', class_='cat-item')
        # Для каждого элемента извлекаем информацию о названии, цене, ссылке на товар и ссылке на картинку
        for cat_item in cat_items:
            # Название
            title = cat_item.find('a', class_='cat-item__title').text.strip()
            # Цена
            price = cat_item.find('div', class_='price').text.strip()
            # Ссылка на товар
            product_url = cat_item.find('a', class_='cat-item__img')['href']
            # Ссылка на картинку товара
            image_url = cat_item.find('a', class_='cat-item__img').find('img')['src']
            # Выводим информацию о товаре
            result.append((
                title,
                price,
                product_url,
                image_url
            ))
        return result