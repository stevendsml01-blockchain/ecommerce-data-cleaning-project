# 🛒 End-to-End E-Commerce Data Cleaning Project

This project demonstrates a complete data cleaning workflow using Python and Pandas on a synthetic e-commerce dataset.

## 📌 Project Overview

The dataset contains realistic issues commonly found in business environments, including:

- Missing values
- Duplicate records
- Inconsistent categorical values
- Invalid email addresses
- Mixed date formats
- Outliers
- Incorrect business calculations

The objective of this project is to transform dirty transactional data into a clean, analysis-ready dataset.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook

---

## 📂 Project Structure

```
ecommerce-data-cleaning/
│
├── data/
│   ├── dirty_ecommerce_sales.csv
│   └── cleaned_ecommerce_sales.csv
│
├── notebooks/
│   └── Ecommerce_Data_Cleaning.ipynb
│
├── src/
│   ├── generate_data.py
│   ├── clean_data.py
│   └── validation.py
│
├── requirements.txt
└── README.md
```

---

## 🔍 Data Cleaning Process

### 1. Missing Value Treatment

Handled missing values in:

- Customer_Name
- Age
- Email
- Rating

---

### 2. Duplicate Removal

Removed duplicate transaction records.

---

### 3. Data Standardization

Standardized inconsistent values in:

- Gender
- City

---

### 4. Email Validation

Validated and corrected invalid email formats.

---

### 5. Date Cleaning

Converted transaction dates into proper datetime format.

---

### 6. Outlier Handling

Removed invalid values such as:

- Age below 18 or above 70
- Quantity outside business rules
- Negative or unrealistic prices

---

### 7. Business Rule Validation

Recalculated Total_Sales using:

Total_Sales = Quantity × Unit_Price × (1 − Discount)

---

### 8. Final Validation

Validated that the final dataset contains:

- No missing values
- No duplicates
- Valid emails
- Consistent categories
- Proper data types
- Business-ready records

---

## 📈 Results

Initial Dataset:

- Rows: 5,050

Final Clean Dataset:

- Rows: 4,961

Validation Status:

✅ PASSED

Dataset is ready for analysis and reporting.

---

## 🚀 Author

**Christians Steven Zoe**

Aspiring Data Scientist passionate about solving business problems using data.
