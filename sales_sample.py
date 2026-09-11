import pandas as pd
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print("Shape:", df.shape)
print("Columns:")
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df[df.duplicated])
df = df.drop_duplicates()


df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

df["ADDRESSLINE2"] = df["ADDRESSLINE2"].fillna("Unknown")
df["STATE"] = df["STATE"].fillna("Unknown")
df["POSTALCODE"] = df["POSTALCODE"].fillna("Unknown")
df["TERRITORY"] = df["TERRITORY"].fillna("Unknown")


print(df.describe())
print(df["STATUS"].value_counts())
print(df["YEAR_ID"].value_counts())
print(df["PRODUCTLINE"].value_counts())
