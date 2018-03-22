"""@module stat_generator
- Collection of functions and classes for generating the network related statistics.
- Extracts interface information and network speed of the interface.

Requires:
subprocess, time, psutil, MySql from sql, deque from collections, Thread from threading,
INTERFACE and RAWLOG from constants.
"""

from collections import deque
from threading import Thread
from sql import MySql
from constants import INTERFACE, RAWLOG
import psutil
import subprocess
import time


class Statistics:
    """Class statistics
    Functions:
    __init__(self), generate(self)
    """
    def __init__(self):
        """
        Constructor for statistics class.
        """
        self.cpu = 0                    # %CPU Usage
        self.memAvailablePercent = 0    # Available RAM Memory
        self.logSize = 0                # RAW Capture Size

    def generate(self):
        """
        - Repeats statistics extraction every one second.
        - Uses psutil module to connect to interface details and manually extracts required information.
        - Output of the extraction is writtn in CSV files.
        - Also connects to the MySQL Database to fetch failed login attempts and writes them in CSV files.
        - CSV files are used to display relevant statistics on the web page.
        :return: None
        """
        try:
            while True:
                self.cpu = psutil.cpu_percent(interval=1)   # CPU Usage in %

                mem = psutil.virtual_memory()               # Memory Usage
                self.memAvailablePercent = mem[2]

                command = "du -sh " + RAWLOG                # Folder Size
                a = subprocess.check_output(command, shell=True).strip().decode().split()
                self.logSize = a[0]

                b = psutil.net_io_counters(pernic=True)     # Network Interface information
                string1 = str(b[INTERFACE[0]][0]) + "," + str(b[INTERFACE[0]][1]) + "," + \
                          str(b[INTERFACE[0]][2]) + "," + str(b[INTERFACE[0]][3])
                string2 = str(b[INTERFACE[1]][0]) + "," + str(b[INTERFACE[1]][1]) + "," + \
                          str(b[INTERFACE[1]][2]) + "," + str(b[INTERFACE[1]][3])

                f = open('/var/www/html/data_guage.csv', "w")
                string = str(self.memAvailablePercent) + "," + str(self.cpu) + "," + str(self.logSize)
                f.write(string)
                f.close()

                f = open('/var/www/html/data_table1.csv', "w")
                f.write(string1)
                f.close()

                f = open('/var/www/html/data_table2.csv', "w")
                f.write(string2)
                f.close()

                temp = MySql("Failed_Logins")               # Number of failed logins.
                temp.connect()

                sql = "SELECT timestamp, COUNT(timestamp) AS a FROM failed_login GROUP BY timestamp HAVING COUNT(timestamp) >= 1 ORDER BY timestamp ASC"
                b = temp.query(sql)
                f = open("/var/www/html/health.csv", 'w')

                for tup in b:
                    string = tup[0] + "," + str(tup[1]) + "\n"
                    f.write(string)

                f.close()

                temp.disconnect()
                time.sleep(1)
        except KeyboardInterrupt:
                print("Exiting Stat Generator")


def calculateSpeed():
    # Create the ul/dl thread and a deque of length 1 to hold the ul/dl- values
    transfer_rate = deque(maxlen=1)
    t = Thread(target=calc_ul_dl, args=(transfer_rate,))

    # The program will exit if there are only daemonic threads left.
    t.daemon = True
    t.start()
    try:
        # The rest of your program, emulated by me using a while True loop
        while True:
            #print_rate(transfer_rate)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting Speed Calculator.")


def calc_ul_dl(rate, dt=3, interface=INTERFACE[0]):
    t0 = time.time()
    counter = psutil.net_io_counters(pernic=True)[interface]
    tot = (counter.bytes_sent, counter.bytes_recv)

    while True:
        last_tot = tot
        time.sleep(dt)
        counter = psutil.net_io_counters(pernic=True)[interface]
        t1 = time.time()
        tot = (counter.bytes_sent, counter.bytes_recv)
        ul, dl = [(now - last) / (t1 - t0) / 1000.0
                  for now, last in zip(tot, last_tot)]
        dl = (dl/1000)
        f = open("/var/www/html/data_speed.csv", "w")
        string = str(dl)
        f.write(string)
        f.close()
        rate.append((ul, dl))
        t0 = time.time()


def print_rate(rate):
    try:
        print('UL: {0:.0f} kB/s / DL: {1:.0f} kB/s'.format(*rate[-1]))
        pass
    except IndexError:
        print('UL: - kB/s/ DL: - kB/s')
