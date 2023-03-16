import socket

# Connect to the server
HOST = "192.168.2.2"
PORT = 50020
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Receive the hex representation of the image from the server
data = client_socket.recv(1024)
print(data)
while True:
    data = client_socket.recv(1024)
    if not data:
        break

    hex_string = data.decode('utf-8')

    # Convert the hex string to bytes
    image_bytes = bytes.fromhex(hex_string)
    print(image_bytes)

    # Write the bytes to a file
    # with open('image.jpg', 'wb') as f:
    #     f.write(image_bytes)

# Close the client socket
client_socket.close()