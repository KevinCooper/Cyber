;; Mon Mar 11 05:34:41 PDT 2013
;; EBX, ECX, EDX, ESI, EDI, EBP then stack
section .text

%define filename ".//testfile"

BITS 32
global main

%include "short32.s"
%include "syscall.s"
%include "constants32.s"
%include "util.s"


main:
	push ebp
	mov ebp, esp
	and esp, 0xfffffff0
	sub esp, 0x10

	xor eax, eax
	push eax
	PUSH_STRING "./readme" 
	mov ebx, esp ;arg1 filename
	xor ecx, ecx 
	add ecx, O_RDONLY ;arg2 = RDONLY
	xor edx, edx ;arg3 = 0
	SYSTEM_CALL(open) 
	mov DWORD [esp+0x4], eax ;Value of open FD
	call getmem
	mov DWORD [esp+0x0], eax ;Value of mmaped region

my_read:
	mov ecx, DWORD [esp+0x0]
	mov ebx, DWORD [esp+0x4]
	mov edx, 0x100
	SYSTEM_CALL(read)
	cmp eax, 0
	jz my_exit ; At the end?

my_write:
	xor ebx, ebx
	inc ebx
	mov edx, 0x100
	SYSTEM_CALL(write)	
	mov ecx, DWORD [esp+0x0]
	xor eax, eax

zero_loop:
	xor ebx, ebx
	mov ebx, DWORD [ecx + eax]
	xor DWORD [ecx + eax], ebx
	inc eax
	cmp eax, 100
	jbe zero_loop
	jmp my_read

my_exit:
	mov ebx, DWORD [esp+0x4]
	SYSTEM_CALL(close)

	xor ebx, ebx
	inc ebx
	SYSTEM_CALL(exit)

getmem:
	; mmap(0, 1M, PROT_READ|PROT_WRITE, MAP_PRIVATE, -1, 0)
	push ebp
	mov ebp, esp
	and esp, 0xfffffff0
	sub esp, 0x30
	mov DWORD [esp+0x14],0x0        			    ; 0
	mov DWORD [esp+0x10],0xffffffff	 			    ; -1
	mov DWORD [esp+0xc], 0x0020|0x0002		 	    ; Priv/Anon
	mov DWORD [esp+0x8], 0x02|0x1				    ; R/W
	mov DWORD [esp+0x4], 0x100000			    	    ; 1MB
	mov DWORD [esp],0x0					    ; sys addr
	mov ebx, esp
	SYSTEM_CALL(mmap)
	leave
	ret
