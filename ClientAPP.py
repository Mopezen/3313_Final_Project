from socket import * 
import time

print ('Running') #Statement to let me know the program started correctly
serverName = 'ec2-52-35-85-158.us-west-2.compute.amazonaws.com' #server name
serverPort = 3400       #server port
clientSocket = socket(AF_INET,SOCK_STREAM) #create the socket
clientSocket.connect((serverName, serverPort))
message = 'Hello Server' #message to be sent
count=1
while 1:
    clientSocket.send(message)#sends a message to the server on port 3313
    print 'sending %d'%count
    count=count+1
    print(clientSocket.recv(1024))        
    time.sleep(60)


clientSocket.close() #closes the sockets
