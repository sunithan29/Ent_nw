#! /usr/bin/python3

"""@module update_database
- update_database module contains Update class.
- This function is used on the distributed nodes present in the network for logging and reporting the features to
 a centralized MySQL Database.

Requires:
* from logparser, Timer from threading, MySql from sql, RepeatedTimer form constants
"""

from logparser import *
from threading import Timer
from sql import MySql
from constants import RepeatedTimer

EXEC_INTERVAL = 5


class Update:
    """Class Update
    Functions:
    __init__(self), upload(self, table), finish(self)
    """
    def __init__(self):
        """
        Constructor for Update Class.
        """
        self.database_object = MySql()
        self.database_object.connect()
        self.database_object.version()

    def upload(self, table):
        """
        - Uploads parsed information to the table specified.
        - Table has to be created before executing this function.
        :param table: Name of the table present in the MySQL database.
        :return: None
        """
        if table == "failed_login":
            #print('\n[*] Modifying \"Failed Login\" table.')
            string = parseErrorLog("error.log")
            sql = """SELECT * FROM failed_login"""
            result = self.database_object.query(sql)
            if len(result) > 0:
                #print("[*] Let the other guy read first...\n")
                return
            else:
                for k in string.keys():
                    for v in string[k]:
                        query = """INSERT INTO """ + table + """(ip_key, timestamp) VALUES (\"""" + \
                            str(k) + """\", \"""" + str(v) + """\");"""
                        #print(query)
                        self.database_object.insert(query)

                sql = """SELECT * FROM failed_login"""
                result = self.database_object.query(sql)
                print(result)
        else:
            print("\n[*] Table \"" + table + "\" not found in the database.")

    def finish(self):
        """
        - Disconnects from the database for graceful exit.
        :return: None
        """
        self.database_object.disconnect()


def repeat():
    """
    - Repeat the database updating process every EXEC_INTERVAL time interval.
    :return: None
    """
    temp = Update()
    tables = ['failed_login']
    for t in tables:
        temp.upload(t)
    temp.finish()

rt = RepeatedTimer(EXEC_INTERVAL, repeat)
