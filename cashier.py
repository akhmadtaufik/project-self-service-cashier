import pandas as pd
import pytz
import datetime

from tabulate import tabulate
from database import create_db, insert_to_table


class Transaction:
    """
    Represents a cashier transaction with basic functions.

    This class provides basic functionalities for a cashier transaction,
    including adding, updating, and deleting items. It also calculates the
    total price for each item and applies discounts based on the total price.

    Attributes:
        data (DataFrame): Pandas DataFrame to store the transaction items.
        nama_toko (str): The name of the supermarket.
        alamat (str): The address of the supermarket.
        no_telepon (str): The contact number of the supermarket.
        date (str): The current date in the format 'YYYY-MM-DD'.
        created_at (str): The current time in the format 'HH:MM:SS'.
        timestamp (float): The timestamp of the transaction creation.

    Example:
        Create a Transaction instance:
        >>> transaction = Transaction()

        Add an item to the transaction:
        >>> transaction.add_item("Product A", 2, 5000)

        Update the quantity of an item:
        >>> transaction.update_item_qty("Product A", 5)

        Calculate the total price and apply discounts for each item:
        >>> transaction.check_out()

    Note:
        The 'database' module is used to handle database-related operations.
        'create_db' creates the database and the 'transactions' table if they
            do not exist.
        'insert_to_table' is used to insert the transaction data into the
            table.

    """

    # Initiate empty dict and assign to DataFrame
    empty_dict = {"nama_item": [], "jumlah_item": [], "harga": []}
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

    def add_item(self, nama_item: str, jumlah_item: int, harga: float or int):
        """Fungsi untuk menambahkan nama_item, jumlah_item, harga_item
            ke dalam attribute class data

        Args:
            nama_item (str): nama item
            jumlah_item (int): jumlah item
            harga (float or int): harga per item

        Raises:
            TypeError:
                Jika parameter nama_item bukan string
            ValueError:
                Jika parameter jumlah_item bukan integer positif
            ValueError:
                Jika parameter harga bukan float atau integer positif
        """

        # Check type of data parameter nama_item
        if type(nama_item) != str:
            raise TypeError(
                "Parameter 'nama_item' harus memiliki tipe data 'str'"
            )

        # Check type of data parameter jumlah_item and ensure it is a
        # positive integer
        if not isinstance(jumlah_item, int) or jumlah_item < 0:
            raise ValueError(
                "Parameter 'jumlah_item' harus merupakan integer positif"
            )

        # Check type of data parameter harga and ensure it is a
        # positive float or integer
        if not (isinstance(harga, (float, int)) and harga >= 0):
            raise ValueError(
                "Parameter 'harga' harus merupakan float atau integer positif"
            )

        # Assign parameter into attribute class data
        self.data.loc[len(self.data)] = [
            nama_item,
            jumlah_item,
            harga,
        ]
        print("Item yang Anda masukan:")
        print(f"Nama Item     : {nama_item}")
        print(f"Jumlah Barang : {jumlah_item}")
        print(f"Harga per-Item: Rp. {harga}")

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
        list_nama_item = self.data["nama_item"].tolist()
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
                        self.data.nama_item == nama_item, "nama_item"
                    ] = update_nama_item
                    print(
                        f"Anda merubah {nama_item} menjadi {update_nama_item}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam sesi transaksi ini")

    def update_item_qty(self, nama_item: str, update_jml_item: int):
        """Fungsi untuk mengupdate jumlah_item jika nama_item terdapat dalam
           attribute class data.

        Args:
            nama_item (str):
                    Nama item sebagai kunci untuk mengupdate jumlah_item.
            update_jml_item (int):
                    Nilai jumlah_item baru yang akan diupdate.

        Raises:
            ValueError: Jika nama_item tidak terdapat dalam attribute class.
            TypeError: Jika parameter nama_item bukan string.
            ValueError: Jika parameter update_jml_item bukan integer positif.

        Returns:
            None
        """
        # Create list of all items in attribute class data
        list_nama_item = self.data["nama_item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError(
                    f"Item {nama_item} tidak ditemukan dalam sesi transaksi"
                )

            else:
                # Check type of data parameter nama_item
                if not isinstance(nama_item, str):
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )

                # Check type of data parameter update_jml_item and
                # ensure it is a positive integer
                if not isinstance(update_jml_item, int) or update_jml_item < 0:
                    raise ValueError()

                else:
                    # Filter by nama_item
                    # Assign update_jml_item in attribute class data
                    self.data.loc[
                        self.data.nama_item == nama_item, "jumlah_item"
                    ] = update_jml_item
                    print(
                        f"Anda merubah Jumlah {nama_item} -> {update_jml_item}"
                    )

        except ValueError:
            print("Parameter 'update_jml_item' harus integer positif")

    def update_item_price(self, nama_item: str, update_harga: float or int):
        """Fungsi untuk mengupdate harga jika nama_item terdapat dalam
        attribute class data.

        Args:
            nama_item (str): Nama item sebagai kunci untuk mengupdate harga.
            update_harga (float or int): Nilai harga baru yang akan diupdate.

        Raises:
            ValueError: Jika nama_item tidak terdapat dalam attribute class.
            TypeError: Jika parameter nama_item bukan string.
            ValueError: Jika parameter update_harga bukan integer positif.

        Returns:
            None
        """
        # Create list of all items in attribute class data
        list_nama_item = self.data["nama_item"].tolist()
        try:
            # Check parameter nama_item in list_nama_item
            if nama_item not in list_nama_item:
                raise ValueError(
                    f"Item {nama_item} tidak ditemukan dalam sesi transaksi"
                )
            else:
                # Check type of data parameter nama_item
                if not isinstance(nama_item, str):
                    raise TypeError(
                        "Parameter 'nama_item' harus memiliki tipe data 'str'"
                    )
                # Check type of data parameter update_harga and
                # ensure it is a positive number
                if not (
                    isinstance(update_harga, (float, int))
                    and update_harga >= 0
                ):
                    raise ValueError()
                else:
                    # Filter by nama_item
                    # Assign update_harga in attribute class data
                    self.data.loc[
                        self.data.nama_item == nama_item, "harga"
                    ] = update_harga
                    print(f"Anda merubah harga {nama_item} -> {update_harga}")
        except ValueError:
            print("Param 'update_harga' harus merupakan float/integer positif")

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
        list_nama_item = self.data["nama_item"].tolist()
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
                        self.data.index[self.data.nama_item == nama_item],
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
        output_data["total_harga"] = (
            output_data.jumlah_item * output_data.harga
        )
        # Create and show table
        table = tabulate(output_data, headers="keys", tablefmt="psql")

        return print(table)

    def check_out(self):
        """Fungsi untuk menghitung total harga dan diskon untuk tiap item.

        Returns:
        list: List of dictionaries berisi (nama_item, jumlah_item, harga,
              total_harga, diskon, harga_diskon).
        """
        # Create database if not exists
        create_db()

        # Copy attribute class data
        output_data = self.data.copy()

        # Create new columns for total_harga, diskon and harga_diskon
        output_data["total_harga"] = (
            output_data.jumlah_item * output_data.harga
        )
        output_data["diskon"] = 0
        output_data["harga_diskon"] = 0

        # Calculate discounts and final prices for each item
        for index, row in output_data.iterrows():
            total_harga = row["jumlah_item"] * row["harga"]
            diskon = 0
            harga_diskon = total_harga

            # Determine discount rates based on total_harga
            if total_harga > 500000:
                diskon = 0.07
            elif total_harga > 300000:
                diskon = 0.06
            elif total_harga > 200000:
                diskon = 0.05

            if diskon > 0:
                harga_diskon = total_harga - (total_harga * diskon)

            output_data.at[index, "diskon"] = int(diskon * 100)
            output_data.at[index, "harga_diskon"] = harga_diskon

        # Create and show table
        table = tabulate(output_data, headers="keys", tablefmt="psql")

        print("\n")
        print("Silahkan Lanjutkan Pembayaran")
        print(table)
        print(
            "----------------------------------------------------------------"
        )
        print(f"Total Pembayaran Anda adalah {output_data.harga_diskon.sum()}")

        # Convert the output_data to a list of dictionaries
        result_list = output_data.to_dict(orient="records")

        return insert_to_table(result_list)
