import pandas as pd 
from openpyxl.workbook import Workbook

path = "Python/Pandas/resources/excel/"

df = pd.read_csv(path + "crime.csv", header=None)

# ----- default columns -----
# ['INCIDENT_NUMBER', 'OFFENSE_CODE', 'OFFENSE_CODE_GROUP', 'OFFENSE_DESCRIPTION', 'DISTRICT', 'REPORTING_AREA', 'SHOOTING', 'YEAR','MONTH', 'DAY_OF_WEEK', 'HOUR']

# ----- rename columns ----- You should to add paramter in read.csv for ignore header
df.columns = ["col_A", "col_B", "col_C",  "col_D", "col_E", "col_F", "col_G", "col_H", "col_I", "col_J", "col_K"]

# ----- specifier des columns que vous voulez ------ 
# df[["col_A", "col_D"]]

# ----- slice rows -----
# df["col_A"][0:5]

# ----- index location ------
# df.iloc[10] -> show row 10
# df.iloc[2, 1] -> show value in row = 2 & col = 1

# ----- save file excel with slice data ------
wanted_values = df[["col_A", "col_B", "col_C"]]
stored = wanted_values.to_excel(path + "save/crime_slicing.xlsx", index=None)