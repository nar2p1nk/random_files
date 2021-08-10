from cryptography.fernet import Fernet

password = 'asscrackerandtitsbolisk'

key = Fernet.generate_key()

fkey = Fernet(key)

encryptedPassword = fkey.encrypt(password.encode())

print('uncrypted password: ',password)
time.sleep(5)
print('encrypted password: ',encryptedPassword)
time.sleep(5)
print('decrypted password: ', fkey.decrypt(encryptedPassword).decode())