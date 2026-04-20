from getpass import getpass
import socket

REMOTE_HOST = "SERVER_IP_HERE"
REMOTE_PORT = 4444

client = socket.socket()
client.connect((REMOTE_HOST, REMOTE_PORT))

password = getpass()
client.send(password.encode())

while True:
    cmd = input("Enter Command: ")

    client.send(cmd.encode())

    if cmd == "exit":
        break

    print(client.recv(4096).decode())

client.close()
