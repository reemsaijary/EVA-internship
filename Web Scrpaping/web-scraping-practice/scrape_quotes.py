# Import library to send requests to websites
import requests

# Import BeautifulSoup to read and extract HTML data
from bs4 import BeautifulSoup

# Import pandas to organize data and save CSV files
import pandas as pd


# Store the website link inside a variable
url = "https://quotes.toscrape.com"


# Send request to the website and get its HTML content
response = requests.get(url)


# Parse and organize the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")


# Create an empty list to store scraped data
quotes_data = []


# Find all div elements that contain quotes
quotes = soup.find_all("div", class_="quote")


# Loop through every quote block
for quote in quotes:

    # Extract the quote text
    text = quote.find("span", class_="text").text

    # Extract the author name
    author = quote.find("small", class_="author").text


    # Add the extracted data into the list
    quotes_data.append({
        "Quote": text,
        "Author": author
    })


# Convert the list into a table (DataFrame)
df = pd.DataFrame(quotes_data)


# Save the table into a CSV file
df.to_csv("quotes.csv", index=False)


# Print success message
print("Done! Data saved to quotes.csv")