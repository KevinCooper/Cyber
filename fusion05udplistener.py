import socket, struct, binascii

UDP_IP = "192.168.72.145"
UDP_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	#data, addr = sock.recvfrom(4)
	#ip, addr = sock.recvfrom(4)
	#print "Flag addr:%r, ip addr: %r" % (hex(struct.unpack("<I", data)[0]), ip )
	data, addr= sock.recvfrom(1024)
	print binascii.hexlify(data)
