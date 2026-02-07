from socket import *

def start_udp_server(server_name = 'localhost', server_port = 12000):
    # AF_INET = IPv4, SOCK_DGRAM = UDP
    with socket(AF_INET, SOCK_DGRAM) as server_socket:
        try:
            # Bind the socket to the address and port
            server_socket.bind((server_name, server_port))
            print(f"UDP Server up and listening on {server_name}:{server_port}")
            print("Press Ctrl+C to stop the server.")

            while True:
                # Receive message and client address
                # 2048 is the buffer size
                data, client_address = server_socket.recvfrom(2048)
                
                if data:
                    print(f"Received message from {client_address}")
                    
                    # Process data (Uppercase conversion)
                    modified_message = data.decode('utf-8').upper()
                    
                    # Send response back to the specific client
                    server_socket.sendto(modified_message.encode('utf-8'), client_address)
        
        except OSError as e:
            print(f"System error occurred: {e}")
        except KeyboardInterrupt:
            print("\nServer shutting down...")

if __name__ == "__main__":
    start_udp_server()