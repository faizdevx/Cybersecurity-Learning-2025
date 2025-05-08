import socket

HOST = '127.0.0.1'  # Must match master.py
PORT = 9999

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("[BOT] Connected to master.")

    while True:
        command = client.recv(1024).decode()
        if not command:
            break
        print(f"[BOT] Received command: {command}")

        # Simulated execution
        output = f"[SIMULATION] Bot executed: {command}"
        client.send(output.encode())

except ConnectionRefusedError:
    print("[BOT] Could not connect to master.")
except Exception as e:
    print(f"[BOT] Error: {e}")
finally:
    client.close()
