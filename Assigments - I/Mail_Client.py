from socket import *
import base64
from email.utils import formatdate, make_msgid
import ssl

# ==============================
# SMTP SERVER CONFIGURATION
# ==============================
SERVER = "mmtp.iitk.ac.in"    # SMTP server hostname
PORT   = 25                   # Standard SMTP port

# ==============================
# AUTHENTICATION CREDENTIALS
# ==============================
USERNAME = "mmamir22@iitk.ac.in"   # Sender email / login username
PASSWORD = ""                      # Email password

# ==================================
# EMAIL METADATA, BODY & ATTACHMENTS 
# ==================================
TO  = ["muhammadmameer22@gmail.com"]     # Primary recipients
CC  = []                                 # Carbon copy recipients
BCC = ["mufeed.amir.17290@gmail.com"]    # Blind carbon copy recipients

SUBJECT = "MAIL CLIENT - EE673 ASSIGNMENT - I"

BODY = """Hi,

PLEASE ADD THE BODY OF THE EMAIL HERE

Regards,
Mohd Amir
"""

# ---------- attachments ----------
# Add files names or file paths to this list to attach them to the email
filenames = []

# ============================================================
# CREATE TCP SOCKET AND CONNECT TO SMTP SERVER
# ============================================================
client = socket(AF_INET, SOCK_STREAM)
client.connect((SERVER, PORT))

def recv(expected_codes=None):
     """
     Receives server response and validates SMTP status codes.

     Parameters:
          expected_codes (list): Valid response codes expected from server.

     Behavior:
          - Prints server response for debugging.
          - Stops execution if an unexpected code is received.
     """
     response = client.recv(4096).decode()
     print(response)

     code = response[:3]

     if expected_codes and code not in expected_codes:
          print(f"SMTP Error: Expected {expected_codes}, got {code}")
          print("Stopping client...")
          client.close()
          exit()

     return code

def send(cmd, expected_codes=None):
     """
     Sends an SMTP command to the server.

     Parameters:
          cmd (str): SMTP command string.
          expected_codes (list): Expected response codes.
     """
     print(">>", cmd)
     client.send((cmd + "\r\n").encode())
     return recv(expected_codes)

# ============================================================
# SMTP HANDSHAKE + AUTHENTICATION
# ============================================================
recv(["220"])                 # Server greeting

send("EHLO client", ["250"])  # Extended handshake (EHLO is like HELO but for modern servers)
send("STARTTLS", ["220"])     # Upgrade to secure TLS connection

# Wrap the existing socket with SSL for encryption
context = ssl.create_default_context()
client = context.wrap_socket(client, server_hostname=SERVER)

send("EHLO client", ["250"])
send("AUTH LOGIN", ["334"])   # Begin authentication

# Username must be Base64 encoded
client.send(base64.b64encode(USERNAME.encode()) + b"\r\n")
recv(["334"])                 # Server requests password

# Password must also be Base64 encoded
client.send(base64.b64encode(PASSWORD.encode()) + b"\r\n")
recv(["235"])                 # Authentication successful


# ============================================================
# SPECIFY SENDER AND RECIPIENTS
# ============================================================
send(f"MAIL FROM:<{USERNAME}>", ["250"])

for addr in TO:
    send(f"RCPT TO:<{addr}>", ["250", "251"])

for addr in CC:
    send(f"RCPT TO:<{addr}>", ["250", "251"])

for addr in BCC:
    send(f"RCPT TO:<{addr}>", ["250", "251"])


# ============================================================
# EMAIL CONTENT (DATA PHASE)
# ============================================================
send("DATA", ["354"])   # Server ready to accept message body

date_header = formatdate(localtime=True)
msgid = make_msgid()
boundary = "BOUNDARY"   # MIME boundary to separate parts

# ---------- Email Headers ----------
headers = f"""From: {USERNAME}
To: {', '.join(TO)}
Subject: {SUBJECT}
Date: {date_header}
Message-ID: {msgid}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary={boundary}
"""

if CC:
    headers += f"Cc: {', '.join(CC)}\r\n"

# ---------- Email Body ----------
message = f"""--{boundary}
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

{BODY}
"""

# ============================================================
# ATTACHMENTS (BASE64 ENCODED)
# ============================================================
attachments = ""
for filename in filenames:
     with open(filename, "rb") as f:
          encoded_file = base64.encodebytes(f.read()).decode()

     attachments += f"""
--{boundary}
Content-Type: application/octet-stream; name="{filename}"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="{filename}"

{encoded_file}
"""

# MIME closing boundary
end = f"\r\n--{boundary}--\r\n"

# Final SMTP termination sequence requires a single dot
full_email = headers + "\r\n" + message + attachments + end + "\r\n.\r\n"

client.send(full_email.encode())

recv(["250"])   # Server confirms acceptance

# ============================================================
# TERMINATE SESSION
# ============================================================
send("QUIT", ["221"])
client.close()