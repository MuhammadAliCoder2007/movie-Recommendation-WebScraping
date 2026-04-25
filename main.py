from bs4 import BeautifulSoup
import requests
import random

recommended = []

strToNum = {
    "One":1,
    "Two": 2,
    "Three":3,
    "Four":4,
    "Five":5
}
min_rating = int(input("Enter minmun rated book you want: (1-5)\n"))

page = requests.get("https://books.toscrape.com/") #get the web
soup = BeautifulSoup(page.text, "html.parser") #

books = {}

for book in soup.find_all('article', class_ = "product_pod"): #goes thorugh each book
    title = book.h3.a['title']
    rating = book.p['class'][1]
    numRating = strToNum[rating]
    books[title] = numRating


for title, rating in books.items():
    if rating>=min_rating:
        recommended.append((title ,rating))
        
print(random.choice(recommended))