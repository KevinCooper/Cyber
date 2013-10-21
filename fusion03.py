import socket, struct, binascii
def main():
	print "[+] Start"
	s = socket.socket()
	s.connect(('192.168.72.134',20003))
	string = s.recv(1024)
	print string.strip("\n").strip("\"")
	token = string.strip("\"")
	#token = string.split(":")[-1].strip("\n").strip("\"")
	print "[+] Sending data"
	s.send(token + "\n" + "testing\n")
	print s.recv(1024)






main()
