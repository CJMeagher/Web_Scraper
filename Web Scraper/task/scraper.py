import os.path
import string

import requests

from bs4 import BeautifulSoup

URL_DOMAIN = 'https://www.nature.com'
URL_ARTICLES_PATH = '/nature/articles?sort=PubDate&year=2020&page='


def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.HTTPError:
        print(f'The URL returned {response.status_code}!')


def get_titles_links(soup, article_type):
    articles = soup.find_all('article')
    titles_links = []
    for article in articles:
        span = article.find('span', {'data-test': 'article.type'})
        if span and span.span.contents[0] == article_type:
            titles_links.append((article.a.text, article.a.get('href')))
    return titles_links


def get_article_body(soup):
    body_div = soup.find('div', {'class': 'c-article-body'})
    return body_div.text.strip() if body_div else ''


def create_file_name(title):
    return str.translate(title, str.maketrans(' ', '_', string.punctuation))


def do_one_page():
    pass


def main():
    pages = int(input())
    article_type = input()
    for page in range(1, pages + 1):
        articles_soup = get_soup(f'{URL_DOMAIN}{URL_ARTICLES_PATH}{page}')
        titles_links = get_titles_links(articles_soup, article_type)
        article_dir = f'Page_{page}'
        if not os.path.isdir(article_dir):
            os.mkdir(article_dir)
        for title, link in titles_links:
            file_name = create_file_name(title)
            article_soup = get_soup(URL_DOMAIN + link)
            article_body = get_article_body(article_soup)
            with open(f'{article_dir}\\{file_name}', 'wb') as article_txt:
                article_txt.write(article_body.encode('utf-8'))
                print(f'{article_dir}\\{file_name}: {URL_DOMAIN + link}')


if __name__ == "__main__":
    main()
