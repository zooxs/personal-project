import pandas as pd
import glob

ls_file = sorted(glob.glob('./data_angin/*txt'))
ls_data = (pd.read_csv(i, sep='\t') for i in ls_file)
data = pd.concat(ls_data)
data = data[['time', 'wSpeed.10', 'wDir.10']]

data.to_csv('dataset.csv', index=False)
