import pandas as pd
import re

# Load data
df = pd.read_csv("data/dirty_ecommerce_sales.csv")

print("=" * 50)
print("DATA INSPECTION")
print("=" * 50)

print("\n=== Missing Values Sebelum Cleaning ===")
print(df.isnull().sum())

print("\nShape Dataset:")
print(df.shape)

print("\nInfo Dataset:")
df.info()

print("\nJumlah Duplicate:")
print(df.duplicated().sum())

print("\nStatistik Numerik:")
print(df.describe())

print("\n5 Data Pertama:")
print(df.head())

print("=" * 50)

# ==================================================
# MISSING VALUE TREATMENT
# ==================================================

print("\nMemproses Missing Values...")

# Customer Name
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")

# Age
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Email
df["Email"] = df["Email"].fillna("unknown@example.com")

# Rating
mean_rating = df["Rating"].mean()
df["Rating"] = df["Rating"].fillna(round(mean_rating, 1))

print("Missing Values berhasil ditangani!")

print("\n=== Missing Values Setelah Cleaning ===")
print(df.isnull().sum())
print("\nDataset setelah Missing Value Treatment berhasil diperbarui.")

# ==================================================
# DUPLICATE REMOVAL
# ==================================================

print("\n=== Duplicate Removal ===")

duplicate_before = df.duplicated().sum()

print(f"Duplicate sebelum dihapus: {duplicate_before}")

df = df.drop_duplicates()

duplicate_after = df.duplicated().sum()

print(f"Duplicate setelah dihapus: {duplicate_after}")

print(f"Jumlah baris sekarang: {len(df)}")

#============= Standardization =============
city_mapping = {
    "jakarta": "Jakarta",
    "JAKARTA": "Jakarta",
    "JKT": "Jakarta",
    "Jakrta": "Jakarta",

    "bandng": "Bandung",
    "BANDUNG": "Bandung",

    "surabya": "Surabaya",
    "SURABAYA": "Surabaya"
}

df["City"] = df["City"].replace(city_mapping)

gender_mapping = {
    "male": "Male",
    "M": "Male",
    "Pria": "Male",

    "female": "Female",
    "F": "Female",
    "Wanita": "Female"
}

df["Gender"] = df["Gender"].replace(gender_mapping)

print("\nCity setelah standardisasi:")
print(df["City"].value_counts())

print("\nGender setelah standardisasi:")
print(df["Gender"].value_counts())

print(sorted(df["City"].unique()))
print(sorted(df["Gender"].unique()))

# ==================================================
# EMAIL VALIDATION
# ==================================================

print("\n=== Email Validation ===")

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_before = (
    ~df["Email"].str.match(email_pattern, na=False)
).sum()

print(f"Jumlah email tidak valid sebelum cleaning: {invalid_before}")

# Ganti email tidak valid
df.loc[
    ~df["Email"].str.match(email_pattern, na=False),
    "Email"
] = "unknown@example.com"

invalid_after = (
    ~df["Email"].str.match(email_pattern, na=False)
).sum()

print(f"Jumlah email tidak valid setelah cleaning: {invalid_after}")

# ==================================================
# DATE CLEANING
# ==================================================

print("\n=== Date Cleaning ===")

print("\nContoh tanggal sebelum cleaning:")
print(df["Order_Date"].head(10))

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce",
    format="mixed"
)

print("\nJumlah tanggal gagal dikonversi:")
print(df["Order_Date"].isnull().sum())

print("\nTipe data Order_Date:")
print(df["Order_Date"].dtype)

print("\nContoh tanggal setelah cleaning:")
print(df["Order_Date"].head(10))

# ==================================================
# OUTLIER HANDLING
# ==================================================

print("\n=== Outlier Handling ===")

print("\nSebelum Cleaning:")

print(f"Age min: {df['Age'].min()}")
print(f"Age max: {df['Age'].max()}")

print(f"Quantity min: {df['Quantity'].min()}")
print(f"Quantity max: {df['Quantity'].max()}")

