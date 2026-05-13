# Import library to send requests to websites
import requests

# Import BeautifulSoup to read and extract HTML data
from bs4 import BeautifulSoup

# Import pandas to organize data and save CSV files
import pandas as pd

# Store the website link inside a variable
url = "https://books.toscrape.com/"

# Send request to the website and get its HTML content
response = requests.get(url)

# Parse and organize the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Create an empty list to store scraped data
books_data = []

# Find all repeated book containers
books = soup.find_all("article", class_="product_pod")


# Loop through every book
for book in books:

    # Extract book title
    title = book.find("h3").find("a").get("title")

    # Extract book price
    price = book.find("p", class_="price_color").text

    # Extract stock availability
    availability = book.find("p", class_="instock availability").text.strip()

    # Extract star rating
    rating = book.find("p", class_="star-rating")["class"][1]


    # Add extracted data into the list
    books_data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating
    })

# Convert data into a table
df = pd.DataFrame(books_data)

# Save data into CSV file
df.to_csv("books.csv", index=False)

# Print success message
print("Done! Books data saved to books.csv")