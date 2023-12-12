import pandas as pd 
import numpy as np
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/excel/"

df = pd.read_excel(path + "all_shifts.xlsx")

df.drop(columns="Sales Rep", inplace=True)

df = df.set_index("Units Sold")

# print(df.loc[111])

df.Region = df.Region.str.split(expand=True)

df = df.replace("Paper", "N/A", regex=True) # np.nan

df.to_excel(path + "save/cleaning.xlsx")

print(df)