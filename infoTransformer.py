from takeInfo import filmsFile
from bs4 import BeautifulSoup 

with open(filmsFile, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

filmsNames = soup.find_all('div', class_='listProxEstreno releaseDate__item cf')

for filmName in filmsNames:
    print(filmName.text)

## Taking all film titles