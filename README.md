# *Python Project: Self-Service Cashier*

## Latar Belakang Problem

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan ekspansi bisnis, yaitu: Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah yang dibeli dan fitur lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

## *Tools*
### Bahasa Pemograman:
- Python

### *Libraries*:
- Pandas
- NumPy
- pytz
- datetime
- tabulate

## *Requirements / Objectives*
### Tujuan Pembelajaran:
- Membuat *Self-Service Cashier* menggunakan Python
- Menggunakan OOP dalam pembuatan program Python
- Mengaplikasikan *Data Structure, Branching, try, and error* pembuatan program Python
- Membuat dokumentasi *docstring* pembuatan program Python
- Mengaplikasikan PEP8 dalam penulisan *clean code* pada program Python

### Tujuan Program:
- Membuat objek dari `class Transaction()`
- Menambahkan *method* `add_item()` yang berisi parameter `nama_item`, `jumlah_item`, dan `harga_per_item` ke dalam *Self-Service Cashier*
- Menambahkan *method* `update_item_name()`, `update_item_qty()`, dan `update_item_price()`. Mengubah berdasarkan parameter `nama_item` untuk mengubah nilai tiap-tiap item, jumlah, dan harga ke dalam *Self-Service Cashier*. 
- Menambahkan *method* `delete_item()`ke dalam *Self-Service Cashier* untuk menghapus satu item berdasarkan parameter `nama_item`
- Menambahkan *method* `reset_transaction()` ke dalam *Self-Service Cashier* untuk menghapus semua transaksi
- Menambahkan *method* `check_order()` ke dalam *Self-Service Cashier* untuk melihat seluruh detail transaksi
- Menambahkan *method* `total_price()` ke dalam *Self-Service Cashier* untuk mengetahui total pembayaran, dengan beberapa ketentuan:
    - Jika total belanja di atas Rp.200.000 maka akan mendapatkan diskon 5%
    - Jika total belanja di atas Rp.300.000 maka akan mendapatkan diskon 8%
    - Jika total belanja di atas Rp.500.000 maka akan mendapatkan diskon 10%

## *Flowchart*

## *Function / Attribute*

- *attribute class* berisi dataframe kosong

- *attribute* mengenai toko atau transaksi
    ```python
    def ___init___:
        nama toko
        alamat
        nomor telepon
        tanggal
        waktu
        timestamp
    ```

- add_item menambahkan item, jumlah dan harga ke dalam sesi transaksi
    ```python
    def add_item(nama_item, jumlah_item, harga_item):
        cek tipe data parameter
        masukan parameter ke dalam attribute class
    ```

- update_item_name merubah nama item jika terjadi kesalahan input
    ```python
    def update_item_name(nama_item, update_nama_item):
        cek tipe data parameter
        cek nama item dalam attribute class
        merubah nama item dalam attribute class
    ```

- update_item_qty merubah jumlah item berdasarkan nama item jika terjadi kesalahan input
    ```python
    def update_item_qty(nama_item, update_jumlah_item):
        cek tipe data parameter
        cek nama item di dalam attribute class
        merubah jumlah item berdasarkan nama item
    ```

- update_item_price merubah harga item berdasarkan nama item jika terjadi kesalahan input
    ```python
    def update_item_qty(nama_item, update_harga_item):
        cek tipe data parameter
        cek nama item di dalam attribute class
        merubah harga item berdasarkan nama item
    ```

- delete_item menghapus satu baris berdasarkan nama_item dalam transaksi 
    ```python
    def delete_item(nama_item):
        cek tipe data parameter
        cek nama item di dalam attribute class
        menghapus jumlah dan harga berdasarkan nama item
    ```

- reset_transaction menghapus semua sesi transaksi
    ```python
    def reset_transaction():
        menampilkan pesan item sudah di reset
        menampilakn tabel kosong
    ```

- check_order menampilkan semua detail transaksi dalam bentuk tabel
    ```python
    def check_order():
        membuat dataframe baru dengan cara copy attribute class
        manambahkan kolom total harga untuk tiap item
        membuat dan menampilkan tabel
    ```

- total_price menampilkan total belanja dari sesi transaksi dengan ketentuan diskon
    ```python
    def total_transaction():
        membuat dataframe baru dengan cara copy attribute class
        manambahkan kolom total harga untuk tiap item
        menjumlahkan kolom total harga
        if total belanja < 200000:
            harga normal
        if total belanja < 30000:
            diskon 5 persen
        if total belanja < 500000:
            diskon 8 persen
        if total belanja > 500000:
            diskon 10 persen
    ```

## *Test Case*

1. Test Case 1 - Customer ingin menambahkan dua item menggunakan method `add_item()`. Item yang ditambahkan sebagai berikut:
    - Nama Item: Ayam Goreng, Qty: 2, Harga: 20.000
    - Nama Item: Pasta Gigi, Qty: 3, Harga: 15.000
&nbsp;

        ```python
        user = Transaction()
        # Test Case 1
        # Add Item 1
        print("Test Case 1")
        print("-----------")
        user.add_item("Ayam Goreng", 2, 20_000)
        print("\n")
        # Add Item 2
        user.add_item("Pasta Gigi", 3, 15_000)
        print("\n")
        print("Order Table :")
        user.check_order()
        user.total_price()
        ```

        Output:
        <img src="Project\assets\test-case-1.png" alt="MarineGEO circle logo" style="height: 100px; width:100px;"/>


## *Conclusion*
