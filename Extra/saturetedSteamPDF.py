from tabula import read_pdf
from tabula import tabulate


try:
    df = read_pdf('Saturated Vapour Curves.pdf')
    print(df)
