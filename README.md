# Simple Socket
This project implements a basic client-server communication system using TCP sockets. The `client` and `server` applications exchange messages over the network. The `client` prompts the user to input an integer between 1 and 100 along with their name, which is then sent to the `server`. Upon receiving the client's message, the `server` performs operations including generating a random integer, computing the sum of this integer and the client's input, and sending the result back to the `client` along with the server's name.

## Design Overview
The project facilitates bidirectional communication between a `client` and a `server` using TCP sockets. The `client` component collects user input and establishes a TCP connection to the server. Meanwhile, the `server` waits for incoming connections and upon receiving a message from a `client`.

## Functionality
`client`:
- Prompts the user for an integer input and their name.
- Establishes a TCP connection to the server.
- Sends a message to the server containing the user's name and the entered integer.
- Receives a response from the server.
- Prints the server's name along with the received numbers.

`server`:
- Creates a string containing its name.
- Listens for incoming connections from clients.
- Upon receiving a message from a client:
- Extracts the client's name and the integer value.
- Prints the client's name and the server's name.
- Generates a random integer and computes the sum of this integer and the client's input.
- Sends the server's name, the generated integer, and the sum back to the client.

## File Structure and Content
```
simple-socket/
├── client/
│   └── client.py
├── README.md
└── server/
    └── server.py
```