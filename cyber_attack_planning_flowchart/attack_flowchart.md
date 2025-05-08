# 🔁 Cyber Attack Planning Flow (Kill Chain Model)


# description 


Reconnaissance: Open-source research, scanning, identifying services.

Weaponization: Develop payloads, phishing emails, malware.

Delivery: Send phishing email or exploit web service.

Exploitation: Trigger vulnerability.

Installation: Drop backdoors or rootkits.

C2: Remote shell or beaconing to hacker.

Actions: Data theft, ransomware, pivoting.

Covering Tracks: Delete logs, clear shell history.

----------------------------------------------------



```mermaid
flowchart TD
    A[1. Reconnaissance] --> B[2. Weaponization]
    B --> C[3. Delivery]
    C --> D[4. Exploitation]
    D --> E[5. Installation]
    E --> F[6. Command & Control (C2)]
    F --> G[7. Actions on Objectives]
    G --> H[8. Covering Tracks]
