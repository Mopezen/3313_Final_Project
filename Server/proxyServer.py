from socket import *
import sys

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('0.0.0.0', 3313))
tcpSerSock.listen(5)
# Fill in end.

while 1:
	# Strat receiving data from the client
	print 'Ready to serve...'
	tcpCliSock, addr = tcpSerSock.accept()
	print 'Received a connection from:', addr
	message = tcpCliSock.recv(4096)
	print message
	
	tcpCliSock.send("Why hi there")
	tcpCliSock.send("Content-Type:text/html\r\n")
	# Fill in start.
	tcpCliSock.send(outputdata)
	tcpCliSock.close()

#Finished and close the orignal connection
#Since were in an infinite loop we won't reach this	
# Fill in start.
tcpSerSock.close()
# Fill in end. 