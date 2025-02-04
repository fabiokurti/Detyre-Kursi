from cryptography.fernet import Fernet

# Gjenerimi i çelësit
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Leximi i të dhënave nga skedari CSV
with open('data.csv', 'r', encoding='utf-8') as file:
    data = file.read()

# Enkriptimi i të dhënave
encrypted_data = cipher_suite.encrypt(data.encode())

# Ruajtja e të dhënave të enkriptuara
with open('encrypted_data.txt', 'wb') as file:
    file.write(encrypted_data)