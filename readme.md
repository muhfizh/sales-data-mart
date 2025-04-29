# Data Mart Project

Proyek ini membuat proses ETL sederhana dari data `sales`, `product`, dan `wilayah` untuk membangun sebuah Data Mart menggunakan PostgreSQL.

## Struktur Proyek

- **Data/**
  - sales.csv
  - product.csv
  - wilayah.csv
- **etl_process.py**
  - Script ETL untuk Extract → Transform → Load data ke PostgreSQL.
- **.env**
  - Menyimpan informasi koneksi database.

## Proses ETL

### Extract

- Membaca file CSV menggunakan pandas.

### Transform

- Menghapus data yang null/missing.
- Menghapus duplikat.
- Membuat kolom tambahan untuk tabel sales:
  - `total` = `quantity` × `price_per_unit`
  - `total_with_discount` = `total` - `discount`

### Load

- Membuat tabel PostgreSQL jika belum ada.
- Insert data ke masing-masing tabel: `sales`, `product`, `wilayah`.

## Prasyarat

- Python 3.x
- Library Python:
  - pandas
  - psycopg2
  - python-dotenv
- PostgreSQL Database

## Cara Menjalankan

1. Install library:

```bash
pip install pandas psycopg2-binary python-dotenv
```

2. Buat file `.env`:

```dotenv
DB_NAME=nama_database
DB_USER=username_database
DB_PASSWORD=password_database
DB_HOST=localhost
DB_PORT=5432
DB_SCHEMA=public
```

3. Jalankan script:

```bash
python Data_Mart.py
```

## Catatan

- Pastikan database dan schema sudah tersedia.
- Pastikan file CSV berada di folder `Data/`.
