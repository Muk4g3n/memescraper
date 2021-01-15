import requests
from bs4 import BeautifulSoup

URL = 'https://www.reddit.com/r/memes/top/?t=all'
headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
imgs = soup.find_all('img')
i = 0
for img in imgs:

    link = img['src']
    with open('./memes/meme' + str(i) + '.jpg', 'wb') as file:
        im = requests.get(link)
        file.write(im.content)
    i = i + 1
