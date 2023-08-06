from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def create_db():
    """
    Creates a SQLite database and a table named 'transactions'
    if it does not exist.

    This function creates a database engine for the SQLite database with
    the name 'andi-supermarket.db'. It then defines the SQL query to create
    the 'transactions' table with the following columns:
        - no_id: Integer, Primary Key, automatically generated transaction ID
        - nama_item: String, the name of the item
        - jumlah_item: Integer, the quantity of the item
        - harga: Integer, the price per item
        - total_harga: Integer, the total price for the items
        - diskon: Integer, the discount percentage applied to the total price
        - harga_diskon: Integer, the final price after applying the discount
        - timestamp: DateTime, the timestamp of the transaction,
                        defaulting to the current time

    The function then establishes a connection to the database and
    executes the SQL query to create the table.

    Raises:
        SQLAlchemyError: If there is an error creating the table.

    Example:
        create_db()

    Note:
        The database engine should be properly configured with
        the required dependencies before calling this function.
    """
    try:
        # Create a database engine for the SQLite database
        engine = create_engine("sqlite:///andi-supermarket.db")

        # Define the SQL query to create the 'orders' table
        query = text(
            """
        CREATE TABLE IF NOT EXISTS transactions(
            no_id INTEGER PRIMARY KEY,
            nama_item VARCHAR(255),
            jumlah_item INTEGER,
            harga INTEGER,
            total_harga INTEGER,
            diskon INTEGER,
            harga_diskon INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        )

        # Establish a connection to the database and execute the query
        with engine.connect() as conn:
            conn.execute(query)

    except SQLAlchemyError as error:
        # If an error occurs, print the error message
        print(f"Error creating table: {error}")


Base = declarative_base()


class Order(Base):
    """
    Represents the 'transactions' table in the database.

    This class defines the structure of the 'transactions' table in
    the database. It inherits from SQLAlchemy's declarative_base() class.

    Attributes:
        __tablename__ (str): The name of the table in the database,
                             set to 'transactions'.

        no_id (Column): Integer, Primary Key. Automatically generated
                        transaction ID.

        nama_item (Column): String, the name of the item.

        jumlah_item (Column): Integer, the quantity of the item.

        harga (Column): Integer, the price per item.

        total_harga (Column): Integer, the total price for the items.

        diskon (Column): Integer, the discount percentage applied to
                         the total price.

        harga_diskon (Column): Integer, the final price after
                               applying the discount.

    Example:
        Create an instance of the Order class:
        >>> order = Order(no_id=1, nama_item='Product A', jumlah_item=5,
                          harga=10000, total_harga=50000, diskon=10,
                          harga_diskon=45000)

        Note:
        To use this class, you need to import it into your database setup
        script and add it to the metadata of the database before creating
        the table.

    """

    __tablename__ = "transactions"
    no_id = Column(Integer, primary_key=True)
    nama_item = Column(String(255))
    jumlah_item = Column(Integer)
    harga = Column(Integer)
    total_harga = Column(Integer)
    diskon = Column(Integer)
    harga_diskon = Column(Integer)


def insert_to_table(data_list):
    """
    Inserts data into the 'orders' table using SQLAlchemy.

    Parameters:
        data_list (list of dict): A list of dictionaries where each dictionary
                                    contains the data for one entry.

    Example of data_list:
        [
            {
                'nama_item': 'Item A',
                'jumlah_item': 5, 'harga': 10000,
                'total_harga': 50000,
                'diskon': 10,
                'harga_diskon': 45000
            },
        ]
    """
    try:
        engine = create_engine("sqlite:///andi-supermarket.db")
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)

        # Use a context manager to manage the session
        with Session() as session:
            # Insert data for each entry in the data_list
            for entry in data_list:
                order = Order(**entry)
                session.add(order)

            # Commit the changes to the database
            session.commit()

    except SQLAlchemyError as error:
        print(f"Error inserting data: {error}")
