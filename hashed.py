import hashlib

password = 'asscrackerandtitsbolisk'.encode()

print(password)

print('password before hashing')

time.sleep(4)

print(hashlib.blake2b(password).hexdigest())

print('password after hashing')
