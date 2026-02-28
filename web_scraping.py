import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")

titles = []
prices_inr = []
ratings = []
availability_list = []

conversion_rate = 105  # 1 Pound = 105 INR (approx)

books = soup.find_all("article", class_="product_pod")

for book in books:
    # Title
    title = book.h3.a["title"]
    titles.append(title)

    # Price (remove £ symbol and convert)
    price_text = book.find("p", class_="price_color").text.strip()

# Remove unwanted characters
    price_clean = price_text.replace("Â£", "").replace("£", "")

    price_pound = float(price_clean)
    price_rupees = round(price_pound * conversion_rate, 2)
    prices_inr.append(price_rupees)

    # Rating
    rating = book.find("p")["class"][1]
    ratings.append(rating)

    # Availability
    availability = book.find("p", class_="instock availability").text.strip()
    availability_list.append(availability)

df = pd.DataFrame({
    "Title": titles,
    "Price (INR ₹)": prices_inr,
    "Rating": ratings,
    "Availability": availability_list
})

df.to_csv("books_data_inr.csv", index=False)

print("Data Scraped & Converted Successfully ✅")
print(df.head())
