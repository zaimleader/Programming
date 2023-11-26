import pandas as pd 
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/"

df_xlsx = pd.read_excel(path + "excel/regions.xlsx")
df_csv = pd.read_csv(path + "excel/crime.csv")
df_txt = pd.read_csv(path + "files/data.txt", delimiter="\t")

print(df_txt)