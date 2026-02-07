from socket import *     
import threading         # Allows running send and receive simultaneously

def get_local_ip():
    sock = socket(AF_INET, SOCK_DGRAM)
    try:
        # Doesn't actually connect to the internet,
        # just forces the OS to choose the correct network interface
        sock.connect(("8.8.8.8", 80))  
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip

print("Computer IP address is:", get_local_ip())

LOCAL_IP = "0.0.0.0"  # Listen on all interfaces (allows receiving from any IP)
LOCAL_PORT = 19999       # Port your computer will listen on

#   for phone's IP and port (destination for outgoing messages)
PHONE_IP = input("Enter phone IP: ")
PHONE_PORT = int(input("Enter phone port: "))

# Create a UDP socket
# AF_INET -> IPv4 addressing
# SOCK_DGRAM -> UDP protocol (connectionless, fast)
sock = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the local IP and port so it can receive messages
sock.bind((LOCAL_IP, LOCAL_PORT))
print(f"Listening on {LOCAL_IP}:{LOCAL_PORT}...")

# Function responsible for RECEIVING messages
def receive():
    while True:
        try:
            # Wait for incoming UDP packet (max 1024 bytes)
            data, addr = sock.recvfrom(1024)

            # Decode bytes into string and print
            # end="" keeps the cursor on same line for clean prompt
            print(f"\nPhone: {data.decode()}")
            print("You: ", end="", flush=True)

        except Exception as e:
            # Print error if something goes wrong
            print("Receive error:", e)
            break

# Function responsible for SENDING messages
def send():
    while True:
        try:
            # Take message input from user
            msg = input("You: ")

            # Encode string into bytes before sending
            # sendto() requires destination address each time in UDP
            sock.sendto(msg.encode(), (PHONE_IP, PHONE_PORT))

        except Exception as e:
            print("Send error:", e)
            break

# Start receive thread (daemon=True ensures it exits when main program exits)
threading.Thread(target=receive, daemon=True).start()

# Start send thread
threading.Thread(target=send, daemon=True).start()

# Keeps the main thread alive forever without consuming CPU
# Otherwise daemon threads would terminate immediately
threading.Event().wait()
