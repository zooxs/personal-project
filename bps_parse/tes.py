from BPSParser import *
import pandas as pd

filename = 'tes/Produksi Tanaman Sayuran.xlsx'

df = pd.read_excel(filename)
df = df.pipe(bps_parse)


print(df)
