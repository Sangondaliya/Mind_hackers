import pyttsx3
import speech_recognition as sr
import smtplib 
dict = {'girl':'gondaliyasan@gmail.com','project':'pythonproject110@gmail.com','pics':'sanpic2002@gmail.com'}
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

        print(f"User said:{query}\n")

        

    except Exception as e:

       speak("Say that again please...")

       return "None"

    return(query)

def sendEmail(sender,to,content):

    server = smtplib.SMTP('smtp.gmail.com',587) 

    server.ehlo()

    server.starttls() 
    
    # password=input('type your password')
    

    server.login(sender,'1!Sanskruti')
    

    server.sendmail(sender,to,content) 

while(True): 
    print("speak email to ... selectfrom(girl or projrct or pics)") 
    print("\nspeak exit ... to exit the program ")
    speak("email to ")

    query = listen().lower()

    if 'email to' in query:
         
        try:
            name = list(query.split()) 

            name = name[name.index('to')+1]
            print("senders email id...select from( girl,projrct ,pics) ")
            speak("senders email id")
            sender = dict[listen()]

            print("subject of the mail..")
            speak("subject of the mail")
            subject=listen()

            print("what should i say in message?")
            speak("what should i say in message")

            message = listen()

            content=("subject: {}\n\n{}".format(subject,message))

            to = dict[name]
            
            sendEmail(sender, to, content)

            speak("email has been sent")

        except Exception as e:

            print(e)

            speak("sorry unable to send the email at the moment.Try again")
    elif 'exit' in query:
        break  