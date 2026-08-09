import pandas as pd
import sqlite3

# File paths
excel_file = "data/HR_Employee_Analytics_Raw.xlsx"
database_file = "sql/hr_employee_analytics.db"

# Load the HR_Data sheet from Excel
df = pd.read_excel(
    excel_file,
    sheet_name="HR_Data"
)

# Clean column names
df.columns = df.columns.str.strip()

# Connect to SQLite database
connection = sqlite3.connect(database_file)

# Create HR_Data table
df.to_sql(
    "HR_Data",
    connection,
    if_exists="replace",
    index=False
)

# Check number of records
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM HR_Data")
employee_count = cursor.fetchone()[0]

print("===== HR DATABASE CREATED =====")
print("Employees loaded:", employee_count)
print("Database:", database_file)
print("Table: HR_Data")

connection.close()

print("===== DATABASE SETUP COMPLETED =====")