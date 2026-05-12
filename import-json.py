import json
import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Open JSON file
with open("leads.json", "r") as file:
    data = json.load(file)

# Connect to database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Loop through JSON data
for lead in data:

    cursor.execute("""
        INSERT INTO imported_leads (
            company_name,
            contact_name,
            email,
            phone,
            industry,
            country,
            lead_status,
            notes
        )

        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (

        lead["company_name"],
        lead["contact_name"],
        lead["email"],
        lead["phone"],
        lead["industry"],
        lead["country"],
        lead["lead_status"],
        lead["notes"]
    ))

# Save changes
connection.commit()

print("JSON data imported successfully!")

# Close connection
cursor.close()
connection.close()