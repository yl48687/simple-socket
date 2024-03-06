import socket
import random

# Stores a user input of a random integer from 1 to 100, inclusive
try:
        integer = int(input("Enter an integer between 1 and 100: "))
        if integer < 1 or integer > 100:
                print("Please enter an integer between 1 and 100, inclusive.")
except ValueError:
	print("Please enter an integer between 1 and 100, inclusive.")

# Creates a client name
clientName = "Client of Yewon Lee"

# Creates a server
server = 'localhost'
port = 12345
serverAddress = (server, port)

# Creates a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempts to connect to the server
clientSocket.connect(serverAddress)

# Proceeds to communicate if connected with the server successfully
print("")
clientNumber = str(integer)
clientSocket.send(bytes(clientName,"utf-8"))
clientSocket.send(bytes(clientNumber,"utf-8"))
serverName = clientSocket.recv(2048)
serverNumber = clientSocket.recv(2048)
serverAddress = clientSocket.recv(2048)
print("Server Name:", serverName.decode("utf-8"))
print("Server Number:", serverNumber.decode("utf-8"))
print("Client Number + Server Number:", serverAddress.decode("utf-8"))

# Closes the communication with the server
clientSocket.close()
