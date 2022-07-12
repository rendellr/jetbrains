import requests
import string
import os
from bs4 import BeautifulSoup

pages = int(input())
article_type = input()

base_url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020'
saved_articles = []

for i in range(1, pages + 1, 1):
    dir_name = 'Page_' + str(i)
    path = os.path.join(os.getcwd(), dir_name)
    # print(path)
    os.mkdir(dir_name)

    url = base_url + '&page=' + str(i)
    # print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        if article.find('span', class_='c-meta__type').text == article_type:
            title = article.find('a').text.replace(' ', '_').strip(string.punctuation) + '.txt'
            link = 'https://www.nature.com' + article.find('a')['href']
            # print(title, link)

            r = requests.get(link)
            news_soup = BeautifulSoup(r.content, 'html.parser')

            article_text = news_soup.find('div', class_='c-article-body u-clearfix').text.strip()
            # print(article_text)

            file = open(os.path.join(path, title), 'w', encoding='utf-8')
            file.write(article_text)
            file.close()
            saved_articles.append(title)

print(saved_articles)
