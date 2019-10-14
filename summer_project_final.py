from tkinter import *
import time as t
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
import random
from tkinter import *
import webbrowser
import dbproject
import wikipedia


import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
roots=Tk()
speak("WELCOME")
def logs():
    roots.destroy()
    def ver1():
        a=v1.get()
        b=v2.get()
        c=v3.get()
        d=v4.get()
        
        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or "@gmail.com" not in v2.get():
              speak("PLEASE CHECK VALUES or Insert Email correctly")
              tkinter.messagebox.showinfo("Window","PLEASE check the VALUES")
              
        elif len(a)!=0 and len(b)!=0 and len(c)!=0 and len(d)!=0:
            w=speak("WELCOME")
            r=speak(c)
        
            
            tkinter.messagebox.showinfo("Window","VERIFIED NOW YOU CAN SUBMIT")
            btn1.config(state=NORMAL)
            
    window = Tk()
    window.title("Login Page")
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
      
    window.geometry('570x420')
    window.resizable(width=False, height=False)
      
    
    l2 = Label(window ,text = "PLEASE SIGN UP",font=25).grid(row=0,column=1,pady=10)
    a = Label(window ,text = "First Name :").grid(row = 1,column=0,padx=10,pady=10)
    b = Label(window ,text = "Last Name :").grid(row = 2,column=0,padx=10,pady=10)
    c = Label(window ,text = "City :").grid(row = 3,column = 0,padx=10,pady=10)
    d = Label(window ,text = "Email Id :").grid(row = 4,column = 0,padx=10,pady=10)
    h=  Label(window ,text = "Hint:only gmail accounts").grid(row = 4,column =3 ,padx=10,pady=10)
    e = Label(window ,text = "Contact Number :").grid(row = 5,column = 0,padx=10,pady=10)
    a1 = Entry(window,textvariable=v1).grid(row = 2,column = 1,padx=10,pady=10)
    c1 = Entry(window,textvariable=v2).grid(row = 4,column = 1,padx=10,pady=10)
    d1 = Entry(window,textvariable=v3).grid(row = 1,column = 1,padx=10,pady=10)
    e1 = Entry(window,textvariable=v4).grid(row = 5,column = 1,padx=10,pady=10)
    city=("Delhi", "Mumbai", "Haryana", "Chattisarh")
    t1=StringVar()
    cb=Combobox(window, values=city,textvariable=t1,state='readonly').grid(row = 3,column = 1,padx=10,pady=10)
    def clicked():
        x=v4.get()
        a=v1.get()
        b=v2.get()
        c=v3.get()
        d=v4.get()
        if (len(x)>10 or len(x)<10):
            tkinter.messagebox.showerror("Window","INVALID NUMBER")
            
        else:
              
            ran=random.randint(100,999)
            ans=StringVar()
            ans.set(ran)
            Entry(window,  text = "%s" %(ans) ).grid(row=6, column=1)
              
  
    temp1=Label(window,text="\n").grid(row=7,column=0)
    b1=StringVar()
    btn2=Button(window,text="Generate OTP",command=clicked).grid(row=6,column=0,padx=10,pady=10)
          
      

  #VER------------------------------------------------------
    def ver():
        window.destroy()
                    
        def showing():
            a=var2.get()
            b=var3.get()
                      
            if len(a)==0 and len(b)==0:  
                         
                pass                          
            else:
                       
                root.destroy()
