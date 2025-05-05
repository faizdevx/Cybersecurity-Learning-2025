# CIA Triad Visualizer / Explainer

This Python script demonstrates the CIA (Confidentiality, Integrity, and Availability) Triad concepts with simple examples. It uses basic cryptography, hashing, and conceptual DDoS simulation to explain each principle in an interactive and easy-to-understand manner.

## Features

1. **Confidentiality (Caesar Cipher)**: 
   - Encrypts and decrypts a message using a simple Caesar cipher, demonstrating confidentiality by encoding and decoding messages.

2. **Integrity (Hash Comparison)**:
   - Compares the hash of two text inputs (original and modified) using SHA-256, demonstrating how hash functions ensure data integrity.

3. **Availability (Conceptual DDoS Simulation)**:
   - Simulates a DDoS (Distributed Denial of Service) attack by printing repeated requests to a target, representing the concept of availability and the impact of DDoS attacks.

## Requirements

- Python 3.x
- No external libraries are required except for the built-in `hashlib` library in Python.


## OUTPUT

```

Confidentiality - Caesar Cipher Demo
Enter a message to encrypt: Hello
Enter the shift value for Caesar Cipher: 3
Encrypted text: Khoor
Decrypted text: Hello

```

```
Integrity - Hash Comparison Demo
Enter the original text for hash comparison: Hello World
Enter the modified text for hash comparison: Hello World!
Integrity Check: The texts have been modified!

```

```
Availability - DDoS Conceptual Simulation Demo
Enter the target URL for DDoS simulation: example.com
Simulating DDoS on example.com...
Request to example.com... (conceptual)
Request to example.com... (conceptual)

```