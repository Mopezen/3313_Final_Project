import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hello",("129.100.227.119", 2000))
data = s.recv(1024)
s.close()