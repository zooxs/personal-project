# Analisis Hindcasting

Analisis ini bertujuan untuk memprediksi tinggi dan perioda gelombang signifikan di suatu peraian menggunakan data kecepatan angin. Standar yang digunakan pada analisi ini mengacu pada SPM 1984 (*Shore Protection Manual*).


## Modul

Terdapat beberapa modul atau librari yang digunakan untuk keperluan analisis, diataranya:

- Pandas untuk pengolahan data
- Matplotlib dan Windrose untuk visualisasi data

## Struktur Project

Project ini terdiri dari beberapa folder berisi data angin, hasil analisis dan *source* dari program yang dijalankan. Program tersebut terdiri 4 berkas yang memiliki fungsi masing-masing.

| Berkas                    	| Fungsi                                                        	|
|---------------------------	|---------------------------------------------------------------	|
| `ekstrak_data.py`         	| Mengekstrak dan mengkompilasi data mentah                     	|
| `gelombang_mask.py`       	| Menentukan gelombang maksimum setelah analisis hindcasting    	|
| `hindcasting.py`          	| Memprediksi tinggi gelombang menggunakan data kecepatan angin 	|
| `visualisasi_windrose.py` 	| Memvisualisasikan windrose                                    	|


```
wave-hindcasting/
├── data-angin/
│   ├── EmdIndonesia_S02.299_E104.853_2004.txt
│   └── ...
├── data_output/
│   └── ...
└── src/
    ├── ekstrak_data.py
    ├── gelombang_maks.py
    ├── hindcasting.py
    └── visualisasi_windrose.py
dataset.csv
fetch_efektif.csv
ref.bib
README.md
```

## Data

Secara umum data yang digunakan pada analisis ini ada 2 yaitu data angin dan panjang fetch efektif di perairan.

### Data angin

Pada data angin ada 2 informasi penting yang diperlukan yaitu waktu, kecepatan dan arah angin. Contoh data tersebut dapat dilihat pada folder `data_angin` yang berisi data untuk beberapa tahun.

### Panjang fetch efektif

Data ini merupakan jarak terjauh dari titik tinjau terhadap darata terdekat untuk setiap arah.



<img src="img/fetch.png" width="70%">

Panjang fetch efektif data dicari dengan persamaan berikut

$$ F_{eff} = \frac{\sum X \cos \alpha}{\sum \cos \alpha} $$

yang bersumber dari (Thoresen, 2003).

## Analisis

Terdapat beberapa tahapan dalam analisis ini

### Ekstraks data

Karena data angin berada dalam file yang terpisah, perlu dilakukan penyatuan dan pengampilan *field* atau kolom pada tabel yang dibutuhkan saja seperti waktu, kecepatan dan arah angin. Langkah ini dapat dilihat pada [tautan ini](./ekstrak_data.py). Hasil penggabungan disimpan kedalam file `dataset.csv`.

### Hindcasting


<img src="img/flowchart1.svg" width="70%">
<img src="img/flowchart2.svg" width="70%">
<img src="img/flowchart3.svg" width="70%">



Langkah ini terdapat pada [file](./hindcasting.py)

### Penentuan gelombang maksimum

Langkah ini dapat dilihat pada [file](./gelombang_maks.py).

### Visualisasi *Windrose*


<img src="data_output/windrose.png" width="70%">


Visualisasi tersebut dapat dibuat dengan menggunakan data kecepatan dan arah angin. Langkah tersebut dapat dilihat pada [file](./visualisasi_windrose.py)

