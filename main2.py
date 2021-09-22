from gtts import gTTS
text = open("your_file.txt")
a = text.read()
mp3 = gTTS(a)
text.close()
mp3.save("hello.mp3")