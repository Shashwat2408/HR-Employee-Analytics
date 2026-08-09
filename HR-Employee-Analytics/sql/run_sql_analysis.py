import sqlite3
import pandas as pd

# Database and SQL file
database_file = "sql/hr_employee_analytics.db"
sql_file = "sql/hr_analysis_queries.sql"

# Connect to database
connection = sqlite3.connect(database_file)

# Read SQL queries
with open(sql_file, "r", encoding="utf-8") as file:
    sql_script = file.read()

print("===== SQL HR ANALYSIS =====")

# Run each query separately
queries = [
    ("Overall Employee Count", """
        SELECT COUNT(*) AS Total_Employees
        FROM HR_Data;
    """),

    ("Overall Attrition", """
        SELECT Attrition, COUNT(*) AS Employee_Count
        FROM HR_Data
        GROUP BY Attrition;
    """),

    ("Attrition by Department", """
        SELECT Department, Attrition, COUNT(*) AS Employee_Count
        FROM HR_Data
        GROUP BY Department, Attrition
        ORDER BY Department, Attrition;
    """),

    ("Attrition by Job Role", """
        SELECT Job_Role, Attrition, COUNT(*) AS Employee_Count
        FROM HR_Data
        GROUP BY Job_Role, Attrition
        ORDER BY Job_Role, Attrition;
    """),

    ("Average Income by Department", """
        SELECT Department,
               ROUND(AVG(Monthly_Income), 2) AS Average_Monthly_Income
        FROM HR_Data
        GROUP BY Department
        ORDER BY Average_Monthly_Income DESC;
    """),

    ("Attrition by Overtime", """
        SELECT Overtime, Attrition, COUNT(*) AS Employee_Count
        FROM HR_Data
        GROUP BY Overtime, Attrition
        ORDER BY Overtime, Attrition;
    """),

    ("Average Job Satisfaction by Department", """
        SELECT Department,
               ROUND(AVG(Job_Satisfaction), 2) AS Average_Job_Satisfaction
        FROM HR_Data
        GROUP BY Department
        ORDER BY Average_Job_Satisfaction DESC;
    """),

    ("Attrition by Age Group", """
        SELECT Age_Group, Attrition, COUNT(*) AS Employee_Count
        FROM HR_Data
        GROUP BY Age_Group, Attrition
        ORDER BY Age_Group, Attrition;
    """),

    ("Average Performance by Department", """
        SELECT Department,
               ROUND(AVG(Performance_Rating), 2) AS Average_Performance_Rating
        FROM HR_Data
        GROUP BY Department
        ORDER BY Average_Performance_Rating DESC;
    """)
]

# Execute queries
for title, query in queries:
    print(f"\n===== {title.upper()} =====")

    result = pd.read_sql_query(query, connection)

    print(result.to_string(index=False))

    # Save result as CSV
    filename = title.lower().replace(" ", "_") + ".csv"
    result.to_csv(f"reports/{filename}", index=False)

connection.close()

print("\n===== SQL ANALYSIS COMPLETED =====")