#MAIN GUI BEGINS                 
                
                def clear():
                    E1.delete(0,END)
                    E2.delete(0,END)
                    E3.delete(0,END)
                    E4.delete(0,END)
                    List1.delete(0,END)
                
                
                def get_selected_row(event):
                    global selected_tuple
                    try:
                        

                        index=List1.curselection()[0]
                        selected_tuple=List1.get(index)
                        E1.delete(0,END)
                        E1.insert(END,selected_tuple[1])
                        E2.delete(0,END)
                        E2.insert(END,selected_tuple[2])
                        E3.delete(0,END)
                        E3.insert(END,selected_tuple[3])
                        E4.delete(0,END)
                        E4.insert(END,selected_tuple[4])
                    except(IndexError):
                        pass
                    
                    index=List1.curselection()[0]
                    selected_tuple=List1.get(index)
                    E1.delete(0,END)
                    E1.insert(END,selected_tuple[1])
                    E2.delete(0,END)
                    E2.insert(END,selected_tuple[2])
                    E3.delete(0,END)
                    E3.insert(END,selected_tuple[3])
                    E4.delete(0,END)
                    E4.insert(END,selected_tuple[4])
                    
                def view_command():
                    List1.delete(0,END)
                    for row in dbproject.view():
                        List1.insert(END,row)
                
                def search_command():
                    List1.delete(0,END)
                    for row in dbproject.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
                        List1.insert(END,row)
                        
                def add_command():
                    try:
                     
                        global selected_tuple
                        index=List1.curselection()[0]
                        selected_tuple=List1.get(index)
                        E1.delete(0,END)
                        E1.insert(END,selected_tuple[1])
                        E2.delete(0,END)
                        E2.insert(END,selected_tuple[2])
                        E3.delete(0,END)
                        E3.insert(END,selected_tuple[3])
                        E4.delete(0,END)
                        E4.insert(END,selected_tuple[4])
                    except Exception:
                        pass
                    a=title_text.get()
                    b=author_text.get()
                    c=year_text.get()
                    d=isbn_text.get()
                    if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0):
                        tkinter.messagebox.showinfo("Window","PLEASE ENTER ALL THE DETTAILS")
                        dbproject.delete(selected_tuple[0]) 
                    else:
                        
                        dbproject.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
                        List1.delete(0,END)
                        List1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
                        view_command()
                def delete_command():
                    a=title_text.get()
                    b=author_text.get()
                    c=year_text.get()
                    d=isbn_text.get()
                    if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0):
                        tkinter.messagebox.showinfo("Window","PLEASE SELECT VALUE TO BE DELETE")
                    else:
                        speak("DELETING")
                        E1.delete(0,END)
                        E2.delete(0,END)
                        E3.delete(0,END)
                        E4.delete(0,END)
                        List1.delete(0,selected_tuple[0])
                        dbproject.delete(selected_tuple[0])
                        view_command()
                        
                def update_command():
                    a=title_text.get()
                    b=author_text.get()
                    c=year_text.get()
                    d=isbn_text.get()
                    if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0):
                        tkinter.messagebox.showinfo("Window","PLEASE SELECT VALUE TO UPDATE")
                    else:
                        speak("Updating")
                        dbproject.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())   
                win=Tk()
                def explore():
                    win.destroy()
                    def speak(audio):
                        engine.say(audio)
                        engine.runAndWait()
                    def gets():
                        
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                           
                              
                            answer_var=wikipedia.summary(entry_var,sentences=2)
                            
                            text.insert(END,answer_var)
                        except Exception:
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                    
                    
                    def ebook():
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                            text.insert(INSERT,"OPENING....")
                            speak("Opening  Books")
                            webbrowser.open("litnet.com")
                            text.delete(1.0,END)
                        except Exception:
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                            
                    def fan():
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                            text.insert(END,"OPENING....")
                            speak("Opening Fan Fiction Books")
                            webbrowser.open("https://litnet.com/en/top/fanfiction")
                            text.delete(1.0,END)
                        except Exception:
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                    def romantic():
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                             text.insert(END,"OPENING....")
                             speak("opening romantic books")
                             
                             webbrowser.open("https://litnet.com/en/top/romance")
                             text.delete(1.0,END)
                        except Exception:
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                    def thriller():
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                            text.insert(END,"OPENING....")
                            t.sleep(2)
                            speak("Opening Thriller Books")
                            webbrowser.open("https://litnet.com/en/top/thrillers-suspense")
                            text.delete(1.0,END)
                        except Exception:
                           
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                    def mystery():
                        entry_var=entry.get()
                        text.delete(1.0,END)
                        try:
                            text.insert(END,"OPENING....")
                            speak("Opening Mystery Books")
                            webbrowser.open("https://litnet.com/en/top/mystery")
                            text.delete(0,END)
                        except Exception:
                            
                            text.insert(END,"PLEASE CHECK THE VALUES OR INTERNET CONNECTION")
                    def speaker():
                        entry_var=entry.get()
                        try:
                            answer_var=wikipedia.summary(entry_var,sentences=2)
                            speak(answer_var)
                        except Exception:
                            speak("NOTHING TO READ.Please search something")
                            
                    spk=Tk()
                    spk.geometry("600x500")
                    spk.resizable(width=False, height=False)
                    spk.title("Book Search")
                    
                    entry=Entry(spk)
                    entry.place(x=200,y=430)
                    B1=Button(spk,text='Search',bg='yellow',fg='black',font=('',12),command=gets)
                    B1.place(x=350,y=425)
                    text=Text(spk,height=15,width=55)
                    text.place(x=75,y=170)
                    
                    sp=Frame(spk, bg="#C8F9C4", highlightbackground="Black", highlightthickness="2", height="200", width="200")
                    sp.place(x=0,y=10)
                    B2=Button(sp,text='Fiction Books',bg='Black',fg='#ffffff',font=('',12),command=fan)
                    B2.grid(row=0,column=0,padx=30, pady=10)
                    B3=Button(sp,text='Thriller Books',bg='Black',fg='#ffffff',font=('',12),command=thriller)
                    B3.grid(row=0,column=1,padx=30, pady=10)
                    B4=Button(sp,text='Romantic Books',bg='Black',fg='#ffffff',font=('',12),command=romantic)
                    B4.grid(row=0,column=2,padx=30, pady=10)
                    B5=Button(sp,text='Mystery Books',bg='Black',fg='#ffffff',font=('',12),command=mystery)
                    B5.grid(row=1,column=0,padx=30, pady=10)
                    B7=Button(sp,text='E-Books',bg='Black',fg='#ffffff',font=('',12),command=ebook)
                    B7.grid(row=1,column=1,padx=10, pady=10)
                    B6=Button(sp,text='Read',bg='Blue',fg='black',font=('',12),command=speaker)
                    B6.grid(row=1,column=2,padx=10, pady=10)
                    
                    
                    sp.mainloop()

                    #AI PART ENDS   
