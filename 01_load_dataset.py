import pandas as pd 
df=pd.read_csv("data/raw/retail_sales_dataset.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.tail())