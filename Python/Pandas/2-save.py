import pandas as pd 
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/excel/"

df_csv = pd.read_csv(path + "notes.csv", header=None)


df_csv.columns = ["index", "Notes"]

df_csv.to_excel(path + "save/mod-notes.xlsx")

