import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

df_angin = pd.read_csv('dataset.csv')[['wSpeed.10', 'wDir.10']]

fig, ax = plt.subplots()

ax = WindroseAxes.from_ax()
ax.bar(df_angin['wDir.10'], df_angin['wSpeed.10'], normed=True, opening=.8, edgecolor='white')
ax.set_legend()
plt.savefig('data_output/windrose.png')