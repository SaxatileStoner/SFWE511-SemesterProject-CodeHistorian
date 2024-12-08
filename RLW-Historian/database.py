"""
Contains all functions utilized to communicate to the sqlite database
"""
from sqlite3 import Connection
import sqlite3
from typing import Union


def create_sql_connection(path: str) -> Union[Connection, None]:
    """
    Attempts to connect to the sqlite database given the path to it.
    :param path: Path where the sqlite file is stored
    :return connection: Returns a connection to the sqlite file, or None if it failed.
    """
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connected to SQLite DB!")
    except Exception as e:
        print(f"SQLite Database Connection Error! {e}")
    return connection


def initialize_table(connection: Connection) -> None:
    """
    Initializes the database tables given a connection to database
    :param connection: connection to database
    :return void:
    """
    init_query_str = """
    CREATE TABLE IF NOT EXISTS {table_name} (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Time TEXT NOT NULL,
        Name TEXT NOT NULL,
        LocationType TEXT NOT NULL,
        Location INTEGER NOT NULL,
        Type TEXT NOT NULL,
        Value {value_type}
    );
    """
    input_registers_table_query = init_query_str.format(table_name = "InputRegister", value_type = "INTEGER")
    input_statuses_table_query = init_query_str.format(table_name = "InputStatus", value_type = "BOOLEAN")
    holding_registers_table_query = init_query_str.format(table_name = "HoldingRegister", value_type = "INTEGER")
    coil_statuses_table_query = init_query_str.format(table_name = "CoilStatus", value_type = "BOOLEAN")

    cursor = connection.cursor()
    try:
        cursor.execute(input_registers_table_query)
        cursor.execute(input_statuses_table_query)
        cursor.execute(holding_registers_table_query)
        cursor.execute(coil_statuses_table_query)
        connection.commit()
        print("Table Initialization Complete!")
    except Exception as e:
        print(f"SQLite Initialize Table Error! {e}")

# Raw insert query data for a value that is of type string
raw_insert_query_value_str = """
INSERT INTO {table} (Time, Name, LocationType, Location, Type, Value)
VALUES ('{time}', '{name}', '{location_type}', {location}, '{type}', '{value}');
"""

# Raw insert query data for a value that is of type integer
raw_insert_query_value_int = """
INSERT INTO {table} (Time, Name, LocationType, Location, Type, Value)
VALUES ('{time}', '{name}', '{location_type}', {location}, '{type}', {value});
"""

def insert_table_input_registers(connection: Connection, entry: list) -> None:
    """
    Inserts data into input register table
    :param connection: Connection to database
    :param entry: list that contains a single unit of entry data
    :return void:
    """
    insert_query = raw_insert_query_value_int.format(
        table = "InputRegister",
        time = entry[0],
        name = entry[1],
        location_type = entry[2],
        location = entry[3],
        type = entry[4],
        value = entry[5]
    )

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query)
        connection.commit()
    except Exception as e:
        print(f"SQLite Insert to Table InputRegister failed! {e}")

def insert_table_input_statuses(connection: Connection, entry: list) -> None:
    """
    Inserts data into input status table
    :param connection: Connection to database
    :param entry: list that contains a single unit of entry data
    :return void:
    """
    insert_query = raw_insert_query_value_str.format(
        table = "InputStatus",
        time=entry[0],
        name=entry[1],
        location_type=entry[2],
        location=entry[3],
        type=entry[4],
        value=entry[5]
    )

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query)
        connection.commit()
    except Exception as e:
        print(f"SQLite Insert to Table InputStatus failed! {e}")

def insert_table_holding_registers(connection: Connection, entry: list) -> None:
    """
    Inserts data into holding register table
    :param connection: Connection to database
    :param entry: list that contains a single unit of entry data
    :return void:
    """
    insert_query = raw_insert_query_value_int.format(
        table="HoldingRegister",
        time=entry[0],
        name=entry[1],
        location_type=entry[2],
        location=entry[3],
        type=entry[4],
        value=entry[5]
    )

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query)
        connection.commit()
    except Exception as e:
        print(f"SQLite Insert to Table HoldingRegister failed! {e}")

def insert_table_coil_statues(connection: Connection, entry: list) -> None:
    """
    Inserts data into coil status table
    :param connection: Connection to database
    :param entry: list that contains a single unit of entry data
    :return void:
    """
    insert_query = raw_insert_query_value_str.format(
        table="CoilStatus",
        time=entry[0],
        name=entry[1],
        location_type=entry[2],
        location=entry[3],
        type=entry[4],
        value=entry[5]
    )

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query)
        connection.commit()
    except Exception as e:
        print(f"SQLite Insert to Table CoilStatus failed! {e}")