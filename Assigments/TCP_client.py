from socket import *

def start_tcp_client(server_name = 'localhost', server_port = 12000):
    # AF_INET = IPv4, SOCK_STREAM = TCP
     with socket(AF_INET, SOCK_STREAM) as client_socket:
          # Set a timeout so the client doesn't hang if the connection fails
          client_socket.settimeout(2.0)
          
          try:
               print(f"Connecting to {server_name}:{server_port}...")
               # Establish the 3-way handshake connection
               client_socket.connect((server_name, server_port))

               message = input("Enter lowercase sentence: ").strip()
               if not message:
                    print("No input provided. Exiting.")
                    return

               # Send message (TCP stream)
               client_socket.send(message.encode('utf-8'))

               # Receive response
               modified_message = client_socket.recv(2048)
               print(f"Server response: {modified_message.decode('utf-8')}")

          except socket.timeout:
               print("Error: Connection timed out. (Server may be offline)")
          except ConnectionRefusedError:
               print("Error: Connection refused. (Server is likely not running)")
          except Exception as e:
               print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        start_tcp_client()
    except KeyboardInterrupt:
        print("\nClient closed.")