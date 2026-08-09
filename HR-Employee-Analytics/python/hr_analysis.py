import pandas as pd

# Load HR dataset
file_path = "data/HR_Employee_Analytics_Raw.xlsx"
df = pd.read_excel(file_path, sheet_name="HR_Data")
df.columns = df.columns.str.strip()

# Basic information
print("===== HR EMPLOYEE ANALYTICS =====")
print("\nDataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

# Data quality checks
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Basic statistics
print("\n===== BASIC STATISTICS =====")
print(df.describe())

# HR KPIs
total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
attrition_rate = (employees_left / total_employees) * 100
average_income = df["Monthly_Income"].mean()
average_years = df["Years_At_Company"].mean()

print("\n===== HR KPIs =====")
print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print(f"Attrition Rate: {attrition_rate:.2f}%")
print(f"Average Monthly Income: {average_income:.2f}")
print(f"Average Years at Company: {average_years:.2f}")

# Attrition by Department
print("\n===== ATTRITION BY DEPARTMENT =====")
department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)
print(department_attrition)

# Attrition by Job Role
print("\n===== ATTRITION BY JOB ROLE =====")
role_attrition = pd.crosstab(
    df["Job_Role"],
    df["Attrition"]
)
print(role_attrition)

# Attrition by Overtime
print("\n===== ATTRITION BY OVERTIME =====")
overtime_attrition = pd.crosstab(
    df["Overtime"],
    df["Attrition"]
)
print(overtime_attrition)

# Create Age Groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[19, 29, 39, 49, 59],
    labels=["20-29", "30-39", "40-49", "50-59"]
)

print("\n===== ATTRITION BY AGE GROUP =====")
age_attrition = pd.crosstab(
    df["Age_Group"],
    df["Attrition"]
)
print(age_attrition)

# Average income by department
print("\n===== AVERAGE INCOME BY DEPARTMENT =====")
income_department = (
    df.groupby("Department")["Monthly_Income"]
    .mean()
    .sort_values(ascending=False)
)

print(income_department)

print("\n===== ANALYSIS COMPLETED =====")

import matplotlib.pyplot as plt

# 1. Attrition by Department
department_attrition.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Employee Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/attrition_by_department_python.png")
plt.show()


# 2. Attrition by Overtime
overtime_attrition.plot(
    kind="bar",
    figsize=(7, 5)
)

plt.title("Employee Attrition by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/attrition_by_overtime_python.png")
plt.show()


# 3. Average Income by Department
income_department.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/average_income_by_department_python.png")
plt.show()

print("\n===== PYTHON VISUALIZATION COMPLETED =====")