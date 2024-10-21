import requests
from bs4 import BeautifulSoup


response = requests.get("https://books.toscrape.com/")

content = response.content

site = BeautifulSoup(content, "html.parser")

post = site.find("li", attrs={"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

dado = post.find("a", attrs={"title": "A Light in the Attic"})
print(dado)

