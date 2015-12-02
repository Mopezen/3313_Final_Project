import socket

# TCP_IP = 'localhost'
TCP_IP = socket.gethostbyaddr("ec2-52-35-85-158.us-west-2.compute.amazonaws.com")[0]
TCP_PORT = 3400
BUFFER_SIZE = 1024

print 'TCP_IP=',TCP_IP
print 'TCP_PORT=',TCP_PORT

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.bind((TCP_IP, TCP_PORT))
tcpsock.listen(1)
conn, addr = tcpsock.accept()

print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data + " HI!")  # echo
conn.close()
