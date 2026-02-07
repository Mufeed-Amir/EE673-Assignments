from socket import *

def start_tcp_server(server_name = 'localhost', server_port = 12000):
    # AF_INET = IPv4, SOCK_STREAM = TCP
     with socket(AF_INET, SOCK_STREAM) as server_socket:
          try:
               # Bind the socket to the address and port
               server_socket.bind((server_name, server_port))
               
               # Start listening for incoming TCP connections (queue up to 1 request)
               server_socket.listen(1)
               
               print(f"TCP Server up and listening on {server_name}:{server_port}")
               print("Press Ctrl+C to stop the server.")

               while True:
                    # Wait for a connection request
                    # This returns a NEW socket specifically for this client
                    connection_socket, client_address = server_socket.accept()
                    
                    # Use 'with' to automatically close the connection socket after this block
                    with connection_socket:
                         print(f"Connected by {client_address}")
                         
                         # Receive message (2048 is the buffer size)
                         data = connection_socket.recv(2048)
                         
                         if data:
                              # Process data (Uppercase conversion)
                              modified_message = data.decode('utf-8').upper()
                              
                              # Send response back using the specific connection socket
                              connection_socket.send(modified_message.encode('utf-8'))
          
          except OSError as e:
               print(f"System error occurred: {e}")
          except KeyboardInterrupt:
               print("\nServer shutting down...")

if __name__ == "__main__":
    start_tcp_server()