import pyttsx3
import speech_recognition as sr
import webbrowser as web 
engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def main():
    #path ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    path =  "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("speak the website for eg youtube.com,instagram.com,google.com")
        print("listing ..")
        speak("listing ..")
        
  
        audio = r.listen(source)

        print("Recognizing ...")

        try:
            dest=r.recognize_google(audio)
            print("Did you say  "+ dest)
            print("wait it may take some time ")
            speak("wait it may take some time ")

            a=web.get(path).open(dest)
            speak("opening it.")
            open(a)
        except Exception as e:
            print("Error.."+str(e))  

if __name__ =="__main__":
    main()
                         