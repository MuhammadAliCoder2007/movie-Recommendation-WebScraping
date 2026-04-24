from bs4 import BeautifulSoup
import requests

page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.text, "html.parser")
print(page.status_code)