from socket import *

def start_udp_client(server_name = 'localhost', server_port = 12000):
    # AF_INET = IPv4, SOCK_DGRAM = UDP
    with socket(AF_INET, SOCK_DGRAM) as client_socket:
        # Set a timeout so the client doesn't wait forever
        client_socket.settimeout(2.0)
        server_address = (server_name, server_port)

        message = input("Enter lowercase sentence: ").strip()
        if not message:
            print("No input provided. Exiting.")
            return
        
        try:
            print(f"Sending to {server_name}:{server_port}...")
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Attempt to receive response
            modified_message, _ = client_socket.recvfrom(2048)
            print(f"Server response: {modified_message.decode('utf-8')}")

        except socket.timeout:
            print("Error: The request timed out. (Server may be offline or packet lost)")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        start_udp_client()
    except KeyboardInterrupt:
        print("\nClient closed.")