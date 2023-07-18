import socket
from ssdpy import SSDPClient
import urllib.parse

client = SSDPClient()
devices = client.m_search("chat-service")
for device in devices:
    location = device.get("location")
    url = urllib.parse.urlparse(location)
    chat_server_ip = url.hostname
    chat_server_port = url.port

HEADER = 64
PORT = chat_server_port
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = chat_server_ip
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hei")
input()
send("På")
input()
send("Deg")
input()
send("Du")
input()
send("Er")
input()
send("En")
input()
send("Liten")
input()
send("Tissefant!")
send(DISCONNECT_MESSAGE)