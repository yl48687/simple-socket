# Simple Socket
This project implements a client-server system using sockets. The client and server interact following a specific protocol:

## Functionality
### Server
On the server side, the program first creates a string containing its name (e.g., "Server of Bob Smith"). It then listens for incoming connections from clients. Upon receiving a connection request from a client, the server extracts the client's name and the integer sent by the client. Subsequently, it prints both the client's name and its own name. The server then proceeds to select a random integer between 1 and 100. After selecting the integer, it calculates the sum of this integer and the one sent by the client. The server constructs a message containing its name, the server-chosen integer value, and the calculated sum, and sends this message back to the client. Following this, the server continues to listen for connections and process messages from clients.

### Client
The client program begins by prompting the user to input an integer between 1 and 100. Upon receiving the input, it establishes a TCP socket connection to the server. Subsequently, it constructs a message comprising the client's name (e.g., "Client of Bob Smith") and the integer provided by the user. This message is then sent to the server. Following the transmission, the client enters a waiting state to receive a response from the server. Upon receiving the server's response, the client processes the received data, extracting the server's name, the integer chosen by the server, and the sum of the server-chosen integer and the client's integer. Finally, it prints this information for the user to view.