#                 
                win.geometry("650x445")
                win.resizable(width=False, height=False)
                win.title("Library Management system")
                
                L1=Label(win,text='Title :',bg='Snow3',font=('',12))
                L1.grid(row=0,column=0,padx=30,pady=10)
                title_text=StringVar()
                
                E1=Entry(win,font=('',12),textvariable=title_text)
                E1.grid(row=0,column=1)
                
                L2=Label(win,text='Author :',bg='Snow3',font=('',12))
                L2.grid(row=0,column=2,padx=5,pady=10)
                author_text=StringVar()
                
                E2=Entry(win,font=('',12),textvariable=author_text)
                E2.grid(row=0,column=3)
                
                L3=Label(win,text='Year :',bg='Snow3',font=('',12))
                L3.grid(row=1,column=0,padx=30,pady=10)
                year_text=StringVar()
                E3=Entry(win,font=('',12),textvariable=year_text)
                E3.grid(row=1,column=1)
                L4=Label(win,text='ISBN :',bg='Snow3',font=('',12))
                L4.grid(row=1,column=2,padx=5,pady=10)
                isbn_text=StringVar()
                E4=Entry(win,font=('',12),textvariable=isbn_text)
                E4.grid(row=1,column=3)
                List1=Listbox(win,height=10,width=45)
                List1.grid(row=3,column=1,columnspan=8,rowspan=3,pady=20)
                List1.bind('<<ListboxSelect>>',get_selected_row)
                
                buttonframe=Frame(win, bg="#C8F9C4", highlightbackground="Black", highlightthickness="2", height="200", width="200")
                buttonframe.place(x=35,y=280)
                
                B1=Button(buttonframe,text='View All',bg='Black',fg='#ffffff',font=('',12),command=view_command)
                B1.grid(row=0,column=0,padx=30,pady=10)
                B2=Button(buttonframe,text='Search Entry',bg='Black',fg='#ffffff',font=('',12),command=search_command)
                B2.grid(row=0,column=1,padx=30, pady=10)
                B3=Button(buttonframe,text='Add Entry',bg='Black',fg='#ffffff',font=('',12),command=add_command)
                B3.grid(row=0,column=2,padx=30, pady=10)
                B4=Button(buttonframe,text='Update Selected',bg='Black',fg='#ffffff',font=('',12),command=update_command)
                B4.grid(row=1,column=0,padx=30, pady=10)
                B5=Button(buttonframe,text='Delete Selected',bg='Black',fg='#ffffff',font=('',12),command=delete_command)
                B5.grid(row=1,column=1,padx=30, pady=10)
                B6=Button(buttonframe,text='Close',bg='Black',fg='#ffffff',font=('',12),command=win.destroy)
                B6.grid(row=1,column=2,padx=10, pady=10)
                B7=Button(buttonframe,text='Clear ALL',bg='Black',fg='#ffffff',font=('',12),command=clear)
                B7.grid(row=2,column=1,padx=10, pady=10)
                B7=Button(buttonframe,text='EXPLORE MORE BOOKS',bg='Blue',fg='black',font=('',12),command=explore)
                B7.grid(row=2,column=2,padx=10, pady=10)
                try:
                     
                    global selected_tuple
                    index=List1.curselection()[0]
                    selected_tuple=List1.get(index)
                    E1.delete(0,END)
                    E1.insert(END,selected_tuple[1])
                    E2.delete(0,END)
                    E2.insert(END,selected_tuple[2])
                    E3.delete(0,END)
                    E3.insert(END,selected_tuple[3])
                    E4.delete(0,END)
                    E4.insert(END,selected_tuple[4])
                except(IndexError):
                    pass
                win.mainloop()
