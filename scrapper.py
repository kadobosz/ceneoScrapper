import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.ceneo.pl/71299209#tab=reviews')

page_dom = BeautifulSoup(response.text, "html.parser")

reviews = page_dom.select("div.js_product-review")

review = reviews.pop(0)

review_id = review["data-entry-id"]
author = review.select_one("span.user-post__author-name").text.strip()
recommendation = review.select_one("span.user-post__author-recomendation").text.strip()
stars = review.select_one("span.user-post__score-count").text.strip()
content = review.select_one("div.user-post__text").text.strip()
pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
useful = review.select_one("button.vote-yes > span").text.strip() 
useless = review.select_one("button.vote-no > span").text.strip()
purchased = review.select_one("div.review-pz").text.strip() 
review_date = review.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
purchase_date = review.select_one("span.user-post__published > time:nth-child(2)")["datetime"]

print(review_id,author,recommendation,stars,content,pros,cons,useful,useless,purchased,review_date,purchase_date)