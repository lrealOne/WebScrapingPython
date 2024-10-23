import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("https://books.toscrape.com/")

content = response.content

site = BeautifulSoup(content, "html.parser")

section = site.find_all("li", attrs={"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

dados = []
for item in section:
    titulo = item.find("h3")
    valor = item.find("p", attrs={"class": "price_color"})
    dados.append([titulo.text, valor.text])

livros = pd.DataFrame(dados, columns=["Titulo", "Preço"])

livros.to_excel("BaseDeDadosRm.xlsx", index=False)
