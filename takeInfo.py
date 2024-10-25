import requests
from bs4 import BeautifulSoup

URL ="https://yelmocines.es/proximos-estrenos"
page = requests.get(URL).text
filmsFile = "filmsFile.html"
soup = BeautifulSoup(page, "html.parser")
results = soup.find('div', class_='col10')

with open(filmsFile, 'w' ,encoding='utf-8') as file: #Sending news to webpageContentFile
        try:
            file.write(results.prettify())
        except Exception as err:
            file.write('An ERROR occurred: '+ str(err)+ '\n')