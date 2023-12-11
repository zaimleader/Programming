import pandas as pd 
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/excel/"

df = pd.read_excel(path + "all_shifts.xlsx")

# filter 1: loc with single item
# df = df.loc[(df["Region"] == "North") & (df["Product"] == "Stapler")]

# ---> with multiple items
myItems = ["Paper", "Pen"] # Define the list of items you want to filter by

df = df.loc[df["Product"].isin(myItems)]    # my items is in "Product"

# df = df.loc[~df["Product"].isin(myItems)] # my items is not in "Product"

# filter 2: lambda
df["Tax %"] = df["Units Sold"].apply(lambda x: .15 if 10 < x < 99 else .20 if 100 < x < 200 else .25)

df["Tax Owed"] = df["Units Sold"] * df["Tax %"]

# drop columns
to_drop = ['Shift', "Region", "Sales Rep", "Product"]

df.drop(columns=to_drop, inplace=True)

# change val of cell with a condition
df["Test col"] = False
df.loc[df["Tax Owed"] > 15.0, "Test col"] = True

# group
print(df.groupby(["Test col"]).mean().sort_values("Units Sold"))

# print(df)