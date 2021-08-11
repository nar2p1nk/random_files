import time 



def clock(t):

  while t:
    mins,secs = divmod(t, 60)
    display = '{:2d}: {:2d}'.format(mins,secs)
    print(display, end='\r')
    time.sleep(1)
    t -= 1

  print('end')

count = input('enter minutes')


clock(int(count)*60)