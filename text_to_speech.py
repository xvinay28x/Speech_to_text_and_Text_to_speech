import pyttsx3

engine = pyttsx3.init()
x = input("Write any thing : ")
engine.say(x)
engine.runAndWait()