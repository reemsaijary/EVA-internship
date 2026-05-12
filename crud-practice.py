import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# CREATE: insert new lead
cursor.execute("""
    INSERT INTO imported_leads
    (company_name, contact_name, email, phone, industry, country, lead_status, notes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id
""", (
    "CRUD Test Company",
    "Reem Test",
    "crud@test.com",
    "+96170000000",
    "Software",
    "Lebanon",
    "New",
    "Created using CRUD practice"
))

new_id = cursor.fetchone()[0]
connection.commit()

print("Created lead with ID:", new_id)


# READ: get the lead we just inserted
cursor.execute("""
    SELECT id, company_name, contact_name, email, lead_status
    FROM imported_leads
    WHERE id = %s
""", (new_id,))
# takes that row and stores it inside lead
lead = cursor.fetchone()
print("Read lead:", lead)


# UPDATE: update lead status
cursor.execute("""
    UPDATE imported_leads
    SET lead_status = %s, notes = %s
    WHERE id = %s
""", (
    "Contacted",
    "Updated using CRUD practice",
    new_id
))

connection.commit()
print("Updated lead status to Contacted")


# READ AGAIN: confirm update
cursor.execute("""
    SELECT id, company_name, lead_status, notes
    FROM imported_leads
    WHERE id = %s
""", (new_id,))

updated_lead = cursor.fetchone()
print("After update:", updated_lead)


# DELETE: delete the test lead
cursor.execute("""
    DELETE FROM imported_leads
    WHERE id = %s
""", (new_id,))

connection.commit()
print("Deleted test lead")


cursor.close()
connection.close()