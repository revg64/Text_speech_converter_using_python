#convert file content into speech
from gtts import gTTS
import os

text1=open('demo.txt','r',encoding="utf-8").read()
output=gTTS(text=text1,lang='te',slow=False)
output.save('file_output.mp3')

os.startfile("file_output.mp3")