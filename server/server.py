import socket
import random

# Creates a server
server = 'localhost'
port = 12345
serverAddress = (server, port)

# Creates a server name
serverName = "Server of Yewon Lee"

# Create a server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the server port number with the server socket
serverSocket.bind(serverAddress)

# Waits for a client
serverSocket.listen(1)

# Proceeds to communicate if connected with the client successfully
connectionSocket, addr = serverSocket.accept()
clientName = connectionSocket.recv(2048)
clientName = clientName.decode("utf-8")
clientNumber = connectionSocket.recv(2048)
clientNumber = clientNumber.decode("utf-8")
print("Client Name: ",clientName)
print("Server Name: ",serverName)
serverNumber = random.randint(1,101)
sum = serverNumber + int(clientNumber)
sum = str(sum)
serverNumber = str(serverNumber)
connectionSocket.send(bytes(serverName,"utf-8"))
connectionSocket.send(bytes(serverNumber,"utf-8"))
connectionSocket.send(bytes(sum,"utf-8"))

# Closes the communication with the cleint
connectionSocket.close()
