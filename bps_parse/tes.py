from BPSParser import *
import pandas as pd
import glob


### Menggabungkan data dengan kelompok komditas yang sama
listCsv = glob.glob("data_csv/*csv")
listDf = list(
    pd.read_csv(i).pipe(bps_parse, separator="_", fullResult=True) for i in listCsv
)
listUniqueGroup = set([Df["kelompok"] for Df in listDf])
for uniqueGroup in listUniqueGroup:
    sameDf = [Df["data"] for Df in listDf if Df["kelompok"] == uniqueGroup]
    fileNames = f"output/csv/Produksi_{uniqueGroup}.csv"
    pd.concat(sameDf, axis=1).to_csv(fileNames)
###
