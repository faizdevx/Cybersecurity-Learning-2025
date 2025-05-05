import hashlib
from itertools import cycle

# Confidentiality: Caesar Cipher
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            if char.isupper():
                shifted = shifted.upper()
            result += shifted
        else:
            result += char
    return result

# Integrity: Hashing for Integrity Check
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def integrity_check(original, modified):
    return generate_hash(original) == generate_hash(modified)

# Availability: DDoS Conceptual Simulation
def ddos_simulation(target):
    # Conceptual: Just simulating the idea with repeated requests
    print(f"Simulating DDoS on {target}...")
    for _ in range(100):
        print(f"Request to {target}... (conceptual)")

def main():
    # Confidentiality: Caesar Cipher
    print("Confidentiality - Caesar Cipher Demo")
    text = input("Enter a message to encrypt: ")
    shift = int(input("Enter the shift value for Caesar Cipher: "))
    encrypted = caesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted}")
    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted text: {decrypted}\n")
    
    # Integrity: Hash Comparison
    print("Integrity - Hash Comparison Demo")
    original_text = input("Enter the original text for hash comparison: ")
    modified_text = input("Enter the modified text for hash comparison: ")
    if integrity_check(original_text, modified_text):
        print("Integrity Check: The texts are identical.")
    else:
        print("Integrity Check: The texts have been modified!\n")
    
    # Availability: DDoS Simulation
    print("Availability - DDoS Conceptual Simulation Demo")
    target = input("Enter the target URL for DDoS simulation: ")
    ddos_simulation(target)

if __name__ == "__main__":
    main()
