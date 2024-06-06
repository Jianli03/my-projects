'''
Fernet Cipher with AES-256 encryption
This example shows the basic steps for using cryptography to encrypt and decrypt data.

First, we generate a random password and a salt, which will be used to derive a key for the cipher. We use the PBKDF2HMAC algorithm to derive the key from the password, using the salt and a strong hashing function.

After obtaining the key, we create a Fernet cipher using the Fernet class. This is a symmetric cipher, which means it uses the same key for both encryption and decryption.

 Then, we use the encrypt() method to encrypt a message, and the decrypt() method to decrypt the encrypted message. The result is a secure and encrypted communication that can be transmitted over an insecure network.
'''
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


#Password-Based Key Derivation Function (PBKDF2): This method stretches a user-provided password into a strong encryption key.
# salt is optional
password = b"your_strong_password_here"  # Replace with your actual password (bytes)
salt = os.urandom(16)  # Generate a random salt for added security

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,  # Adjust iterations based on desired security level
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Derive the key from password


# Create a Fernet cipher using the key
cipher = Fernet(key)

# Encrypt a message
encrypted_message = cipher.encrypt(b'Hello, world!')

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  cipher.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + cipher.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue