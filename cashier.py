import numpy as np
import pandas as pd
import pytz
import datetime
from tabulate import tabulate


class Transaction:
    """Berisi fungsi dasar dalam program kasir"""

    # Initiate empty dict and assign to DataFrame
    empty_dict = {"Item": [], "JumlahBarang": [], "Harga": []}
    data = pd.DataFrame(empty_dict)

    def __init__(self):
        self.nama_toko = "Supermarket Andi"
        self.alamat = "Kota Besar"
        self.no_telepon = "08098888"
        # Initiate current time
        now = datetime.datetime.now()
        # Create date, timezone jakarta
        self.date = (
            pytz.timezone("Asia/Jakarta").localize(now).strftime("%Y-%m-%d")
        )
        # Create time, timezone jakarta
        self.created_at = (
            pytz.timezone("Asia/Jakarta").localize(now).strftime("%H:%M:%S")
        )
        # Created timestamp
        self.timestamp = now.timestamp()

    def add_item(
        self, nama_item: str, jumlah_item: int, harga_item: float or int
    ):
        """Fungsi untuk menambahkan nama_item, jumlah_item, harga_item
            ke dalam attribute class data

        Args:
            nama_item (str): nama item
            jumlah_item (int): jumlah item
            harga_item (float or int): harga per item

        Raises:
            TypeError:
                Jika parameter nama_item bukan string
            TypeError:
                Jika parameter jumlah_item bukan integer
            TypeError:
                Jika parameter harga_item bukan float atau integer
        """

        # Check type of data parameter nama_item
        if type(nama_item) != str:
            raise TypeError(
                "Parameter 'nama_item' harus memiliki tipe data 'str'"
            )
        # Check type of data parameter jumlah_item
        elif type(jumlah_item) != int:
            raise TypeError(
                "Parameter 'jumlah_item' harus memiliki tipe data 'int'"
            )
        # Check type of data parameter harga_item
        elif type(harga_item) != float and type(harga_item) != int:
            raise TypeError(
                "Parameter 'harga_item' memiliki tipe data 'float' atau 'int'"
            )
        else:
            # Assign parameter into attribute class data
            self.data.loc[len(self.data)] = [
                nama_item,
                jumlah_item,
                harga_item,
            ]
            print("Item yang Anda masukan:")
            print(f"Nama Item     : {nama_item}")
            print(f"Jumlah Barang : {jumlah_item}")
            print(f"Harga per-Item: Rp. {harga_item}")

    def update_item_name(self, nama_item: str, update_nama_item: str):
        """Fungsi untuk mengupdate nama_item jika nama_item terdapat
            dalam attribute class data

        Args:
            nama_item (str): nama item lama
            update_nama_item (str): nama item baru

        Raises:
            ValueError:
                Jika nama_item tidak terdapat dalam attribute class data
            TypeError:
                Jika parameter nama_item bukan string
            TypeError:
                Jika parameter update_nama_item bukan string
        """
        # Create list of all item in attribute class data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError
            else:
                # Check type of data parameter nama_item
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )
                # Check type of data parameter update_nama_item
                elif type(update_nama_item) != str:
                    raise TypeError(
                        "Parameter 'update_nama_item' memiliki tipe data 'str'"
                    )
                else:
                    # Filter by name_item
                    # assign update_nama_item in attribute class data
                    self.data.loc[
                        self.data.Item == nama_item, "Item"
                    ] = update_nama_item
                    print(
                        f"Anda merubah {nama_item} menjadi {update_nama_item}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam sesi transaksi ini")

    def update_item_qty(self, nama_item: str, update_jml_item: int):
        """Fungsi untuk mengupdate jumlah_item dalam jika nama_item
            terdapat dalam attribute class data

        Args:
            nama_item (str):
                    nama item sebagai keys untuk mengupdate jumlah_item
            update_jml_item (int):
                    value jumlah_item baru yang akan di update

        Raises:
            ValueError:
                Jika nama_item tidak terdapat dalam attribute class data
            TypeError:
                Jika parameter nama_item bukan string
            TypeError:
                Jika parameter update_jml_item bukan integer
        """

        # Create list of all item in attribute class data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError
            else:
                # Check type of data parameter nama_item
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )
                # Check type of data parameter update_jml_item
                elif type(update_jml_item) != int:
                    raise TypeError(
                        "Parameter 'update_jml_item' memiliki tipe data 'int'"
                    )
                else:
                    # Filter by nama_item
                    # assign update_jml_item in attribute class data
                    self.data.loc[
                        self.data.Item == nama_item, "JumlahBarang"
                    ] = update_jml_item
                    print(
                        f"Anda merubah Jumlah {nama_item} menjadi {update_jml_item}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam sesi transaksi ini")

    def update_item_price(self, nama_item: str, update_harga: float or int):
        """Fungsi untuk mengupdate harga dalam jika nama_item terdapat
            dalam attribute class data

        Args:
            nama_item (str): nama item sebagai keys untuk mengupdate harga
            update_harga (float / int): value harga baru yang akan di update

        Raises:
            ValueError:
                Jika nama_item tidak terdapat dalam attribute class data
            TypeError:
                Jika parameter nama_item bukan string
            TypeError:
                Jika parameter update_harga bukan integer atau float
        """
        # Create list of all item in attribute class data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError

            else:
                # Check type of data parameter nama_item
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )

                # Check type of data parameter update_harga
                elif type(update_harga) != float and type(update_harga) != int:
                    raise TypeError(
                        "Parameter 'update_harga' memiliki tipe data float/int"
                    )

                else:
                    # Filter by nama_item
                    # assign update_harga in attribute class data
                    self.data.loc[
                        self.data.Item == nama_item, "Harga"
                    ] = update_harga
                    print(
                        f"Anda merubah harga {nama_item} menjadi {update_harga}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam sesi transaksi ini")

    def delete_item(self, nama_item: str):
        """Fungsi untuk menghapus salah satu item yang terdapat dalam
            attribute class data

        Args:
            nama_item (str): nama_item yang ingin dihapus

        Raises:
            ValueError:
                Jika nama_item tidak terdapat dalam attribute class data
            TypeError:
                Jika parameter nama_item bukan string

        Returns:
           table : order tabel dengan attribute class data yang masih aktif
        """

        # Create list of all item in attribute class data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError

            else:
                # Check type of data parameter nama_item
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )
                else:
                    # Show deleted item
                    print(
                        f"Anda telah menghapus item {nama_item} dari transaksi"
                    )

                    # Filter and drop by nama_item
                    data = self.data.drop(
                        self.data.index[self.data.Item == nama_item],
                        inplace=True,
                    )

                    # Assign and show table
                    table = tabulate(data, headers="keys", tablefmt="psql")

                    return print(table)

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam sesi transaksi ini")

    def reset_transaction(self):
        """Fungsi untuk menghapus semua item dalam attribute class data

        Returns:
            table: order tabel kosong
        """

        # Show blank table
        print("Semua item berhasil di delete!")

        # Drop index in attribute class data
        self.data.drop(self.data.index, inplace=True)

        # Create  and show table
        table = tabulate(self.data, headers="keys", tablefmt="psql")

        return print(table)

    def check_order(self):
        """Fungsi untuk menghitung dan menampilkan total harga untuk tiap item

        Returns:
            table: Tabel order dengan total harga untuk tiap transaksinya
        """

        # Copy attribute class data
        output_data = self.data.copy()

        # Create new column
        output_data["TotalHarga"] = (
            output_data.JumlahBarang * output_data.Harga
        )
        # Create and show table
        table = tabulate(output_data, headers="keys", tablefmt="psql")

        return print(table)

    def total_price(self):
        """Fungsi untuk menghitung total transaksi beserta diskonnya

        Returns:
            int : total transaksi
        """
        # Copy attribute class data
        output_data = self.data.copy()
        # Create new column
        output_data["TotalHarga"] = (
            output_data.JumlahBarang * output_data.Harga
        )
        # Assign variable total payment
        total = np.sum(output_data.TotalHarga)

        # If total payment les than 200.000 get normal price
        if total >= 0 and total <= 200_000:
            return print(f"Total Transaksi Anda adalah Rp.{int(total)}")

        # if total paymen more than 200.000 and less than 300.000
        # Get 5 percent discount
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(
                f"Total Transaksi Anda adalah Rp.{int(total_belanja)}"
            )

        # if total paymen more than 300.000 and less than 500.000
        # Get 8 percent discount
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(
                f"Total Transaksi Anda adalah Rp.{int(total_belanja)}"
            )

        # if total paymen more than 500.000, get 10 percent discount
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(
                f"Total Transaksi Anda adalah Rp.{int(total_belanja)}"
            )

        else:
            return "Total Belanja Tidak Boleh Negatif"
