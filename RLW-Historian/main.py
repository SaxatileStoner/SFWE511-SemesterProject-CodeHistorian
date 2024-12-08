"""
Program connects to `127.0.0.1` and reads data from OpenPLC Runtime, then stores it in /db/database.sqlite
@institution University of Arizona - SFWE 511 - Fall 2024
@author Christopher Stoner
"""

from pymodbus.pdu import ModbusPDU
import pymodbus.pdu.register_read_message
import pymodbus.pdu.bit_read_message
from pymodbus.client import ModbusTcpClient
from datetime import datetime
import time
from data_enum import InputRegister as InputRegister
from data_enum import InputStatus as InputStatus
from data_enum import HoldingRegister as HoldingRegister
from data_enum import CoilStatus as CoilStatus
import database

# Config
plc_runtime_address = "127.0.0.1"
client = ModbusTcpClient(plc_runtime_address)
path_to_db = "../db/database.sqlite"

def compile_data_to_list(enum_data: [InputRegister, InputStatus, HoldingRegister, CoilStatus],
                         time_stamp: datetime,
                         register_data: ModbusPDU) -> list:
    """
    Compiles a list from a register enum data type, a given time_stamp when the data was created,
    and the value of the data.

    :param enum_data: Enum Data gives specific name and location value for each register/coil in PLC
    :param time_stamp: This is the time in which the data was collected from the PLC
    :param register_data: This contains the actual data of that register/coil from the PLC, can read either bits or registers
    :return append_list: Returns a list of appended values from the data entry created for each register/coil
    """
    append_list = []
    if type(register_data) == pymodbus.pdu.register_read_message.ReadInputRegistersResponse or \
        type(register_data) == pymodbus.pdu.register_read_message.ReadHoldingRegistersResponse:
        for i in range(enum_data.__len__()):
            append_list.append(
                [
                     time_stamp.__str__(),
                     enum_data(i).name,
                     enum_data.__name__,
                     enum_data(i).value,
                     "int",
                     register_data.registers[i]
                ])
    elif type(register_data) == pymodbus.pdu.bit_read_message.ReadDiscreteInputsResponse or \
            type(register_data) == pymodbus.pdu.bit_read_message.ReadCoilsResponse:
        for i in range(enum_data.__len__()):
            append_list.append([
                     time_stamp.__str__(),
                     enum_data(i).name,
                     enum_data.__name__,
                     enum_data(i).value,
                     "boolean",
                     register_data.bits[i]
                ])

    return append_list

# Database Initialization
print("Connecting to Database...")
db_connection = database.create_sql_connection(path_to_db)
print("Initializing Database...")
database.initialize_table(db_connection)

# Main Program Loop Here
try:
    # Client Connect to OpenPLC Runtime Server
    while client.connect():
        print("Reading OpenPLC Runtime Server...")
        # Read Registers and Coils, Get Time After Read
        input_registers = client.read_input_registers(0,InputRegister.__len__(), 1)
        input_register_time = datetime.now()

        input_statuses = client.read_discrete_inputs(0, InputStatus.__len__(), 1)
        input_status_time = datetime.now()

        holding_registers = client.read_holding_registers(0, HoldingRegister.__len__(), 1)
        holding_register_time = datetime.now()

        coil_statuses = client.read_coils(0, CoilStatus.__len__(), 1)
        coil_status_time = datetime.now()

        print("Compiling Data...")
        # Compile data to be stored as [TIME, NAME, LOCATION_TYPE, LOCATION, TYPE, VALUE]
        database_entries_as_lists = [compile_data_to_list(InputRegister, input_register_time, input_registers),
                              compile_data_to_list(InputStatus, input_status_time, input_statuses),
                              compile_data_to_list(HoldingRegister, holding_register_time, holding_registers),
                              compile_data_to_list(CoilStatus, coil_status_time, coil_statuses)]

        # Insert data into database
        print("Adding Entries to Database...")
        for locational_type in database_entries_as_lists:
            for entry in locational_type:
                match entry[2]:
                    case "InputRegister":
                        database.insert_table_input_registers(db_connection, entry)
                        pass
                    case "InputStatus":
                        database.insert_table_input_statuses(db_connection, entry)
                        pass
                    case "HoldingRegister":
                        database.insert_table_holding_registers(db_connection, entry)
                        pass
                    case "CoilStatus":
                        database.insert_table_coil_statues(db_connection, entry)
                        pass

        # Sleep for 30 Seconds and continue loop
        print("Loop Complete! Sleeping for 30 seconds...")
        print("-"*50)
        time.sleep(30)
    else:
        print("Connection Failed! Check IP address or make sure OpenPLC Runtime.")
except KeyboardInterrupt:
    print("Stopping Program...")
    print("Closing connection to OpenPLC Runtime Server...")
    client.close()
    print("Closing connection to database...")
    db_connection.close()
    print("Goodbye!")