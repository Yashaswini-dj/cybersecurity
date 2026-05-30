from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("secret.key", "wb") as file:
    file.write(key)

with open("secret.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)

message = input("enter message:")

encrypted = fernet.encrypt(message.encode())

print("Encrypted:",encrypted)

decrypted = fernet.decrypt(encrypted).decode()

print("Decrypted:",decrypted)