from BPSParser import *
import pandas as pd
import glob


### Menggabungkan data dengan kelompok komditas yang sama
# listCsv = glob.glob("data_csv/*csv")
# listDf = list(
#     pd.read_csv(i).pipe(bps_parse, separator="_", fullResult=True) for i in listCsv
# )
# listUniqueGroup = set([Df["kelompok"] for Df in listDf])
# for id, uniqueGroup in enumerate(listUniqueGroup):
#     sameDf = [Df["data"] for Df in listDf if Df["kelompok"] == uniqueGroup]
#     fileNames = f"output/csv/Produksi_{id}.csv"
#     pd.concat(sameDf, axis=1).to_csv(fileNames)
###
pathInput = "data_csv/*csv"
pathOutput = "output/"

bulk_parse(pathInput, pathOutput, fileType="txt", separator="_")
