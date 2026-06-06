from gtts import gTTS
import os
from tkinter import *

def text_speech():
    text1=entry1.get()
    output=gTTS(text=text1,lang='en',slow=False)
    output.save("output_1.mp3")
    os.system("start output_1.mp3")

root=Tk()
canvas1=Canvas(root,width=400,height=300)
canvas1.pack()

entry1=Entry(root)
canvas1.create_window(200,180,window=entry1) #coordinate positions

button1=Button(text="Strat",command=text_speech)
canvas1.create_window(200,230,window=button1) # y will be same x changes


root.mainloop()