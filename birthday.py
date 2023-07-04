from gtts import gTTS
import os
mytext="hii"
language="en"
v=gTTS(text=mytext,lang=language,sloe=True)
v.save("v.mp3")
os.system("start v.mp3")