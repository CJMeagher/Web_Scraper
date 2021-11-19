import requests

from bs4 import BeautifulSoup


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')


def search_soup(soup, word):
    paragraphs = soup('p')
    for paragraph in paragraphs:
        if word in paragraph.text:
            return paragraph.text
    return ''


def main():
    word = input()
    url = input()
    soup = get_soup(url)
    print(search_soup(soup, word))


if __name__ == "__main__":
    main()
