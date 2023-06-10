from pandas import concat, DataFrame
import pandas as pd
import glob

# ektraks single data


# ektraks satu data bps
def bps_parse(df: DataFrame, separator=" ", fullResult=False):
    """Fungsi yang bertujuan untuk mengekstrak dan mentrasnformasikan data BPS ke dalam bentuk long table.

    :param df: Objek DataFrame
    :return: Objek DataFrame
    """

    # Penentuan variabel judul, golongan, jenis dan satuan data
    fields = df.columns[0]
    title = ""
    unit = ""
    group = None

    # Pengecekan satuan pada judul tabel

    if "(" in df.columns[1]:
        title = separator.join(
            df.columns[1].split("(")[0].split(separator)[:-1]
        ).replace("/", separator)
        group = separator.join(title.split(separator)[1:])
        unit = df.columns[1].split("(")[-1][:-1]
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
    year = nan_rows.iloc[-1].dropna().astype("int").unique().tolist()

    if nan_rows.shape[0] == 1:
        sub_class = [group]
    else:
        sub_class = nan_rows.dropna(axis=1).iloc[0].to_list()

    # mengganti nilai - dengan 0
    df = df.dropna(axis=0)[old_col].replace("-", "0")

    ls_data = []
    for n, _ in enumerate(old_col):
        if (n != len(old_col) - 1) & (n % len(year) == 0):
            m = int(n / len(year))
            df1 = df[old_col[n : n + len(year)]].astype("float")
            df1.columns = year

            df1[fields] = ls_field
            df1["Kelompok"] = group
            df1["Jenis"] = group if len(sub_class) == 1 else sub_class[m - 1]
            df1["Satuan"] = unit

            ls_data.append(df1)

    result = concat(ls_data)

    # pengisian nilai satuan jika terdapat pada jensi komoditas
    if unit == "":
        expand_cols = result["Jenis"].str.split("(", expand=True)
        result["Satuan"] = expand_cols[1].str.replace(")", "", regex=False)
        result["Jenis"] = expand_cols[0]

    # mengganti case pada kolom daerah menjadi Title Case
    result[fields] = result[fields].str.title()

    # penyusunan kolom data
    oldCols = result.columns.to_list()
    newCols = oldCols[-4:] + oldCols[: len(oldCols) - 4]
    result = result[newCols].reset_index(drop=True)

    if fullResult == True:
        result = result.set_index([fields, "Kelompok", "Jenis", "Satuan"])
        return {
            "kelompok": group,
            "data": result,
        }

    else:
        return result


# ektraks multiple data
def bulk_parse(pathInput, pathOutput, fileType="csv", separator=" "):
    """Fungsi yang bertujuan untuk mengekstrak data dalam jumlah besar. Data tersebut diekstrak pada lokasi output yang diinginkan.

    :param pathInput: lokasi data bps
    :param pathOutput: lokasi output data bps
    :param separator: tanda pisah yang digunakan
    """
    listDataBPS = glob.glob(pathInput)
    listFileType = ["csv", "xlsx"]
    listDf = []

    if fileType == "csv":
        listDf = list(
            pd.read_csv(i).pipe(bps_parse, separator=separator, fullResult=True)
            for i in listDataBPS
        )

    elif fileType == "xlsx":
        listDf = list(
            pd.read_excel(i).pipe(bps_parse, separator=separator, fullResult=True)
            for i in listDataBPS
        )

    listUniqueGroup = set([Df["kelompok"] for Df in listDf])
    for id, uniqueGroup in enumerate(listUniqueGroup):
        sameDf = [Df["data"] for Df in listDf if Df["kelompok"] == uniqueGroup]
        fileNames = f"{pathOutput}/Hasil_Ekstrak_{id}.csv"
        print(f"Mengekstrak {fileNames}")
        pd.concat(sameDf, axis=1).to_csv(fileNames)
