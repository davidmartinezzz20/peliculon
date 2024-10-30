from takeInfo import filmsFile
from bs4 import BeautifulSoup

URL="https://yelmocines.es"

with open(filmsFile, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

filmsInfo = soup.find_all('article', class_='releaseDate')
#filmsDates = soup.find_all('h3', class_='releaseDay')

d = []
mailContent = []

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

    x = """
    <div class="box">
        <img src="""+""+filmImage+""+""" /><br/>
        <a style="color: #000000; font-size: 25px;"><b>"""+filmName+"""</b></a><br/>
        <a style="color: #000000; font-size: 15px;">Fecha de estreno: <b>"""+filmDate+"""</b></a><br/>
        <a style="color: #000000; font-size: 20px;" href="""+filmHref+">Sinopsis</a><br/>""""
    </div> 
    """
    mailContent.append(x)

print(mailContent)