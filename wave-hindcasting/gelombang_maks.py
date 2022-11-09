import pandas as pd

data = pd.read_csv('./data_output/hasil_hindcasting.csv')
data = data[['time', 'Hs', 'Ts']]
set_date = data['time'].str.split(expand=True)[0].str.split('-',expand=True)
data['Y'] = set_date[0]
data['M'] = set_date[1]
data['D'] = set_date[2]

data = data[['Y', 'M', 'D', 'Hs', 'Ts']]

# dafta tahun
ls_Y = data['Y'].unique()

# daftar bulan
ls_M = data['M'].unique()

ls_gmax = []
for y in ls_Y:
    # menentukan nilai tinggi gelombang maksimum setiap bulannya
    # for m in ls_M:
    #     val = data.loc[(data['Y'] == y) & (data['M'] == m)]
    #     ls_gmax.append(val.loc[val['Hs'] == val['Hs'].max()])

    # menentukan nilai tinggi gelombang maksimum setiap tahunnya

    val = data.loc[data['Y'] == y]
    ls_gmax.append(val.loc[val['Hs'] == val['Hs'].max()])


output = pd.concat(ls_gmax)
output.to_csv('./data_output/hasil_gel_max.csv', index=False)
