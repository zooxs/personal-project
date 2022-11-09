import pandas as pd
import math

data = pd.read_csv('dataset.csv')
data = data[['time', 'wSpeed.10', 'wDir.10']]
data = data.drop(data[data['wSpeed.10'] == 0].index)

# feff = pd.read_excel('fetch_efektif.xlsx')
feff = pd.read_csv('fetch_efektif.csv')
feff = feff.set_index('arah').T

# fungsi utk menentukan kategori arah mata angin
def wDir_code(wDir_val):
    stored_val = []
    for i in wDir_val:
        if (i >= 337.5) and (i <= 360):
            stored_val.append('N')
        elif (i >= 0) and (i < 22.5):
            stored_val.append('N')
        elif (i >= 22.5) and (i < 67.5):
            stored_val.append('NE')
        elif (i >= 67.5) and (i < 112.5):
            stored_val.append('E')
        elif (i >= 112.5) and (i < 157.5):
            stored_val.append('SE')
        elif (i >= 157.5) and (i < 202.5):
            stored_val.append('S')
        elif (i >= 202.5) and (i < 247.5):
            stored_val.append('SW')
        elif (i >= 247.5) and (i < 292.5):
            stored_val.append('W')
        elif (i >= 292.5) and (i < 337.5):
            stored_val.append('NW')
    return stored_val

# fungsi utk menentukan lama angin berhembus setiap arah
def set_time(ls_code, number):
    mark = ls_code[0]
    val = [number]
    count = number
    for i in ls_code[1:]:
        if i == mark:
            count += number
            val.append(count)
        else: 
            count = number
            val.append(count)
            mark = i
    return val

# fungsi utk menentukan nilai koefisien c1 dan c2
def set_coef(tf, t):
    C1, C2 = [], []
    for time, times in zip(tf,t):
        if time >1 and time <=3600:
            c1 = 1.277 + 0.296*math.tanh(0.9*math.log10(45/time))
        elif time > 3600 :
            c1 = -0.15*math.log10(time) + 1.5334
        if times >1 and times <=3600:
            c2 = 1.277 + 0.296*math.tanh(0.9*math.log10(45/times))
        elif times > 3600 :
            c2 = -0.15*math.log10(times) + 1.5334
        C2.append(c2)
        C1.append(c1)
    return [C1, C2]


def hindcasting(UA, t, Feff):
    H, T, FD = [], [], []
    for a, b, c in zip(UA, t, Feff):
        if (b/a)*9.81 == 71500:
            # y = 'Fully Developed'
            h = (0.2433/9.81)*a**2
            ts = (8.132/9.81)*a
        
        else:
            # y = 'Undeveloped'
            tc = (68.8/9.81)*a*(9.81*(c/a**2))**(2/3)
            
            if b > tc:
                Fd = 0
                h = (0.0016/9.81)*(a**2)*(9.81*(c/a**2))**0.5
                ts = (0.2857/9.81)*a*(9.81*(c/a**2))**(1/3)
            
            else:
                Fd = (a**2/9.81)*((9.81/68.8)*(b/a))**1.5
                h = (0.0016/9.81)*(a**2)*(9.81*(Fd/a**2))**0.5
                ts = (0.2857/9.81)*a*(9.81*(Fd/a**2))**(1/3)
    
        H.append(h)
        T.append(ts)
        FD.append(Fd)
    return [FD,H,T]

data['arah'] = wDir_code(data['wDir.10'])
data['Feff'] = [ feff[i].values[0] for i in data['arah'] ]
data['t'] = set_time(data['arah'], 3600)
data['tf'] = 1609/data['wSpeed.10']
data['C1'], data['C2'] = set_coef(data['tf'], data['t'])
data['U3600'] = data['wSpeed.10']/data['C1']
data['UL'] = data['U3600']*data['C2']
data['UW'] = data['UL']*0.9
data['UC'] = data['UW']*1.1
data['UA'] = 0.71*(data['UC']**1.23)
data['Fd'], data['Hs'], data['Ts'] = hindcasting(data['UA'], data['t'], data['Feff'])

data.to_csv('./data_output/hasil_hindcasting.csv', index=False)