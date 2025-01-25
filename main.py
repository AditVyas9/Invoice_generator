import pandas as pd
import glob as gb

filepaths = gb.glob("Invoice/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)