import socket, struct, binascii

def sendDb(s, ipv4, port):
	s.sendall("senddb "+ ipv4 + " " + port+"\n")
	print "Attempting to send the DB."

def addReg(s, name, ipv4):	
	s.sendall("addreg "+ name +" e0 "+ipv4+"\n")
	print ("Registration successfully added")

def get(s):
	print s.recv(1024)

def main(s):
	myAddr = "192.168.72.145"
	myPort = "9000"
	get(s)
	addReg(s, "testing" ,"22.22.22.22")
	sendDb(s, myAddr, myPort)

s = socket.socket()
s.connect(("192.168.72.134",20005)) 
main(s)

