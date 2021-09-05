import speech_recognition as sr

r  = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.energy_threshold = 4000
    audio = r.listen(source) 
try:
    text = r.recognize_google(audio)  
    print("User said : ",text)
except: 
    print("Sorry, couldn't hear you!")