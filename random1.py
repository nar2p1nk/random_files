# print(divmod(12, 6))

import random
# randos =['ass','booty','zuby','ruby','juby']


# for i in randos:
#     x = random.choice(randos)
#     print(x)



# # import the time module
import time
from playsound import playsound
# define the countdown func.
def countdown(t):    
    while t:
        mins, secs = divmod(t,60)
        timer = '{:2d}:{:2d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    playsound('/home/enemy/voiceClip/mp3/8a2087f5-4db9-40c0-baf2-bbbc12f39e49.mp3')


# input time in seconds
t = input('enter time in minutes: ')

# function call
countdown(int(t)* 60)


# count = random.randint(0, 100)

# while count:
#     time.sleep(1)
#     count -= 1
#     print(count)
# playsound('/home/enemy/voiceClip/mp3/8a2087f5-4db9-40c0-baf2-bbbc12f39e49.mp3')

#def hashed(word):

   # Lword= list(word)

  #  random.shuffle(Lword)

 #   password= ''.join(Lword)

#    print(password)

#ui = input('enter password: ')

#hashed(ui)






