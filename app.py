from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/stt",methods=["POST"])
def stt():
    return render_template("speech_to_text.html")

@app.route("/tts",methods=["POST"])
def tts():
    return render_template("text_to_speech.html")


if __name__ == "__main__": 
    app.run(debug=True) 