import hashlib
import random

### basic hashing ###
def shuffle(word):

   Lword= list(word)

   random.shuffle(Lword)

   password= ''.join(Lword)

   print(password)


def hashed(word):

    eword = word.encode()

    hashedWord =hashlib.blake2b(eword).hexdigest()

    print(hashedWord)

