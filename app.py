from flask import Flask, render_template, request
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
import pickle
temp_path = os.path.join(os.environ["USERPROFILE"])
path = temp_path+"/Downloads/"
global c
c = "vinay"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/stt", methods=["POST"])
def stt():
    return render_template("speech_to_text.html")


@app.route("/tts", methods=["POST"])
def tts():
    return render_template("text_to_speech.html")

@app.route("/speech_to_text_using_file",methods=["POST"])
def speech_to_text():
    file_name = "your_file.mp3"

    r  = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        r.energy_threshold = 4000
        audio = r.listen(source) 
        text = r.recognize_google(audio,language=c)  
    return render_template("stt3.html",stt = text)    

@app.route("/main", methods=["POST"])
def main():
    a = request.form['input']
    if a == 'mic':
        c = request.form['language']
        if c == "hindi":
            m = "hi"
        else:
            m = "en"
        return render_template("stt2.html",lang=m)
    elif a == 'file':
        c = request.form['language']
        n = request.files["mp3_file"]
        if c == "hindi":
            m = "hi"
        else:
            m = "en"
        n.save("D:/programming/Python/Machine_Learning_Projects/project_speech_to_text_or_text_to_speech/your_file.mp3")
        speech_to_text()
    elif a == 'write':
        return render_template("tts2.html")
    elif a == 'upload':
        n = request.files['file']
        n.save("D:/programming/Python/Machine_Learning_Projects/project_speech_to_text_or_text_to_speech/your_file.txt")   
        return render_template("tts3.html") 

@app.route("/write",methods=["POST"])
def write():
    return render_template("tts2.html")


@app.route('/download_file',methods=['POST'])
def dnd():
    a = request.form['converted_text']
    z = open(path+"file.txt","w")
    z.write(a)
    z.close()
    return render_template("stt2.html")


@app.route("/text-to-speech-using-file",methods=['POST'])
def text_to_speech_using_file():
    text = open("your_file.txt")
    a = text.read()
    mp3 = gTTS(a)
    text.close()
    mp3.save(path+"file.mp3")
    return render_template("tts3.html",x="File Download Successfully")

@app.route("/text-to-speech",methods=['POST'])
def text_to_speech():
    text = request.form['text']
    mp3 = gTTS(text)
    mp3.save(path+"file.mp3")
    return render_template("tts2.html",x="File Download Successfully")

if __name__ == "__main__":
    app.run(debug=True)
