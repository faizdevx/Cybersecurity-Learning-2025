import socket

HOST = '127.0.0.1'  # Localhost only
PORT = 9999         # Arbitrary non-privileged port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[MASTER] Listening on {HOST}:{PORT}")

clients = []

try:
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"[MASTER] Bot connected from {addr}")

        # Send a command to this bot
        command = input("[MASTER] Enter command to send: ")
        if command.lower() == "exit":
            break

        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print(f"[BOT RESPONSE] {response}")

except KeyboardInterrupt:
    print("\n[MASTER] Shutting down.")
finally:
    for c in clients:
        c.close()
    server.close()
