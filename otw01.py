import socket
import struct
import binascii
def main():
        print "Start"
        so = socket.socket()
        so.connect(('vortex.labs.overthewire.org',5842))
        sum = 0;
        for x in xrange(4):
		
                byte = so.recv(4)
		print "Hex: " +str(binascii.hexlify(byte))
                sum+=  struct.unpack('<I',byte)[0]
		print "Int value: "+ str(struct.unpack('<I',byte)[0])
		print "Running sum: "+str( sum)
        print "Sum is :" + str(sum)
        so.sendall(struct.pack("<I", (sum & 0xFFFFFFFF)))
        print so.recv(1024)
main()

#password: Gq#qu3bF3
