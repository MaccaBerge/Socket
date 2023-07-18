import socket 
import threading

from ssdpy import SSDPServer



# Socket
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# SSDP
location = f"http://{SERVER}:{PORT}"

def start_ssdp_server():
    server = SSDPServer("my-chat-service", device_type="chat-service", location=location)
    server.serve_forever()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start_server():
    ssdp_thread = threading.Thread(target=start_ssdp_server)
    ssdp_thread.start()

    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


