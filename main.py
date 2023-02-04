import pyttsx3
import speech_recognition as sr
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import time

engine = pyttsx3.init('sapi5') 

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)
    time.sleep(0.1)

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

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
model = load_model('mp_hand_gesture')
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)
cap = cv2.VideoCapture(0)

while True:
    

    _, frame = cap.read()

    x, y, c = frame.shape

    
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    result = hands.process(framergb)

    # print(result)
    
    className = ''

    
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

    
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    speak(className)
    k=cv2.waitKey(3)

    if  k == ord('q') or k==27:
        break

   
    cv2.imshow("Output", frame) 

    
    # query = listen().lower()
    # if 'exit' in query:
    #     break


cap.release()

cv2.destroyAllWindows()