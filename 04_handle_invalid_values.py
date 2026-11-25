import pandas as pd

# Load Cleaned Dataset
df=pd.read_csv("retail_sales_cleaned.csv")
print("Dataset Loaded Successfully!")
print("Dataset Shape:",df.shape)

# Check invalid ages
print("\nInvalid Ages:")
print(df[(df["age"] < 1) | (df["age"] > 100)])

# Check invalid quantities
print("\nInvalid Quantities:")
print(df[(df["quantity"] <= 0) | (df["quantity"] == 999)])

# Check invalid shipping costs
print("\nInvalid Shipping Costs:")
print(df[df["shipping_cost"] < 0])

# Check invalid shipping days
print("\nInvalid Shipping Days:")
print(df[df["days_to_ship"] < 0])

# Handling Invalid Values
print("\nHandling Invalid Values...")

# Fix invalid ages
df.loc[(df["age"] < 1) | (df["age"] > 100), "age"] = df["age"].median()

# Fix invalid quantities
df.loc[(df["quantity"] <= 0) | (df["quantity"] == 999), "quantity"] = df["quantity"].median()

# Fix invalid shipping costs
df.loc[df["shipping_cost"] < 0, "shipping_cost"] = df["shipping_cost"].median()

# Fix invalid shipping days
df.loc[df["days_to_ship"] < 0, "days_to_ship"] = df["days_to_ship"].median()
print("Invalid Values Handled Successfully!")

# Verify The Results
print("\nChecking Invalid Values After Fixing:")
print("Invalid Ages:", ((df["age"] < 1) | (df["age"] > 100)).sum())
print("Invalid Quantities:", ((df["quantity"] <= 0) | (df["quantity"] == 999)).sum())
print("Invalid Shipping Costs:", (df["shipping_cost"] < 0).sum())
print("Invalid Shipping Days:", (df["days_to_ship"] < 0).sum())

# Save The Updated Dataset
df.to_csv("retail_sales_final.csv", index=False)
print("\nFinal Dataset Saved Successfully!")