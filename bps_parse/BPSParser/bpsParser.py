from pandas import concat

def bps_parse(df, separator=' '):

    """Fungsi yang bertujuan untuk mengekstrak dan mentrasnformasikan data BPS ke dalam bentuk long table.

    :paramter df: Objek DataFrame
    :return: Objek DataFrame
    """

    # Penentuan variabel judul, golongan, jenis dan satuan data
    fields = df.columns[0]
    title = ''
    unit = ''
    group = None
    
    
    # Pengecekan satuan pada judul tabel

    if '(' in df.columns[1]:
        title = separator.join(df.columns[1].split('(')[0].split(separator)[:-1]).replace('/', separator)
        group = separator.join(title.split(separator)[1:])
        unit = df.columns[1].split('(')[-1][:-1]
    else:
        title = df.columns[1]
        group = separator.join(title.split(separator)[1:])
        
    # daftar nama kolom awal
    old_col = df.columns[1:]

    # mengeluarkan keterangan data
    df = df.iloc[:-4]
    ls_field = df[fields].dropna().values
    
    # penentuan baris data yang memuat nilai NaN
    nan_rows = df.loc[df.isnull().any(axis=1) == True]
    year = nan_rows.iloc[-1].dropna().astype('int').unique().tolist()
    
    if nan_rows.shape[0] == 1:
        sub_class = [group]
    else: 
        sub_class = nan_rows.dropna(axis=1).iloc[0].to_list()
    
    # mengganti nilai - dengan 0
    df = df.dropna(axis=0)[old_col].replace('-', '0')
    
    
    ls_data = []
    for n,_ in enumerate(old_col):
        if (n != len(old_col) - 1) & (n % len(year) == 0):
            m = int(n/len(year))
            df1 = df[old_col[n:n+len(year)]].astype('float')
            df1.columns = year

            df1[fields] = ls_field
            df1['Kelompok'] = group
            df1['Jenis'] = group if len(sub_class) == 1 else sub_class[m-1]
            df1['Satuan'] = unit

            ls_data.append(df1)

    result = concat(ls_data)

    # pengisian nilai satuan jika terdapat pada jensi komoditas
    if unit == '':
        expand_cols = result['Jenis'].str.split('(', expand=True)
        result['Satuan'] = expand_cols[1].str.replace(')', '', regex=False)
        result['Jenis'] = expand_cols[0]
    
    # mengganti case pada kolom daerah menjadi Title Case
    result['Provinsi'] = result['Provinsi'].str.title()
    
    # penyusunan kolom data
    oldCols = result.columns.to_list()
    newCols = oldCols[-4:] + oldCols[:len(oldCols)-4]
    return result[newCols]