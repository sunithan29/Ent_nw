#! /usr/bin/python3

"""@module fetch_database
- fetch_databse module contains definition of class Fetch.
- It is used to interact with the distributed MySQL Server(s) where the additional feature information is logged
with the timestamp values.
- This information is used in analyzer class and is appended to the flow features.
- It is then used as features required to train the machine learning algorithm in the Classifier class.

Requires:
Timer from threading, MySql from sql, RepeatedTimer from constants
"""

from threading import Timer
from sql import MySql
from constants import RepeatedTimer

EXEC_INTERVAL = 5


class Fetch:
    """Class Fetch
    Functions:
    __init__(self), fetch(self, table), finish(self)
    """
    def __init__(self):
        """
        Constructor for Fetch Class.
        """
        self.database_object = MySql("Features")
        self.database_object.connect()

    def fetch(self, table):
        """
        - Fetches all records from the table specified.
        :param table: Name of the table present in the MySQL database.
        :return: Dictionary of the records.
        """
        if table == "failed_login":
            #print('\n[*] Fetching \"Failed Login\" table.')
            sql = """SELECT * FROM failed_login"""
            result = self.database_object.query(sql)
            flowpara = {}
            if len(result) > 0:
                #print(result)
                query = """DELETE FROM `failed_login` WHERE 1"""
                answer = self.database_object.delete(query)
                print(answer)
                for each in result:
                    if each[0] not in flowpara.keys():
                        flowpara[each[0]] = []
                    flowpara[each[0]].append(each[1])
                return flowpara
            else:
                #print("[*] Let the other guy write first...\n")
                return {}
        else:
            print("\n[*] Table \"" + table + "\" not found in the database.")

    def finish(self):
        """
        - Disconnects from the database for graceful exit.
        :return: None
        """
        self.database_object.disconnect()


#def repeat():
#    temp = Fetch()
#    tables = ['failed_login']
#    for t in tables:
#        a = temp.fetch(t)
#        print(a)
#    temp.finish()

#rt = RepeatedTimer(EXEC_INTERVAL, repeat)
#repeat()
