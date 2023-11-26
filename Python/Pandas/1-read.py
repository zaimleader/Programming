import pandas as pd 
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/"

rd_xlsx = pd.read_excel(path + "excel/regions.xlsx")
rd_csv = pd.read_csv(path + "excel/crime.csv")
rd_txt = pd.read_csv(path + "files/data.txt", delimiter="\t")

print(rd_txt)