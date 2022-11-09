# BPS Parse

Program ini berfungsi untuk mengesktrak data-data esensial dari data BPS
sehingga memudahkan pengguna dalam menyiapkan data sebelum melakukan analisis.
Python digunakan pada proyek ini karena memiliki librari atau modul yang mencukupi untuk kebutuhan ekstraksi seperti **pandas**.

# Data BPS
Secara umum data yang tersedia di BPS memiliki format excel (**xlsx**)
sehingga perlu dikonversi menjadi format **csv** untuk memudahkan analisis. Data yang akan diolah pada program ini merupakan data produksi komoditi suatu wilayah yang memiliki variasi terhadap golongan, jenis dan tahun. Sebagai contoh, data yang digunakan merupakan beberapa data komoditi di Sumatera Selatan.

Data BPS memiliki format khusus seperti tabel pivot yang merangkum data dalam beberapa tahun.
![Contoh data awal](/img/awal.png)

Program ini dapat mengeksrak data esensia dan merubahnya ke dalam format yang lebih mudah untuk dianalisis.
![Contoh hasil](/img/akhir.png)

