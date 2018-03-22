"""@package sql
Requires pymysql module to be installed first.
Wrapper functions/driver interface for accessing MySQL Database.
"""

import pymysql


class MySql:
    """ Class MySQL
    Functions:
    __init__(self, db_name), connect(self), version(self), query(self), insert(self), delete(self)
    update(self), read(self), disconnect(self)
    """
    def __init__(self, db_name):
        """
        Constructor for MySQL Class.
        :param db_name: Name of the MySQL Database to connect to.
        It is assumed that the "@param"  database is present in MySQL Database.
        """

        self.db_ip = "10.114.70.201"    # IP address of MySQL Database Machine
        self.uid = "root"		        # USER ID of the SQL ADMIN
        self.pwd = "root"		        # PASSWORD of the SQL ADMIN
        self.db_name = db_name          # DATABASE name to connect to
        self.db = None
        self.cursor = None

    def connect(self):
        """
        Connect to the MySQL Database using the provided USER ID and PASSWORD.
        :return: None
        """
        self.db = pymysql.connect(self.db_ip, self.uid, self.pwd, self.db_name)
        self.cursor = self.db.cursor()

    def version(self):
        """
        Check the SQL Database Version and prints on console.
        :return: None
        """
        self.cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = self.cursor.fetchone()
        print("Database version : %s " % data)

    def query(self, sql):
        """
        Run a SQL query on the MySQL Database.
        :param sql: Query to be run on the SQL Server.
        :return: result of the SQL Query.
            If query is successful -> Result of the query as tuples/list.
            If query is unsuccessful -> None
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insert(self, sql):
        """
        Insert a record into the MySQL Database.
        :param sql: INSERT query that has to be run on the MySQL Database.
        :return: None.
            If query is successful -> A record gets inserted in MySQL Database.
            If query is unsuccessful -> No Changes made to the existing MySQL Database.
        """
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

    def delete(self, sql):
        """
        Delete a record from the MySQL Database.
        :param sql: DELETE query that has to be run on the MySQL Database.
        :return: None.
            If query is successful -> A record gets deleted from MySQL Database.
            If query is unsuccessful -> No Changes made to the existing MySQL Database.
        """
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

    def update(self, sql):
        """
        Update a record into the MySQL Database.
        :param sql: Update query that has to be run on the MySQL Database.
        :return: None.
            If query is successful -> An existing record gets updated with new values in MySQL Database.
            If query is unsuccessful -> No Changes made to the existing MySQL Database.
        """
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

    def disconnect(self):
        """
        Disconnect from the MySQL Database.
        :return: None
        """
        self.db.close()

