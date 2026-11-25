import pandas as pd 
df=pd.read_csv("data/raw/retail_sales_dataset.csv")

# To check missing Values 
print(df.isnull().sum())

# To Find Total Missing Values 
print("Total Missing Values ")
print(df.isnull().sum().sum())

# To Find Duplicate Records
print("Total Duplicate Records")
print(df.duplicated().sum())

# To Display Row Containg Missing Values 
missing_row=df[df.isnull().any(axis=1)]
print(missing_row.head(10))

# Display Duplicated Records 
duplicates=df[df.duplicated()]
print("Duplicated records:")
print(duplicates.head(10))
print("Total duplicate records:",len(duplicates)) 

# To Check Duplicate Values 

duplicate_orders=df[df.duplicated(subset=["order_id"],keep=False)]
print("Duplicate Order IDs:")
print(duplicate_orders[["order_id","customer_name","order_date"]].head(20))

print("Total duplicate Order IDs:",len(duplicate_orders))

# To Count occurrences of each Order ID

order_counts=df["order_id"].value_counts()
print("Most repeated Order IDs:")
print(order_counts[order_counts>1].head(10))

# count Missing Order IDs
print("Missing Order IDs:",df["order_id"].isnull().sum())

# Investigate Missing Order IDs
missing_orders=df[df["order_id"].isnull()]
print("Records With missing Order IDs:")
print(missing_orders.head(10))
print("Total missing Orders IDs:",len(missing_orders))

# Investigate Completely Empty Rows
print("\nMissing Values in each missing-order record:")
print(missing_orders.isnull().sum(axis=1))

# Check How many cokumn contain actual data 
print("\nNumber of non-missing values in each record:")
print(missing_orders.notnull().sum(axis=1))

# Count completely empty records 
empty_rows=missing_orders.isnull().all(axis=1).sum()
print("\nCompletely empty rows:",empty_rows)

# Display all 30 records
print(missing_orders.to_string())

print("\n==========INVESTIGATION SUMMARY ==========")
print("Total records with misssing orders IDs:",len(missing_orders))
print("Completely empty records:",empty_rows)
print("\nNon-missing values per record:")
print(missing_orders.notnull().sum(axis=1).value_counts().sort_index())

# Create a working copy
cleaned_df=df.copy()

# Remove completely empty rows 
cleaned_df=cleaned_df.dropna(how="all")
print("Original dataset shape:",df.shape)
print("After removing empty rows:",cleaned_df.shape)
print("Rows removed:",len(df)-len(cleaned_df))

# Checkin Remainig missing values after removing empty rows 
print("\nMissing Values after removing empty rows:")
print(cleaned_df.isnull().sum())
print("\nTotal remaing missing values:")
print(cleaned_df.isnull().sum().sum())
print("\nMissing value percentage:")
print((cleaned_df.isnull().mean()*100).round(2))

# Step 1: Inspect data Types
print("\nCurrent Data Types:")
print(cleaned_df.dtypes)

# Step 2: Inspect order date values
print("\nOrder Date Sample:")
print(cleaned_df["order_date"].head(10))

# Step 3: Check dataset information 
print("\nDataset Information:")
cleaned_df.info()

print("\nOrder Date Data Type:")
print(cleaned_df["order_date"].dtype)
print("\nFirst 10 Order Dates:")
print(cleaned_df["order_date"].head(10).to_list())
print("\nMissing Order Dates:")
print(cleaned_df["order_date"].isnull().sum())

# Investegate different date formats
print("\nDates containg / :")
slash_dates=cleaned_df[cleaned_df["order_date"].str.contains("/",na=False)]
print(slash_dates["order_date"].value_counts())
print("\nTotal slash format dates:")
print(len(slash_dates))
print("\nTotal dash format dates:")
print(cleaned_df["order_date"].str.contains("-",na=False).sum())

# Find dates that don't contain - or / 
date_text=cleaned_df["order_date"].astype(str)
other_dates=cleaned_df[~date_text.str.contains(r"[-/]",na=False)]
print("\nOther date formats:")
print(other_dates["order_date"].value_counts(dropna=False))
print("\nTotal Other Dates")
print(len(other_dates))

# Inspect slash format dates 
print("\nSample slash format dates:")
print(slash_dates["order_date"].head(20).to_list())

# Inspect other date formats
print("\nsample other formats")
print(other_dates["order_date"].head(20).to_list())

# Standardize all order dates
cleaned_df["order_date"]=pd.to_datetime(cleaned_df["order_date"],format="mixed",dayfirst=True,errors="coerce")

#Check converted dates
print("\nConverted Order Dates:")
print(cleaned_df["order_date"].head(20))

# Check data type
print("\nNew Date Data Type:")
print(cleaned_df["order_date"].dtype)

# Check invalid dates
print("\nInvalid Dates:")
print(cleaned_df["order_date"].isnull().sum())

