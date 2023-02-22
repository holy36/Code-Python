import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
r = sr.Recognizer()

while(1):
    with sr.Microphone() as source:
        print("Mời bạn nói: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            print("Bạn -->: {}".format(text))
            x = text.lower().find("kết thúc")
            if(x!=-1):
                break
            output = gTTS(text,lang="vi", slow=False)
            output.save("output.mp3")
            playsound.playsound('output.mp3', True)
            
        except:

            print("Xin lỗi! tôi không nhận được voice!")


