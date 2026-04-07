import socket
import subprocess

HOST = ''   # change to your VM IP
PORT = 4444
PASSWORD = "iloveboosters"

def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print("Connecting to server...")
        client.connect((HOST, PORT))

        # Send password
        client.sendall(PASSWORD.encode())
        print("Password sent")

        while True:
            cmd = input("Enter command (or 'exit'): ").strip()

            if not cmd:
                continue

            client.sendall(cmd.encode())

            if cmd == "exit":
                print("Closing connection")
                break

            response = client.recv(4096).decode()
            print("Server response:", response)

    except Exception as e:
        print("Connection error:", e)

    finally:
        client.close()

if __name__ == "__main__":
    main()
