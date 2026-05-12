import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load database connection string from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Read CSV file
df = pd.read_csv("leads.csv")

# Connect to Supabase PostgreSQL
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Insert each row from CSV into imported_leads table
for index, row in df.iterrows():
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
        row["company_name"],
        row["contact_name"],
        row["email"],
        row["phone"],
        row["industry"],
        row["country"],
        row["lead_status"],
        row["notes"]
    ))

# Save all inserts
connection.commit()

print("CSV data imported successfully!")

# Close connection
cursor.close()
connection.close()