import requests
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'Python', 'физика', 'программирование']

HEADERS = Headers(os="mac", headers=True).generate()
base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
articles_list = []

for article in articles:
    preview_title = article.findAll(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    preview_title = [pre_title.text.strip() for pre_title in preview_title]
    for title in preview_title:
        title = title.split()
        for word in title:
            if word in KEYWORDS:
                date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                title = article.find('h2').find('span').text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = base_url + href
                correct_article = f'{date} / {title} => {link}'
                articles_list.append(correct_article)
    preview_hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    preview_hubs = [hub.text.strip() for hub in preview_hubs]
    for hub in preview_hubs:
        hub = hub.split()
        for word in hub:
            if word in KEYWORDS:
                date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                title = article.find('h2').find('span').text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = base_url + href
                correct_article = f'{date} / {title} => {link}'
                if correct_article not in articles_list:
                    articles_list.append(correct_article)
    preview_title = article.findAll(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    preview_title = [pre_title.text.strip() for pre_title in preview_title]
    for title in preview_title:
        title = title.split()
        for word in title:
            if word in KEYWORDS:
                date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                title = article.find('h2').find('span').text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                link = base_url + href
                correct_article = f'{date} / {title} => {link}'
                if correct_article not in articles_list:
                    articles_list.append(correct_article)

if __name__ == '__main__':
    for i in articles_list:
        print(i)