print(f"Unit Price min: {df['Unit_Price'].min()}")
print(f"Unit Price max: {df['Unit_Price'].max()}")

age_before = len(df)

df = df[
    (df["Age"] >= 13) &
    (df["Age"] <= 100)
]

print(f"\nBaris dihapus karena Age tidak valid: {age_before - len(df)}")

qty_before = len(df)

df = df[
    (df["Quantity"] >= 1) &
    (df["Quantity"] <= 100)
]

print(f"Baris dihapus karena Quantity tidak valid: {qty_before - len(df)}")

price_before = len(df)

df = df[
    (df["Unit_Price"] > 0) &
    (df["Unit_Price"] <= 10000)
]

print(f"Baris dihapus karena Unit Price tidak valid: {price_before - len(df)}")

print("\nSetelah Cleaning:")

print(f"Age min: {df['Age'].min()}")
print(f"Age max: {df['Age'].max()}")

print(f"Quantity min: {df['Quantity'].min()}")
print(f"Quantity max: {df['Quantity'].max()}")

print(f"Unit Price min: {df['Unit_Price'].min()}")
print(f"Unit Price max: {df['Unit_Price'].max()}")

print(f"\nJumlah baris setelah Outlier Handling: {len(df)}")

# ==================================================
# RECALCULATE TOTAL SALES
# ==================================================

print("\n=== Recalculate Total Sales ===")

print("\nContoh Total Sales sebelum diperbaiki:")

print(
    df[
        [
            "Quantity",
            "Unit_Price",
            "Discount",
            "Total_Sales"
        ]
    ].head()
)

df["Total_Sales"] = (
    df["Quantity"]
    * df["Unit_Price"]
    * (1 - df["Discount"])
).round(2)

print("\nTotal Sales berhasil dihitung ulang!")

print("\nContoh Total Sales setelah diperbaiki:")

print(
    df[
        [
            "Quantity",
            "Unit_Price",
            "Discount",
            "Total_Sales"
        ]
    ].head()
)
# ==================================================
# FINAL DUPLICATE CHECK
# ==================================================

print("\n=== Final Duplicate Check ===")

duplicate_before = df.duplicated().sum()

print(f"Duplicate ditemukan: {duplicate_before}")

if duplicate_before > 0:
    df = df.drop_duplicates()

duplicate_after = df.duplicated().sum()

print(f"Duplicate setelah dibersihkan: {duplicate_after}")

print(f"Jumlah baris akhir: {len(df)}")

# ==================================================
# FINAL VALIDATION
# ==================================================

print("\n=== FINAL VALIDATION ===")

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Email Validation
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_email = (
    ~df["Email"].str.match(email_pattern, na=False)
).sum()

print("\nInvalid Email:")
print(invalid_email)

# Age
print("\nAge Range:")
print(
    f"Min: {df['Age'].min()}, "
    f"Max: {df['Age'].max()}"
)

# Quantity
print("\nQuantity Range:")
print(
    f"Min: {df['Quantity'].min()}, "
    f"Max: {df['Quantity'].max()}"
)

# Unit Price
print("\nUnit Price Range:")
print(
    f"Min: {df['Unit_Price'].min()}, "
    f"Max: {df['Unit_Price'].max()}"
)

# Order Date
print("\nOrder_Date Type:")
print(df["Order_Date"].dtype)

# Gender
print("\nGender Categories:")
print(sorted(df["Gender"].unique()))

# City
print("\nCity Categories:")
print(sorted(df["City"].unique()))

print("\n" + "=" * 50)

if (
    df.isnull().sum().sum() == 0
    and df.duplicated().sum() == 0
    and invalid_email == 0
):
    print("🎉 VALIDATION PASSED!")
    print("Dataset siap digunakan.")
else:
    print("⚠ VALIDATION FAILED!")
    print("Masih ada masalah pada dataset.")

print("=" * 50)

df.to_csv(
    "data/cleaned_ecommerce_sales.csv",
    index=False
)

print("\nClean dataset berhasil disimpan!")