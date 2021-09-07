from flask import Flask, render_template, request
import speech_recognition as sr

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
        n = request.files['file']
        n.save('D:/programming/Python/Machine Learning Projects/project_speech_to_text_or_text_to_speech/voice.mp3')
        return render_template("stt3.html")
    elif a == 'write':
        return render_template("tts2.html")
    elif a == 'upload':
        n = request.files['file']
        n.save("D:/programming/Python/Machine Learning Projects/project_speech_to_text_or_text_to_speech/text.txt")   
        return render_template("tts3.html") 

@app.route("/write",methods=["POST"])
def write():
    return render_template("tts2.html")

@app.route('/download_file',methods=['POST'])
def dnd():
    a = request.form['converted_text']
    z = open("your file.txt","w")
    z.write(a)
    z.close()
    return render_template("stt2.html")

@app.route("/speech-to-text")
def speech_to_text():
    a = request.form["mp3_file"]
    
    r  = sr.Recognizer()

    with sr.Microphone() as source:
        r.energy_threshold = 4000
        audio = r.listen(source) 
        text = r.recognize_google(audio)  
        print("User said : ",text)
        a = open("voice.txt",'w')
        a.write(text)
        a.close()
        
if __name__ == "__main__":
    app.run(debug=True)
