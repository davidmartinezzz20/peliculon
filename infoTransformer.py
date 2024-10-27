from takeInfo import filmsFile
from bs4 import BeautifulSoup

URL="https://yelmocines.es"

with open(filmsFile, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

filmsInfo = soup.find_all('article', class_='releaseDate')
#filmsDates = soup.find_all('h3', class_='releaseDay')

d = []

for filmInfo in filmsInfo:

    # Taking movie name, synopsis href and release date
    filmName = filmInfo.find('figcaption').text.strip()
    filmHref = filmInfo.find('a', href=True)
    filmHref = URL+filmHref['href']
    filmImage = filmInfo.find('img', src=True).get("src")
    filmDate = filmInfo.find('h3', class_='releaseDay').text.strip().replace("\n","")
    filmDate = filmDate.split(" ")
    filmDate = list(filter(None, filmDate))
    filmDate = ' '.join(filmDate)
    
    # Write each movie to a list
    line = {'Name':filmName, 'URL':filmHref, 'Release date':filmDate, 'Image':filmImage}
    d.append(line)