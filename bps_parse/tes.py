from BPSParser import *
import pandas as pd

df = pd.read_excel('tes/dataset.xlsx')
print(df.pipe(bps_parse))
