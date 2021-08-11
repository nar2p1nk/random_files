from cryptography.fernet import Fernet

import time

password = input('enter password: ')

### symetrical encryption ###

### generate key
def syncEncrypt(t):


    key = Fernet.generate_key()

    fkey = Fernet(key)
### encryption
    encryptedPassword = fkey.encrypt(t.encode())

    print('uncrypted password:',password)
    time.sleep(5)
    print('encrypted password:',encryptedPassword)
    time.sleep(5)

### decryption ###
    decryptedPassword =fkey.decrypt(encryptedPassword).decode()
    print('decrypted password:',decryptedPassword)


### asymetrical encrytioon

import rsa

def asyncEncrypt(t):
    publicKey, privateKey = rsa.newkeys(512)

    encrypt = rsa.encrypt(t.encode(),publicKey)

    print('uncrypted password:',t)
    time.sleep(4)
    print('encrypted password:', encrypt)


### decryption ###
    decrypt = rsa.decrypt(encrypt,privateKey).decode()

    time.sleep(4)

    print('decrypted password:',decrypt)



