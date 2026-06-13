import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Agar hasil tetap sama setiap dijalankan
random.seed(42)
np.random.seed(42)

n_rows = 5000

categories = [
    "Electronics",
    "Fashion",
    "Home",
    "Beauty",
    "Sports",
    "Books",
    "Toys"
]

payment_methods = [
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "E-Wallet",
    "Cash"
]

cities = [
    "Jakarta",
    "Surabaya",
    "Bandung",
    "Medan",
    "Denpasar",
    "Makassar",
    "Yogyakarta"
]

genders = [
    "Male",
    "Female"
]

data = []

for i in range(n_rows):

    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(5, 1000), 2)
    discount = round(random.uniform(0, 0.30), 2)

    total_sales = round(
        quantity * unit_price * (1 - discount),
        2
    )

    order_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    row = {
        "Order_ID": f"ORD{100000 + i}",
        "Customer_ID": f"CUST{10000 + random.randint(1, 3000)}",
        "Customer_Name": fake.name(),
        "Gender": random.choice(genders),
        "Age": random.randint(18, 70),
        "City": random.choice(cities),
        "Product_Category": random.choice(categories),
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Order_Date": order_date,
        "Payment_Method": random.choice(payment_methods),
        "Email": fake.email(),
        "Discount": discount,
        "Rating": round(random.uniform(1, 5), 1),
        "Total_Sales": total_sales
    }

    data.append(row)

df = pd.DataFrame(data)

# ====================================================
# MEMBUAT DATA MENJADI "KOTOR"
# ====================================================

# Missing values
for col in ["Customer_Name", "Age", "Email", "Rating"]:
    idx = np.random.choice(df.index, size=100, replace=False)
    df.loc[idx, col] = np.nan

# Duplicate records
duplicates = df.sample(50, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Typo kota
city_typos = {
    "Jakarta": ["jakarta", "JAKARTA", "JKT", "Jakrta"],
    "Surabaya": ["surabya", "SURABAYA"],
    "Bandung": ["bandng", "BANDUNG"]
}

for city, typo_list in city_typos.items():
    idx = df[df["City"] == city].sample(
        30,
        random_state=42
    ).index

    df.loc[idx, "City"] = np.random.choice(
        typo_list,
        len(idx)
    )

# Gender tidak konsisten
gender_map = {
    "Male": ["male", "M", "Pria"],
    "Female": ["female", "F", "Wanita"]
}

for gender, variants in gender_map.items():
    idx = df[df["Gender"] == gender].sample(
        40,
        random_state=42
    ).index

    df.loc[idx, "Gender"] = np.random.choice(
        variants,
        len(idx)
    )

# Umur tidak valid
idx = np.random.choice(df.index, 20, replace=False)
df.loc[idx, "Age"] = [-5, 0, 150, 999] * 5

# Harga tidak valid
idx = np.random.choice(df.index, 15, replace=False)
df.loc[idx, "Unit_Price"] = [
    -100,
    0,
    -50,
    999999,
    -500
] * 3

# Quantity tidak masuk akal
idx = np.random.choice(df.index, 15, replace=False)
df.loc[idx, "Quantity"] = [
    0,
    -1,
    999,
    5000,
    200
] * 3

# Email tidak valid
invalid_emails = [
    "gmail.com",
    "andi@",
    "siti.gmail.com",
    "abc@abc",
    "test"
]

idx = np.random.choice(df.index, 25, replace=False)
df.loc[idx, "Email"] = np.random.choice(
    invalid_emails,
    25
)

# Format tanggal berantakan
idx = np.random.choice(df.index, 40, replace=False)

date_formats = [
    "%d/%m/%Y",
    "%m-%d-%y",
    "%Y/%m/%d"
]

for i in idx:
    dt = pd.to_datetime(df.loc[i, "Order_Date"])

    fmt = random.choice(date_formats)

    df.loc[i, "Order_Date"] = dt.strftime(fmt)

# Total Sales sengaja dibuat salah
idx = np.random.choice(df.index, 30, replace=False)

df.loc[idx, "Total_Sales"] *= random.uniform(
    1.5,
    3.0
)

# ====================================================
# SAVE CSV
# ====================================================

df.to_csv(
    "data/dirty_ecommerce_sales.csv",
    index=False
)

print("=" * 50)
print("DIRTY DATASET BERHASIL DIBUAT!")
print(f"Jumlah baris : {len(df)}")
print(f"Jumlah kolom : {df.shape[1]}")
print("File tersimpan di:")
print("data/dirty_ecommerce_sales.csv")
print("=" * 50)