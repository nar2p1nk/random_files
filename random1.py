####### clock  ########## 
# # import the time module
import time
from pydub import AudioSegment
from pydub.playback import play
# define the countdown func.
def clock(t):    
    while t:
        mins, secs = divmod(t,60)
        timer = '{:2d}:{:2d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    play(AudioSegment.from_mp3('/home/nemesis/Music/MusicSYNDICATE'))


