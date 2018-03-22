# Packet Object Structure

FLAGS = {'F': 'FIN', 'S': 'SYN', 'R': 'RST',
         'P': 'PSH', 'A': 'ACK', 'U': 'URG',
         'E': 'ECE', 'C': 'CWR'}

class Packet:
    def __init__(self, packet):

        if packet is None:
            self.timestamp = None
            self.proto = None
            self.source = None
            self.dest = None
            self.size = None
            self.flags = None
            self.key = None
        else:
            self.timestamp = packet[0]
            self.proto = int(packet[1])
            self.source = packet[2]
            self.dest = packet[3]
            self.size = packet[4]
            self.flags = packet[5]

            if self.source < self.dest:
                self.key = self.source + self.dest
            else:
                self.key = self.dest + self.source

    def print_obj(self):
        print(str(self.timestamp) + ", " + str(self.proto) + ", " + str(self.source)
              + ", " + str(self.dest) + ", " + str(self.size) + ", " + str(self.key))

    '''    def print_obj(self):
        print(str(self.timestamp) + ", " + str(self.proto) + ", " + str(self.source)
              + ", " + str(self.dest) + ", " + str(self.size) + ", " + str(self.flags) + ", " + str(self.key))'''
