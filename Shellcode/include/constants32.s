BITS 32

;OPEN() Constants
%define O_RDONLY	0x0000
%define O_WRONLY	0x0001
%define O_RDWR		0x0002
;OPEN() Creation Constants
%define O_CREAT		0x0100	/* second byte, away from DOS bits */
%define O_EXCL		0x0200
%define O_NOCTTY	0x0400
%define O_TRUNC		0x0800
%define O_APPEND	0x1000
%define O_NONBLOCK	0x2000

;MMAP FLAGS
%define	PROT_READ	0x04	/* pages can be read */
%define	PROT_WRITE	0x02	/* pages can be written */
%define	PROT_EXEC	0x01	/* pages can be executed */

%define	MAP_COPY	0x0020	/* "copy" region at mmap time */
%define	MAP_SHARED	0x0010	/* share changes */
%define	MAP_PRIVATE	0x0000	/* changes are private */
%define	MAP_FILE	0x0001	/* mapped from a file or device */
%define	MAP_ANON	0x0002	/* allocated from memory, swap space */
%define	MAP_TYPE	0x000f	/* mask for type field */
