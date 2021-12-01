#!/usr/bin/python3

from login_details import engine1
from sqlalchemy import MetaData, Integer, Boolean, Column, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
meta = MetaData(bind=None)


class ln_stoppages_production(Base):
    __tablename__ = 'ln_stoppages_production'

    id = Column(Integer, primary_key=True, )
    stoppage_id = Column(Integer)
    from_datetime = Column(DateTime)
    until_datetime = Column(DateTime)
    line_stopped = Column(Boolean)

   # meta.create_all(engine1)


class dg_ln_stoppages_production:
    table = Table(
        'dg_ln_stoppages_production', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('stoppage_id', Integer),
        Column('from_datetime', DateTime),
        Column('until_datetime', DateTime),
        Column('line_stopped', Boolean)
    )


'''
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
'''
