import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load final cleaned dataset
df = pd.read_csv("retail_sales_final.csv")

# Sales by Product Category
category_sales = df.groupby("product_category")["sales_amount"].sum()

# Create Bar Chart
plt.figure(figsize=(10, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Region-wise Sales
region_sales=df.groupby("region")["sales_amount"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# Monthly Sales Trend

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = df.groupby(
    df["order_date"].dt.to_period("M")
)["sales_amount"].sum()

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.show()