from flask import Flask ,render_template,request
import pyttsx3
import speech_recognition as sr
import time
#import main
engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def listen(): 

    r = sr.Recognizer()


    with sr.Microphone() as source:

        print("Iam listening.....")

        r.pause_threshold=1

        audio = r.listen(source)

    try:

        print("Recognizing.....")

        query = r.recognize_google(audio, language = 'en-in') 

        print("User said:{}\n".format(query))

    except Exception as e:
        print(e)

        speak("Say that again please...")

        return "None"

    return(query)
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
time.sleep(0.1)
speak('welcome ')
time.sleep(0.5)
speak(' ')
speak('please fill the detalis')
time.sleep(0.5)
while True:
    speak(' ')
    speak("enter your name")
    time.sleep(0.1)
    Name=listen()
    print(Name)
    if Name=='exit':
        break
@app.route('/form')
def form():
    request.form['name']=Name
    return render_template('index.html',name=Name)






@app.route("/nirma",methods=['GET','POST'])
def nirma():
    if request.method=="POST":
        data=request.form["nirma"]
    return render_template("index.html",my_data='San')
if __name__ == "__main__":
    #san.run
    app.run(debug=True)