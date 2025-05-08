# 🤖 Simulated Botnet with Python (Educational Only)

This project demonstrates how a basic **botnet command-and-control system** works, using Python sockets — entirely offline and local.

---

## ⚙️ Components

- `master.py`: The command & control (C2) server that sends commands
- `bot_client.py`: The bot that connects to the C2 server and executes commands

---

## 🧪 How It Works

1. Run `master.py`
2. Run one or more instances of `bot_client.py`
3. Type a command in the master console (e.g., `print("Hello from bot!")`)
4. Bots receive and display a simulated execution response

---

## ⚠️ Real Botnets vs This Demo

| Real Botnets | This Simulation |
|--------------|-----------------|
| Spread via malware | Manually started |
| Perform malicious acts | Only prints commands |
| Communicate over internet | Only localhost |
| Highly illegal | Educational & ethical |

---

## 🛡️ How to Defend Against Real Botnets

- Use antivirus and keep software updated
- Block unknown outbound traffic (firewall rules)
- Monitor for unauthorized socket communication
- Use endpoint detection & response (EDR) tools
- Educate users on avoiding malware/phishing

---

## 🧠 Educational Use Only

This simulation is 100% safe and legal. Never attempt real botnet development or deployment — it’s a **serious cybercrime**.
