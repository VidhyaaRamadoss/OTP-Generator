from tkinter import *
import math,random


def gopt2():
    values="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    otp=""
    global Otpq
    
    size=len(values)
    for i in range(8):
        otp+=values[math.floor(random.random()*size)]
    Otpq=otp
def main():
   Otpq="xyz"
   root = Tk() 
   root.geometry("300x300") 
   root.title("OTP")
   Label(root, text='OTP GENERATOR').pack()
   frame = Frame(root) 
   frame.pack() 
   redbutton = Button(frame, text = 'CLICK', fg ='red',command=gopt2) 
   redbutton.pack( side = LEFT)
   Label(root).pack()
   messageVar = Message(root, text = Otpq) 
   messageVar.config(bg='lightgreen') 
   messageVar.pack( ) 
   root.mainloop() 

if __name__ == "__main__":
    main()