import pandas as pd 

# Load Final Cleaned Dataset 
df=pd.read_csv("retail_sales_final.csv")
print("Dataset Loaded Successfully!")
print(df.head())
print(df.shape)
print(df.columns)

# 1. Top 5 Products Categories
category_sales=df.groupby("product_category")["sales_amount"].sum()
category_sales=category_sales.sort_values(ascending=False)
print("\nTop 5 Products Categories:")
print(category_sales.head(5))

# 2. Top 5 Customers By Sales
customer_sales=df.groupby("customer_name")["sales_amount"].sum()
customer_sales.sort_values(ascending=False)
print("\nTop 5 Customers By Sales:")
print(customer_sales.head(5))

# 3. Best Performing Region
region_sales = df.groupby("region")["sales_amount"].sum()
region_sales = region_sales.sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)
print("\nBest Performing Region:")
print(region_sales.idxmax())