# step 4: Inspect Numerical Columns
print("\nNumerical column Summary:")
print(cleaned_df.describe())

# Check negative quanities
print("\nNegative Quantites")
print((cleaned_df["quantity"]<0).sum())

# Check zero quantites 
print("\nZero Quantites:")
print((cleaned_df["quantity"]==0).sum())

# Check negative unit prices
print("\nNegative Unit Price:")
print((cleaned_df["unit_price"]<0).sum())

# Investigate negative quantites
print("\nRecords With Negative Quantites:")
negative_qty=cleaned_df[cleaned_df["quantity"]<0]
print(negative_qty[["order_id","product_name","quantity","unit_price","sales_amount","order_status","return_flag"]])
print("\nTotal Negative Quantity Records:")
print(len(negative_qty))


# Investigate zero quantities
print("\nRecords with Zero Quantities:")
zero_qty=cleaned_df[cleaned_df["quantity"]==0]
print(zero_qty[["order_id","product_name","quantity","sales_amount","order_status","return_flag"]])

# Investigating Negative Quantites
print(len(negative_qty))
print("\nNegative Quantity Summary:")
print(negative_qty["quantity"].describe())
print("\nNegative Quantity Order Status:")
print(negative_qty["order_status"].value_counts())
print("\nNegative Quantity Return Flags:")
print(negative_qty["return_flag"].value_counts())

# Check duplicate records

print("\nDuplicate Records:")
print(cleaned_df.duplicated().sum())

# Display duplicate rows
duplicates = cleaned_df[cleaned_df.duplicated()]

print("\nDuplicate Rows:")
print(duplicates)

print("\nTotal Duplicate Rows:")
print(len(duplicates))

# Check missing values

print("\nMissing Values in Each Column:")
print(cleaned_df.isnull().sum())

print("\nTotal Missing Values:")
print(cleaned_df.isnull().sum().sum())

# Missing value percentage
print("\nMissing Value Percentage:")
print((cleaned_df.isnull().sum() / len(cleaned_df)) * 100)

# Check unique values in categorical columns

print("\nUnique Order Status:")
print(cleaned_df["order_status"].unique())

print("\nUnique Product Names:")
print(cleaned_df["product_name"].unique())

print("\nUnique Return Flags:")
print(cleaned_df["return_flag"].value_counts())

# Standardize order status

print("\nBefore Standardization:")
print(cleaned_df["order_status"].value_counts())

# Convert all values to lowercase
cleaned_df["order_status"] = cleaned_df["order_status"].str.lower()

print("\nAfter Standardization:")
print(cleaned_df["order_status"].value_counts())

# Remove extra spaces
cleaned_df["order_status"] = cleaned_df["order_status"].str.strip()

print("\nUnique Order Status:")
print(cleaned_df["order_status"].unique())

# Final Data Quality Check

print("\nFinal Dataset Information:")
print("Total Rows:", cleaned_df.shape[0])
print("Total Columns:", cleaned_df.shape[1])

# Check Missing Values
print("\nTotal Missing Values:")
print(cleaned_df.isnull().sum().sum())

# Check Duplicate Records
print("\nTotal Duplicate Records:")
print(cleaned_df.duplicated().sum())

# Check Unique Order Status
print("\nFinal Order Status:")
print(cleaned_df["order_status"].value_counts())

# Save Cleaned Dataset
cleaned_df.to_csv("retail_sales_cleaned.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

# Remove Duplicate Records
print("\nRemoving Duplicate Records...")
cleaned_df = cleaned_df.drop_duplicates()
print("Rows After Removing Duplicates:", len(cleaned_df))
print("Remaining Duplicate Records:")
print(cleaned_df.duplicated().sum())

# Save Updated Dataset
cleaned_df.to_csv("retail_sales_cleaned.csv", index=False)
print("\nUpdated Dataset Saved Successfully!")

# Investigate Missing Values
print("\nMissing Values Analysis:")
missing_values = cleaned_df.isnull().sum()
print(missing_values[missing_values > 0])

# Missing Value Percentage
print("\nMissing Value Percentage:")
missing_percentage = (cleaned_df.isnull().sum() / len(cleaned_df)) * 100
print(missing_percentage[missing_percentage > 0].round(2))

# Handle Missing Values Using Median
print("\nHandling Missing Values...")
columns_to_fill = [
    "age",
    "quantity",
    "discount_pct",
    "customer_satisfaction",
    "days_to_ship"
]

for col in columns_to_fill:
    median_value = cleaned_df[col].median()
    cleaned_df[col] = cleaned_df[col].fillna(median_value)

# Check Missing Values After Filling
print("\nMissing Values After Filling:")
print(cleaned_df.isnull().sum())
print("\nTotal Missing Values:")
print(cleaned_df.isnull().sum().sum())

# Save Final Cleaned Dataset
cleaned_df.to_csv("retail_sales_cleaned.csv", index=False)
print("\nMissing Values Handled Successfully!")