#MAIN GUI ENDS                   
        
        def names():
     
            a=var2.get()
            b=var3.get()
           
                
            if len(a)==0 or len(b)==0:
                var.set("PLEASE ENTER NAME AND PASSWORD!!")
         
         
                    
         
            elif len(a)!=0 and len(b)!=0 and int(b) in range(100,100000):
                x=var2.get()
                var.set("VERIFIED"+" "+"WELCOME"+" "+var2.get()+" "+var10)
                speak("WELCOME")
                speak(x)
                B7.config(state=NORMAL)
            
            else:
                var.set("INCORRECT")
 
             
        root=Tk()
        root.geometry("600x300")
        root.resizable(width=False, height=False)
        var=StringVar()
        var10=StringVar()
        var11=StringVar()
    
    
        var10="(CLICK ON LOGIN)"
        var12=StringVar()
    #CHANGE HERE|||||||||||||||||}
        l1=Label(root,textvariable=var,font=('arial',18))
        l1.place(relx=0.5, rely=0.8, anchor=CENTER)
        l10=Label(root,textvariable=var10).grid(row=15,column=4)
        l12=Label(root,textvariable=var12).grid(row=5,column=11)
        l2=Label(root,text="NAME").grid(row=2,column=7)
        var2=StringVar()
        e2=Entry(root,textvariable=var2).grid(row=2,column=9)
        l3=Label(root,text="PASSWORD:").grid(row=4,column=7)
        var3=StringVar()
        e3=Entry(root,textvariable=var3,show='*').grid(row=4,column=9)
        def show_pass1():
            e3=Entry(root,textvariable=var3).grid(row=4,column=9)
        def show_pass2():
            e3=Entry(root,textvariable=var3,show='*').grid(row=4,column=9)   

        B6=Button(text='VERIFY',command=names)
        B6.grid(row=7,column=7)
        B7=Button(text='LOG IN',command=showing)
        B7.config(state=DISABLED)
        B7.grid(row=7,column=9)
        B8=Button(text="UNHIDE",command=show_pass1)
        B8.grid(row=4,column=11)
        B9=Button(text="HIDE",command=show_pass2)
        B9.grid(row=4,column=19)
        
        root.mainloop()
#VER ENDS        
    btn4 = ttk.Button(window ,text="Already a Member ?",command=ver).grid(row=8,column=1)
    temp2=Label(window,text="\n").grid(row=7,column=0)
    btn1 =Button(window ,text='SUBMIT',command=ver)
    btn1.config(state=DISABLED)
    btn1.grid(row=9,column=1,padx=20,pady=10)
    btn4 = ttk.Button(window ,text="Verify",command=ver1)
    btn4.grid(row=8,column=0)
                        
    window.mainloop()
#FUNCTION FIRST ENDS 
l=Label(roots,text="THE BOOK STORE",font=('latin',30),fg='Black',bg="White")
l.grid(row=0,column=9,sticky=W)
 
 
l2=Button(roots,text="Sign Up",font=('arial',10),fg='White',bg="black",command=logs)
l2.grid(row=8,column=9,sticky=W+N+S+E)
canvas=Canvas(roots,height=100,width=360)
canvas.grid(row=3,column=9,sticky=E)
my_image=PhotoImage(file="lib.gif")
canvas.create_image(70,70,image=my_image)

roots.mainloop()
#FIRST PAGE ENDS 
