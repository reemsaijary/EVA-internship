# Import libraries
import psycopg2
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get connection string from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to Supabase PostgreSQL database
connection = psycopg2.connect(DATABASE_URL)

# Create cursor to run SQL commands
cursor = connection.cursor()

# Insert data into leads table
cursor.execute("""
INSERT INTO leads 
(company_name, contact_name, email, phone, website, linkedin_url, industry, country, lead_status, notes)

VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (
    "Tech Company",
    "John Doe",
    "john@test.com",
    "123456789",
    "john.com",
    "linkedin.com/company/john",
    "Software",
    "USA",
    "New Lead",
    "Inserted from Python"
))

# Read data from leads table
cursor.execute("SELECT * FROM leads")

# Get all rows
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

    
# Save changes
connection.commit()

print("Lead inserted successfully!")

print("Connected successfully to Supabase!")

# Close connection
cursor.close()

#avoids memory waste,avoids too many open connections,keeps application clean
connection.close()