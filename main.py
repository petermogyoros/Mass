# This is a sample Python script.

from login_details import engine1
from sqlalchemy import create_engine, select, MetaData, Table, and_, func
from sqlalchemy.sql import text

meta = MetaData(bind=None)

class connect_to_db(database):
    table = Table(
        database,
        metadata,
        autoload=True,
        autoload_with=engine1
    )




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
