## 🔧 Step 1: Install Nmap

```bash
sudo apt update && sudo apt install nmap


nmap -sS -T4 127.0.0.1


Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-08 12:40 IST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000080s latency).
All 1000 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 1000 closed tcp ports (reset)

Nmap done: 1 IP address (1 host up) scanned in 0.26 seconds



# conclusion 

The scan shows no open TCP ports on localhost.

This is a secure configuration: no exposed services.

In real-world attacks, open ports might reveal:

SSH (22), HTTP (80), RDP (3389), DBs (3306, 5432), etc.

It demonstrates how attackers identify entry points.