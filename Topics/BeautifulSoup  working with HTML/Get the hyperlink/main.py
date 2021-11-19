import requests

from bs4 import BeautifulSoup

def main():
    act = input()
    url = input()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find('a', string=f'ACT {act}')
    print(link['href'])


if __name__ == "__main__":
    main()
