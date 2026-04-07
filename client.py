import socket
import subprocess

HOST = '10.0.2.15'   # change to your VM IP
PORT = 4444
PASSWORD = "iloveboosters"

def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print("Connecting to server...")
        client_sock.connect((HOST, PORT))

        # Send password
        client_sock.sendall(PASSWORD.encode())
        print("Password sent")

        while True:
            cmd = input("Enter command (or 'exit'): ").strip()

            if not cmd:
                continue

            client_sock.sendall(cmd.encode())

            if cmd == "exit":
                print("Closing connection")
                break

            response = client_sock.recv(4096)
            if not response:
                print("Server closed connection")
            
            print("Server response:", response.decode())

    finally:
        client_sock.close()

if __name__ == "__main__":
    main()
