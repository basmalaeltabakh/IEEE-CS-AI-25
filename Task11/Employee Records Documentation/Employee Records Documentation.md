

## 1. Data Entry & Formatting

- **Employee Records Sheet** contains **more than 50 entries**.
    
- **Dataset Source**:
    
    - The dataset was originally obtained from [Kaggle - Employee Records Dataset](https://www.kaggle.com/datasets/cankatsrc/employee-records-dataset).
        
    - Modifications were made to fill missing values, improve formatting, and align with task requirements.
        
- **Fields included**:
    
    - Employee ID
        
    - Name
        
    - Department
        
    - Job Title
        
    - Date of Joining
        
    - Salary
        
    - Email
        
    - Phone Number
        
    - Status (Active/Inactive)
        
    - Category (Senior/Junior)
        
    - Department Rules (retrieved using VLOOKUP)
        

## 2. Data Validation

- **Drop-down lists** implemented for:
    
    - Department (HR, IT, Finance, Admin, etc.)
        
    - Job Title
        
    - Status (Active/Inactive)
        
- **Restrictions applied**:
    
    - Salary must be numeric and greater than 0.
        
    - Email must follow a valid format ([example@example.com](mailto:example@example.com)).
        
    - Date of Joining cannot be in the future.
        
    - Status can only be "Active" or "Inactive".
        

## 3. Sorting & Filtering

- **Sorting**:
    
    - Sorted by **Department** and **Date of Joining** for better organization.
        
- **Filtering**:
    
    - Enabled filtering to display employees who joined after a specific year.
        

## 4. Conditional Formatting

- **Salary below $50,000** highlighted in **red**.
    
- **Employees who joined in the last Year** highlighted in **green**.
    

## 5. Functions & Lookups

- **IF statements** used to classify employees:
    
    - If **Salary > $100,000**, label as "Senior"; otherwise, "Junior".
        
- **VLOOKUP** used to retrieve department-specific rules from another sheet.
    

## 6. PivotTables & Reports

- **Summary report** created to show the number of employees in each department.
    
- **Grouping by year of joining** to analyze hiring trends.
    
- **Filters** added to allow analysis based on "Active/Inactive" status.
    
--- 
