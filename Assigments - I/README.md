# Assignment - I  
> EE673A - DIGITAL COMMUNICATION NETWORKS <br>
> @author: **Mohd Amir (220660)**
# Question 1: Basics of Socket Programming

## Files
```
-   UDP_server.py
-   UDP_client.py
-   TCP_server.py
-   TCP_client.py
```

## UDP Protocol
### **1. Start the Server**

Open a terminal and navigate to the project directory.

``` bash
python UDP_server.py
```

You should see when running UDP server:

    UDP Server up and listening on localhost:12000
    Press Ctrl+C to stop the server.


> Keep this terminal open --- the server must be running before
starting the client.


### **2. Run the Client**

Open **another terminal** and navigate to the same directory.

``` bash
python UDP_client.py
```

Enter a lowercase sentence when prompted:

    Enter lowercase sentence: Testing UDP Protocol

Expected output:

    Sending to localhost:12000...
    Server response: TESTING UDP PROTOCOL

## TCP Protocol
### **1. Start the Server**

Open a terminal and navigate to the project directory.

``` bash
python TCP_server.py
```

You should see when running UDP server:

    TCP Server up and listening on localhost:12000
    Press Ctrl+C to stop the server.


> Keep this terminal open --- the server must be running before
starting the client.


### **2. Run the Client**

Open **another terminal** and navigate to the same directory.

``` bash
python TCP_client.py
```

Enter a lowercase sentence when prompted:

    Connecting to localhost:12000...
    Enter lowercase sentence: Testing TCP Protocol

Expected output:

    Server response: TESTING TCP PROTOCOL

------------------------------------------------------------------------

# Question 2: UDP Chat application

> **Both devices (computer & phone) MUST be connected to the same network.**

## On Your Phone
Install the UDP testing app:
**UDP Monitor (Android)**\
https://play.google.com/store/apps/details?id=com.sandersoft.udpmonitor

------------------------------------------------------------------------
### 1. Start the Python Script & Configure UDP Monitor (Phone)

Navigate to assignment directory folder and run:

``` bash
python UDP_chatApp.py
```

(or `python3 udp_chat.py` on Mac/Linux)

You will see:

    Remote IP address is: <Your computer IP>
    Remote PORT is: 19999
    Enter phone IP:

### Open the app and set:

#### Remote IP:
    <Your Computer IP> (ex: 192.168.1.5)

### Remote PORT:
    19999

#### 
#### 


### Enter Phone Details in Terminal

Script will ask:

    Enter phone IP: <"Local IP" The IPv4 address of your phone will be displayed on the top left corner>
    Enter phone port: <"Local PORT" of the UDP monitor app>

You'll see

    Computer IP address is: 172.23.5.133
    Enter phone IP: 100.75.201.49
    Enter phone port: 50787
    Listening on 0.0.0.0:19999...
    You: 
> Now the connection is ready, start chatting!
------------------------------------------------------------------------

## Question 3: Mail Client

### 1. Update Credentials

Inside the script add your IITK email address and password:

```python
# ==============================
# AUTHENTICATION CREDENTIALS
# ==============================
USERNAME = "mmamir22@iitk.ac.in"   # Sender email / login username
PASSWORD = "password"              # Email password (keep secure)
```
**Note:**
If you are using `GMAIL` account to send email use `app password` not gmail password \
Also update `SMTP SERVER CONFIGURATION`:

```python
# ==============================
# SMTP SERVER CONFIGURATION
# ==============================
SERVER = "smtp.gmail.com"   # SMTP server hostname
PORT = 587                    # Standard SMTP port
```

### 2. Update TO, CC, BCC & BODY

Inside the script:

```python
# ==============================
# EMAIL METADATA & BODY
# ==============================
TO = ["mufeed.amir.17290@gmail.com"]     # Primary recipients
CC = []                                  # Carbon copy recipients
BCC = ["muhammadmameer22@gmail.com"]     # Blind carbon copy recipients

SUBJECT = "MAIL CLIENT - EE673 ASSIGNMENT - I"

BODY = """Hi!,

PLEASE ADD THE BODY OF THE EMAIL HERE

Regards,
Mohd Amir
"""
```
> You can add multiple email address in each List (TO, CC, BCC) seperated by comma
---

### 3. Add Attachments (Optional)

Place files in the same directory or provide full paths:

```python
filenames = ["<filename1>.<extension1>", "<filename2>.<extension2>"]
```
> set `filenames` = [ ] ; if you don't want to send attachment
---

### 4. Run the Script

```
python Mail_Client.py
```
> (or `python3 Mail_Client.py` on Mac/Linux)

If successful, you will see SMTP response codes printed in the terminal.

---

