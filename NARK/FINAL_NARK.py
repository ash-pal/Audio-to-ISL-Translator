import tkinter as tk                
from tkinter import *
import pyttsx3
import speech_recognition as sr
import datetime
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageTk
import string

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
entryquery=""
arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
isl_gif=['youarewrong','whereisthepolicestation','whereisthebathroom','whatsup','whatisyourname','whatdoesyourfatherdo',
'whatistodaysdate','whatistheproblem','wednesday','village','usa','tuesday','tomato','toilet','thursday','therewastrafficjam',
'temple','takecare','standup','sitdown','signlanguageinterpreter','shop','shallwegotogethertommorow','shallIhelpyou','saturday',
'punjab','pune','postoffice','policestation','pleasecallmelater','pakistan','openthedoor','nicetomeetyou','nagpur','mumbai',
'mile','may','letsgoforlunch','krishna','kerala','karnataka','june','july','job','ilovetoshop','ilikepinkcolour',
'ihadtosaysomethingbutiforgot','igotoatheatre','iamtired','iamthinking','iamsorry','iamfine','iamaclerk','hyderabad',
'hindu','hello','grapes','goodquestion','goodmorning','goodafternoon','flowerisbeautiful','doyouwatchtv',
'doyouwantsomethingtodrink','doyouwantsomethingtodrink','doyouhavemoney','dontworry','didyoufinishhomework','december',
'dasara','clinic','church','christmas','cat','bridge','becareful','banglore','banaras','banana','august','assam','areyouhungry',
'areyouangry','anyquestions','all','ahemdabad','address']

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def popupmsg(msg):
    popup = Tk()
    popup.title("Error")
    popup.geometry("300x80")
    label = Label(popup, text=msg, font=("Verdana", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.configure(background="#6b2aa3")
        self.title("N.A.R.K.")
        self.geometry("1900x1000")
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, AcceptAudio, AcceptText):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#6b2aa3")
        var1 = StringVar()
        var2 = StringVar()
        l1 = Label( self, textvariable=var1, relief=FLAT, height=5, width=25, font=("Times 50 bold"), bg="#a742ff", fg="black" )
        l1.place(x=300,y=20)
        l2 = Label( self, textvariable=var2, relief=FLAT, height=1, width=40, font=("Times 20 bold"), bg="#a742ff", fg="black" )
        l2.place(x=480,y=280)
        logo=tk.PhotoImage(file="wel2.png")
        w1 = Label(self, image=logo, height=100, width=400, bg="#a742ff")
        w1.image=logo
        w1.place(x=600,y=70)
        var1.set("N.A.R.K")
        var2.set("Audio to Sign Language Translator")
        hour=int(datetime.datetime.now().hour)
        m1=""
        if hour>=0 and hour<12:
            m1="Good Morning!"
        elif hour>=12 and hour<18:
            m1="Good Afternoon!"
        else:
            m1="Good Evening!"
        m2=m1+"\n Welcome to NARK audio to sign language translator! I am your assistant William Clark."
        m1=m1+" Welcome to NARK audio to sign language translator! I am your assistant William Clark."
        #mess.set(m1)
        speak(m1)
        mess=StringVar()
        system = Message( self, textvariable=mess, relief=RIDGE, font=("Comic 13 bold"), bg="#6b2aa3", justify=CENTER, aspect=700 )
        system.place(x=570,y=450)
        mess.set(m2)
        B1 = Button(self, text='INPUT AUDIO',height=2, width=20, command=lambda: controller.show_frame("AcceptAudio"))
        B1.place(x=550,y=600)
        B2 = Button(self, text='INPUT TEXT',height=2, width=20, command=lambda: controller.show_frame("AcceptText"))
        B2.place(x=900,y=600)


class AcceptAudio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#6b2aa3")
        var1 = StringVar()
        var2 = StringVar()
        l1 = Label( self, textvariable=var1, relief=FLAT, height=5, width=25, font=("Times 50 bold"), bg="#a742ff", fg="black" )
        l1.place(x=300,y=20)
        l2 = Label( self, textvariable=var2, relief=FLAT, height=1, width=40, font=("Times 20 bold"), bg="#a742ff", fg="black" )
        l2.place(x=480,y=280)
        logo=tk.PhotoImage(file="logo2.png")
        w1 = Label(self, image=logo, height=120, width=400, bg="#a742ff")
        w1.image=logo
        w1.place(x=600,y=60)
        var1.set("N.A.R.K")
        var2.set("Audio to Sign Language Translator")
        mess=StringVar()
        system = Message( self, textvariable=mess, relief=RIDGE, font=("Comic 13 bold"), bg="#6b2aa3", justify=LEFT, aspect=700 )
        system.place(x=570,y=450)
        mess.set("Click START to say something\nClick HOME to go to home page\nClick SHOW to see the respective Sign Language of the audio")
        B1 = Button(self, text='START',height=2, width=20, command=self.record)
        B1.place(x=420,y=650)
        B2= Button(self, text="HOME",height=2, width=20, command=lambda: controller.show_frame("HomePage"))
        B2.place(x=740,y=650)
        B3 = Button(self, text='SHOW',height=2, width=20, command=self.show)
        B3.place(x=1070,y=650)
        
    def record(self):
        global entryquery
        global usersaid
        query=""
        said=StringVar()
        userlabel = Label(self, text="User Said:", relief=FLAT, width=10, font=("Times 13 bold"), bg="#6b2aa3", fg="black" )
        userlabel.place(x=700,y=550)
        usersaid=Entry(self, textvariable=said, width=20,bg="#a742ff",relief=FLAT,font=("Times 13 "))
        usersaid.place(x=820,y=550)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            speak('Start Speaking')
            audio = r.listen(source)
            try:
                speak('Recognizing')
                query=r.recognize_google(audio)
                print("You said " + query)
                speak("You said")
                speak(query)
            except:
                popupmsg("Could not listen!")
                #speak("Could not listen")

        said.set(query)
        entryquery=query
        print("In record func entryquery:"+entryquery)


    def show(self):
        global arr
        global usersaid
        
        entryquery=usersaid.get()
        a=entryquery.lower() 
        if a=="":
            popupmsg("Input not given\nTry Again!")                
        for i in a:
            if i in string.punctuation:
                a= a.replace(i,"")                                
        if(a.replace(" ","") in isl_gif):
            app = Tk()
            app.title('Video Player')
            app.geometry("300x80")   
            neww = a.replace(" ","")  
            def snd1():
                os.system(neww+'.gif')
            var = IntVar()
            rb1 = Radiobutton(app, text= "Click to Play ", variable = var, value=1, command=snd1)
            rb1.pack()
            B1 = Button(app, text="Close", command = app.destroy)
            B1.pack(padx=10,pady=10,anchor=S)
                           
        else:
            for i in range(len(a)):
                if(a[i] in arr):
                    fig = plt.figure(0)
                    fig.canvas.set_window_title('N.A.R.K')
                    ImageAddress = 'letters/'+a[i]+'.jpg'
                    ImageItself = Image.open(ImageAddress)
                    ImageNumpyFormat = np.asarray(ImageItself)
                    plt.imshow(ImageNumpyFormat)
                    plt.axis('off')
                    plt.draw()
                    plt.pause(1.0) # pause how many seconds

                else:
                    continue
            plt.close()

class AcceptText(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#6b2aa3")
        var1 = StringVar()
        var2 = StringVar()
        l1 = Label( self, textvariable=var1, relief=FLAT, height=5, width=25, font=("Times 50 bold"), bg="#a742ff", fg="black" )
        l1.place(x=300,y=20)
        l2 = Label( self, textvariable=var2, relief=FLAT, height=1, width=40, font=("Times 20 bold"), bg="#a742ff", fg="black" )
        l2.place(x=480,y=280)
        logo=tk.PhotoImage(file="logo2.png")
        w1 = Label(self, image=logo, height=120, width=400, bg="#a742ff")
        w1.image=logo
        w1.place(x=600,y=60)
        var1.set("N.A.R.K")
        var2.set("Audio to Sign Language Translator")
        mess=StringVar()
        system = Message( self, textvariable=mess, relief=RIDGE, font=("Comic 13 bold"), bg="#6b2aa3", justify=LEFT, aspect=700 )
        system.place(x=570,y=450)
        mess.set("Click START to type\nClick HOME to go to home page\nClick SHOW to see the respective Sign Language of the audio")
        B1 = Button(self, text='START',height=2, width=20, command=self.get_text)
        B1.place(x=420,y=650)
        B2= tk.Button(self, text="HOME",height=2, width=20, command=lambda: controller.show_frame("HomePage"))
        B2.place(x=740,y=650)
        B3 = Button(self, text='SHOW',height=2, width=20, command=self.show)
        B3.place(x=1070,y=650)
        
    def get_text(self):
        global entryquery
        global usersaid
        query=""
        said=StringVar()
        userlabel = Label(self, text="User Says:", relief=FLAT, width=10, font=("Times 13 bold"), bg="#6b2aa3", fg="black" )
        userlabel.place(x=700,y=550)
        usersaid=Entry(self, textvariable=said, width=20,bg="#a742ff",relief=FLAT,font=("Times 13 "))
        usersaid.place(x=820,y=550)
        said.set(query)

    def show(self):
        global arr
        global usersaid
        print(usersaid.get())
        entryquery=usersaid.get()
        a=entryquery.lower() 
        if a=="":
            popupmsg("Input not given\nTry again!")              
        for i in a:
            if i in string.punctuation:
                a= a.replace(i,"")                                 

        if(a.replace(" ","") in isl_gif):
            app = Tk()
            app.title('Video Player')
            app.geometry("300x80")   
            neww = a.replace(" ","")  
            def snd1():
                os.system(neww+'.gif')
            var = IntVar()
            rb1 = Radiobutton(app, text= "Click to Play ", variable = var, value=1, command=snd1)
            rb1.pack()
            B1 = Button(app, text="Close", command = app.destroy)
            B1.pack(padx=10,pady=10,anchor=S)
            
                           
        else:                       
            for i in range(len(a)):
                if(a[i] in arr):
                    fig = plt.figure(0)
                    fig.canvas.set_window_title('N.A.R.K')
                    ImageAddress = 'letters/'+a[i]+'.jpg'
                    ImageItself = Image.open(ImageAddress)
                    ImageNumpyFormat = np.asarray(ImageItself)
                    plt.imshow(ImageNumpyFormat)
                    plt.axis('off')
                    plt.draw()
                    plt.pause(1.0) # pause how many seconds

                else:
                    continue
            plt.close()

app = MainWindow()
usersaid=tk.Entry()
app.mainloop()