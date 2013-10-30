import socket, struct, binascii

def sendDb(s, ipv4, port):
	s.sendall("senddb "+ ipv4 + " " + port+"\n")
	print "Attempting to send the DB."

def addReg(s, name, ipv4):	
	s.sendall("addreg "+ name +" \x26\xa9\x10\x01 "+ipv4+"\n")
	print ("Registration successfully added")

def get(s):
	print s.recv(1024)

def checkname():
	print "What"

def isUp(port):
	s.sendall("isup "+ "junk "+ str(port) +" \n")

def main(s):
	myAddr = "192.168.72.145"
	myPort = "9000"
	get(s)
	#addReg(s, "iamalongaddress" ,"192.168.72.145")
	sendDb(s, myAddr, myPort)
	#isUp(9000)

s = socket.socket()
s.connect(("192.168.72.134",20005)) 
main(s)

