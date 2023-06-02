from tkinter import *


import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your wiki ai will open sooner please wait ")

x.runAndWait()
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python index.py")
lbl=Button(root,text="WIKI AI DISTRIBUTION ",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)
def display():
    import os
    os.system("python time_1.py")

btns=Button(root,text="TIME",command=display)
btns.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btns.pack(side=LEFT,padx=10)
img=PhotoImage(file="core.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()

lbl2=Label(root,text="SEARCH ANYTHING:")
lbl2.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl2.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",20,"bold"))
entry.pack(padx=10,pady=20)
def sample1():
    import wikipedia
    x=entry.get()
    y=str(x)
    z=wikipedia.summary(y,sentences=1000)
    n=open(y+".txt","w")
    n.write(z)
    n.close()
    a="your file "+y+" was created sucessfully"
    import pyttsx3
    b=pyttsx3.init()
    b.say(a)
    b.runAndWait()
def sample2():
    import wikipedia
    x=entry.get()
    y=str(x)
    z=wikipedia.summary(y,sentences=1000)
    m=y+".txt"
    n=open(m,"w")
    n.write(z)
    n.close()
    a="your file "+y+" was created sucessfully"
    import pyttsx3
    b=pyttsx3.init()
    b.say(a)
    b.runAndWait()
    import subprocess
    subprocess.call(m,shell=True)
def sample3():
    import wikipedia
    x=entry.get()
    y=str(x)
    z=wikipedia.summary(y,sentences=100)
    import pyttsx3
    x=pyttsx3.init()
    x.say(z)
    x.runAndWait()
    
    
    
    

btn=Button(root,text="CREATE",command=sample1)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(side=LEFT,padx=100,pady=20)
btn2=Button(root,text="OPEN",command=sample2)
btn2.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn2.pack(side=LEFT,padx=135,pady=20)
btn3=Button(root,text="SPEAK",command=sample3)
btn3.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn3.pack(side=LEFT,padx=135,pady=20)
root.mainloop()
