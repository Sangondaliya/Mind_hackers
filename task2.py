import pyttsx3
import speech_recognition as sr

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

def square_and_circle():
    
    import turtle as tu
    import time as t 

    wd = tu.Screen()
    wd.title("Animation Demo 1 ")
    wd.bgcolor("black")

    player = tu.Turtle()
    player.shape("square")
    player.color("yellow")

    while True :
       player.shape("square")
       t.sleep(0.5)
       player.shape("circle")
       t.sleep(0.5)
       wd.mainloop()

def figure():
    import turtle 

    t= turtle.Turtle()
    s = turtle.Screen()

    s.bgcolor("black")
    t.width(2)
    t.speed(15)

    col=('yellow','green','blue','red')
    for i in range(300):
      t.pencolor(col[i%4])
      t.forward(i*4)
      t.right(137)


def Analog_clock():
    import time
    import turtle
    wn =turtle.Screen()
    wn.setup(width=600,height=600)
    wn.title("simple Anaglod Clock")
    wn.bgcolor("black")
    wn.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)

    def draw_clock(h,m,s,pen):
       pen.up()
       pen.goto(0,210)
       pen.setheading(180)
       pen.color("orange")
       pen.pendown()
       pen.circle(210)

       pen.penup()
       pen.goto(0,0)
       pen.setheading(90)

       for _ in range(12):
          pen.fd(190)
          pen.pendown()
          pen.fd(20)
          pen.penup()
          pen.goto(0,0)
          pen.rt(30)

       pen.penup()
       pen.goto(0,0)
       pen.color("aqua")
       pen.setheading(90)
       angle = (h/12)*360    
       pen.rt(angle)
       pen.pendown()
       pen.fd(80)

       pen.penup()
       pen.goto(0,0)
       pen.color("yellow")
       pen.setheading(90)
       angle = (m/60)*360    
       pen.rt(angle)
       pen.pendown()
       pen.fd(150)

       pen.penup()
       pen.goto(0,0)
       pen.color("royalblue")
       pen.setheading(90)
       angle = (s/60)*360    
       pen.rt(angle)
       pen.pendown()
       pen.fd(170)

    while True:
        h=int(time.strftime("%I"))
        m=int(time.strftime("%M"))
        s=int(time.strftime("%S"))
        draw_clock(h,m,s,pen)
        wn.update()
        time.sleep(1)
        pen.clear() 
  
    wn.mainloop()
        
        


while(True):  

    print("speak select 1.. for simple animation")
    print("speak select 2..for the amazing spriral")
    print("speak select 3..for analog clock ")
    print("speak exit to exit the program ")
    speak("speak select ..")

    query = listen().lower()

    if 'select' in query:
         
        try:
            name = list(query.split()) 
            name = name[name.index('select')+1]
            if name == 'one':
                square_and_circle()

            elif name == '2':
                figure()

            elif name == '3':
                Analog_clock()

            # elif name == '4':
            #     runing_man()
        except Exception as e:

            print(e)

            speak("sorry unable to select it please .Try again")
    elif 'exit' in query:
        break               


