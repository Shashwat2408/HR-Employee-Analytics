-- ============================================
-- HR EMPLOYEE ANALYTICS - SQL ANALYSIS
-- ============================================

-- 1. Overall employee count
SELECT
    COUNT(*) AS Total_Employees
FROM HR_Data;


-- 2. Overall attrition count
SELECT
    Attrition,
    COUNT(*) AS Employee_Count
FROM HR_Data
GROUP BY Attrition;


-- 3. Attrition by department
SELECT
    Department,
    Attrition,
    COUNT(*) AS Employee_Count
FROM HR_Data
GROUP BY Department, Attrition
ORDER BY Department, Attrition;


-- 4. Attrition by job role
SELECT
    Job_Role,
    Attrition,
    COUNT(*) AS Employee_Count
FROM HR_Data
GROUP BY Job_Role, Attrition
ORDER BY Job_Role, Attrition;


-- 5. Average monthly income by department
SELECT
    Department,
    ROUND(AVG(Monthly_Income), 2) AS Average_Monthly_Income
FROM HR_Data
GROUP BY Department
ORDER BY Average_Monthly_Income DESC;


-- 6. Attrition by overtime
SELECT
    Overtime,
    Attrition,
    COUNT(*) AS Employee_Count
FROM HR_Data
GROUP BY Overtime, Attrition
ORDER BY Overtime, Attrition;


-- 7. Average job satisfaction by department
SELECT
    Department,
    ROUND(AVG(Job_Satisfaction), 2) AS Average_Job_Satisfaction
FROM HR_Data
GROUP BY Department
ORDER BY Average_Job_Satisfaction DESC;


-- 8. Attrition by age group
SELECT
    Age_Group,
    Attrition,
    COUNT(*) AS Employee_Count
FROM HR_Data
GROUP BY Age_Group, Attrition
ORDER BY Age_Group, Attrition;


-- 9. Average performance rating by department
SELECT
    Department,
    ROUND(AVG(Performance_Rating), 2) AS Average_Performance_Rating
FROM HR_Data
GROUP BY Department
ORDER BY Average_Performance_Rating DESC;


-- 10. Employees with high job satisfaction
SELECT
    Employee_ID,
    Department,
    Job_Role,
    Job_Satisfaction,
    Attrition
FROM HR_Data
WHERE Job_Satisfaction >= 4
ORDER BY Job_Satisfaction DESC;