from gtts import gTTS
import os

text1="LoL this is really funny ok" 
audio=gTTS(text=text1,lang='en',slow=False)

#saving audio as mp3 file
audio.save('output.mp3')

#playing the mp3 file
os.system("start output.mp3")

# or
# import os
# os.startfile("output.mp3")