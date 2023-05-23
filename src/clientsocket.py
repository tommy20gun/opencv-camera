import socket

# Set the IP address and port of the Raspberry Pi server
IP_ADDRESS = "192.168.147.134"
PORT = 1025

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))

while True:
    # Send data to the server
    print("input data here: ")
    data = input()
    client_socket.sendall(data.encode())

    # Receive data from the server
    received_data = client_socket.recv(1024).decode()
    print("Received data: ", received_data)

    if data == "break":
        break

# Close the connection
client_socket.close()
