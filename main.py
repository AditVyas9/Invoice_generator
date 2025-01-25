import pandas as pd
import glob as gb
from fpdf import FPDF

filepaths = gb.glob("Invoice/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",unit="mm", format="A4")
    pdf.add_page()
    Invoice_no = filepath[8:13]
    print(Invoice_no)
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=50, h=8, txt=f"Invoice no: {Invoice_no}")