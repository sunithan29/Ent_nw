#! /usr/bin/python3

"""@module main
Main module, combining all the classes and modules for Enterprise Network Monitoring and Security.

Requires:
stats_generator, analyzer, scapy, process and Semaphore from multiprocessing
"""

from stats_generator import *
from analyzer import *
from scapy.all import *
from multiprocessing import Process, Semaphore

sem = Semaphore(CAPTURETHREADLIMIT)     # Semaphore declaration for limiting the parallel capture threads.


def captureThread(command, id):
    """
    Captures the network traffic in promiscuous mode on the Network Interface Cards.
    :param command: Accepts String, executes received string on Linux Shell
    :param id: Number to identify which thread is capturing the network traffic
    :return: None
    """
    try:
        sem.acquire()
        subprocess.call(command, shell=True)
    except KeyboardInterrupt:
        print("\n[*] Thread " + str(id) + " Ended.")
    finally:
        sem.release()
        print("\n[*] Capture Process Terminated.")


def main():
    command = []        # Holds the command strings to be executed for NIC traffic capture
    processes = []      # Holds the list of process objects running parallel

    # Create an object of Statistics class; Refer statistics documentation for further information.
    stats = Statistics()
    processes.append(Process(target=stats.generate))
    processes.append(Process(target=calculateSpeed))

    processes[0].start()
    processes[1].start()

    i = 3               # Holds index for processes
    idx = 0             # Index for threads in capture process

    # Create an object of Analyzer class; Refer analyzer class documentation for further information.
    test = Analyzer(0)
    processes.append(Process(target=test.netfiler))

    processes[2].start()

    # Generate command string for network traffic capture.

    for iFace in INTERFACE:
        command.append("sudo dumpcap -i " + iFace + " -b filesize:" + str(FILESIZE) +
                       " -B " + str(BUFFERSIZE) + " -w " + RAWLOG + "/" + FILENAME + "_" + iFace + "." + EXTENSION)
        idx += 1

    # Start network traffic capture processes
    for c in command:
        processes.append(Process(target=captureThread, args=(c, i)))
        processes[i].start()
        i += 1

    try:
        for p in processes:
            p.join()    # Wait fo the processes to finish.
    except KeyboardInterrupt:
        print("[*] Keyboard Interrupt Received...")
        for p in processes:
            p.kill()
    finally:
        print("[*] Done")
        sys.exit(0)

if __name__ == "__main__":
    main()
