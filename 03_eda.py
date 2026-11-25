import pandas as pd 
import numpy as np 

# Load Cleaned dataset
df=pd.read_csv("retail_sales_cleaned.csv")
print("Dataset Loaded Successfully!")
print("\nDataset Shape:")
print(df.shape)
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())


# Total Sales
print("\nTotal Sales:")
print(df["sales_amount"].sum())

# Average Sales
print("\nAverage Sales:")
print(df["sales_amount"].mean())

# Maximum Sales
print("\nMaximum Sales:")
print(df["sales_amount"].max())

# Minimum Sales
print("\nMinimum Sales:")
print(df["sales_amount"].min())

# Total Profit
print("\nTotal Profit:")
print(df["profit"].sum())
print("\nSales By Product Category:")
category_sales = df.groupby(
    "product_category"
)["sales_amount"].sum().sort_values(ascending=False)
print(category_sales)
print("\nRegion Wise Sales:")
region_sales = df.groupby(
    "region"
)["sales_amount"].sum().sort_values(ascending=False)
print(region_sales)
print("\nOrder Status Analysis:")
order_analysis = df["order_status"].value_counts()
print(order_analysis)

# Convert order_date into datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract month
df["month"] = df["order_date"].dt.month
print("\nMonthly Sales:")
monthly_sales = df.groupby(
    "month"
)["sales_amount"].sum()
print(monthly_sales)

# Investigate Invalid values
print("\nChecking Invalid Values:")
print("\nInvalid Ages:")
print(df[(df["age"] < 0) | (df["age"] > 100)])
print("\nInvalid Quantities:")
print(df[df["quantity"] <= 0])
print("\nInvalid Shipping Costs:")
print(df[df["shipping_cost"] < 0])
print("\nInvalid Shipping Days:")
print(df[df["days_to_ship"] < 0])

# Improve monthly sales analysis
df["order_date"] = pd.to_datetime(df["order_date"])
df["year_month"] = df["order_date"].dt.to_period("M")
monthly_sales = df.groupby(
    "year_month"
)["sales_amount"].sum()
print("\nMonthly Sales Analysis:")
print(monthly_sales)