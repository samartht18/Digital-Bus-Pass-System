from tkinter import *
import qrcode

import csv
global search_photo
global register_photo

#login_photo = PhotoImage(file="login.png")



def regiuser():
    win.destroy()
    reg = Tk()      #Constructing the register window
    reg.title("E-BUS PASS")

    photo = PhotoImage(file="bus.ico")
    reg.iconphoto(False, photo)

    regiframe = Frame(reg)
    regiframe.grid(padx=100, pady=100)

    def store():
        user1 = e1.get()
        pass1 = e2.get()
        pass2 = e3.get()
        if len(pass1) < 8 :
            i1 = Label(regiframe, text="*Password should contain at least 8 characters,please try again..."+"\n"+"( For strong password ; Use uppercase letters, lowercase letters, numbers , symbols like {!,@,#,$,%,&} ).", fg='red',
                       font=("Times 30 bold underline", 10))
            i1.grid(row=3,column=0, columnspan=2)
        elif pass1 !=pass2 :
            i1 = Label(regiframe,
                       text="* Password is not confirmed, please enter a valid password",
                       fg='red',
                       font=("Times 30 bold underline", 10))
            i1.grid(row=3, column=0, columnspan=2)

        else :

           fh = open("newuser.txt", "a")
           fh.write(user1+"," + pass1+"\n")
           fh.close()
           reg.destroy()
           loginfun()

    n1 = Label(regiframe, text="Enter your username :",font=("Times 30 bold underline", 15))
    n1.grid(row=0, column=0, columnspan=2)

    n2 = Label(regiframe, text="Enter your password :",font=("Times 30 bold underline", 15))
    n2.grid(row=1, column=0, columnspan=2)

    n3 = Button(regiframe, text="Quit", fg="RED", command=quit, height=1, width=5)
    n3.grid(row=0, column=6, padx=25, pady=25, columnspan=3)

    n4 = Label(regiframe, text="Confirm your password :", font=("Times 30 bold underline", 15))
    n4.grid(row=2, column=0, columnspan=2)

    e1 = Entry(regiframe)
    e1.grid(row=0, column=3)

    e2 = Entry(regiframe,show="*")
    e2.grid(row=1, column=3)

    e3 = Entry(regiframe, show="*")
    e3.grid(row=2, column=3)

    global register_photo
    register_photo = PhotoImage(file="submit.png")
    r1 = Button(regiframe, text="signup", command=store,image = register_photo,height=50,width=180)
    r1.grid(row=4,column=3,padx=25, pady=25)

    reg.grid_columnconfigure(0, weight=1)
    reg.grid_rowconfigure(0, weight=1)
    reg.configure(background='coral1')

def log1 ():
    win.destroy()
    loginfun()

def loginfun():
    root = Tk()     #Constructing the login window
    root.title("E-BUS PASS")

    photo = PhotoImage(file="bus.ico")
    root.iconphoto(False, photo)

    lf = Frame(root)
    lf.grid(padx=50, pady=50)

    def check():
        x1 = u1.get()
        x2 = p1.get()
        # d=x1+" "+x2
        with open("newuser.txt", "r") as file:
            fh = csv.reader(file, delimiter=",", lineterminator="\n")
            for row in fh:
                if row[0] == x1:
                    if row[1] == x2:
                        file.close()
                        afterlogin()
                        break
            else:
                i3 = Label(lf, text="*Invalid username or password,please try again...", fg='red',font=("Times 30 bold underline", 15))
                i3.grid(row=4, columnspan=2)

    def afterlogin():
        root.destroy()
        start = Tk()       #Constructing after login window
        start.title("E-BUS PASS")

        photo = PhotoImage(file="bus.ico")
        start.iconphoto(False, photo)

        start.grid_columnconfigure(0, weight=1)
        start.grid_rowconfigure(0, weight=1)
        frame=Frame(start)
        frame.grid(padx=50, pady=50)

        global QR_code
        QR_code=PhotoImage(file="login.png")

        def qr():
            start.destroy()
            start1= Tk()
            start1.title("E-BUS PASS")

            photo = PhotoImage(file="bus.ico")
            start1.iconphoto(False, photo)

            qrframe = Frame(start1)
            qrframe.grid(padx=50, pady=50)

            global QR_code
            QR_code = PhotoImage(file="QR_code.png")
            n1 = Button(qrframe, text="My QR code",image=QR_code, command=qr, height=500, width=500)
            n1.grid(row=2 , column=0,sticky=NSEW, padx=10, pady=10)

            n1= Label(qrframe, text='scan this to generate your e-pass', font=("Times 30 bold underline", 15))
            n1.grid(row=1, sticky=NSEW, column=0, columnspan=3)

            n2 = Button(qrframe, text="Quit", fg="RED", command=quit, height=1, width=5)
            n2.grid(row=0, column=6, padx=25, pady=25, columnspan=3)

            start1.grid_columnconfigure(0, weight=1)
            start1.grid_rowconfigure(0, weight=1)
            start1.configure(background='coral1')
            start1.mainloop()

        def logout():
            start.destroy()
            l1 = Tk()
            l1.title("E-BUS PASS")

            photo = PhotoImage(file="bus.ico")
            l1.iconphoto(False, photo)

            logoutframe = Frame(l1)
            logoutframe.grid(padx=50, pady=50)

            i3 = Label(logoutframe, text="You have successfully Logged Out ,"+"\n"+"Thank you for visiting E-bus pass !!!", fg='Green', font=("Times 30 bold underline", 15))
            i3.grid(row=0, columnspan=2)

        def qr1():
            start3 = Tk()
            start3.title("E-BUS PASS")

            photo = PhotoImage(file="bus.ico")
            start3.iconphoto(False, photo)

            qr1frame = Frame(start3)
            qr1frame.grid(padx=50, pady=50)

            global QR_code
            QR_code = PhotoImage(file="QR_code.png")
            n1 = Button(qr1frame, text="My QR code", image=QR_code, command=qr1, height=500, width=500)
            n1.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10)

            n1 = Label(qr1frame, text='scan this to generate your e-pass', font=("Times 30 bold underline", 15))
            n1.grid(row=1, sticky=NSEW, column=0, columnspan=3)

            n2 = Button(qr1frame, text="Quit", fg="RED", command=quit, height=1, width=5)
            n2.grid(row=0, column=6, padx=25, pady=25, columnspan=3)

            start3.grid_columnconfigure(0, weight=1)
            start3.grid_rowconfigure(0, weight=1)
            start3.configure(background='coral1')
            start3.mainloop()



        global get_pass
        def get_pass():
            start.destroy()
            start2 = Tk()
            start2.title("E-BUS PASS")

            photo = PhotoImage(file="bus.ico")
            start2.iconphoto(False, photo)

            getframe = Frame(start2)
            getframe.grid(padx=50, pady=50)

            def store1():
                p1 = e1.get()
                p2 = e2.get()
                p3 = e3.get()
                p4 = e4.get()
                p5 = e5.get()
                fh = open("passdetail.txt", "a")
                fh.write(
                    "Name : " + p1 + "\n" + "Start date:" + p2 + "\n" + "End date:" + p3 + "\n" + "Route: From " + p4 + " TO " + p5 + "\n" + "\n")
                fh.close()
                qr = qrcode.make("Name : " + p1 + "\n" + "Start date:" + p2 + "\n" + "End date:" + p3 + "\n" + "Route: From " + p4 + " TO " + p5 + "\n" + "\n")
                qr.save('QR_code.png')
                start2.destroy()
                qr1()

            n1 = Label( getframe, text="Enter your Name:", font=("Times 30 bold underline", 15))
            n1.grid(row=1, column=0)

            n2 = Label(getframe, text="PASS detail's", font=("Times 30 bold underline", 25))
            n2.grid(row=0,sticky=NSEW,column=0,columnspan=2)

            n3 = Label( getframe, text="Start date:", font=("Times 30 bold underline", 15))
            n3.grid(row=2, column=0)

            n4 = Label(getframe, text="End date:", font=("Times 30 bold underline", 15))
            n4.grid(row=3, column=0)

            n5 = Label(getframe, text="Route", font=("Times 30 bold underline", 20))
            n5.grid(row=4, column=0)

            n6 = Label(getframe, text="From (enter the starting location):", font=("Times 30 bold underline", 15))
            n6.grid(row=5, column=0)

            n7 = Label(getframe, text="To (enter the destination):", font=("Times 30 bold underline", 15))
            n7.grid(row=6, column=0)

            n8 = Label(getframe, text=" (DD/MM/YYYY)", fg="RED",font=("Times 30 bold underline", 15))
            n8.grid(row=2, column=2)

            n9 = Label(getframe, text=" (DD/MM/YYYY)", fg="RED", font=("Times 30 bold underline", 15))
            n9.grid(row=3, column=2)

            

            e1 = Entry( getframe)
            e1.grid(row=1, column=1)

            e2 = Entry( getframe)
            e2.grid(row=2, column=1)

            e3 = Entry(getframe)
            e3.grid(row=3, column=1)

           # OPTIONS = [
           #     "Jan",
           #     "Feb",
           #     "Mar"
           # ]  # etc

           # variable = tk.StringVar(start2)
          # default value

           # w = tk.OptionMenu(start2, variable, *OPTIONS)
           # w.grid(row=3, column=0)

            #sf =variable.get()
            #print(sf)

            e4 = Entry(getframe)
            e4.grid(row=5, column=1)

            e5 = Entry(getframe)
            e5.grid(row=6, column=1)

            s1 = Button(getframe, text="Submit and Show My QR Code",bg="CadetBlue1",fg="brown4",command=store1,relief=GROOVE,activeforeground = "yellow",activebackground = "Green",height=5, width=15)
            s1.grid(row=7, column=1, sticky=NSEW, padx=10, pady=10,columnspan=3)

            n2 = Button(getframe, text="Quit", fg="RED", command=quit, height=1, width=5)
            n2.grid(row=8, column=3, padx=25, pady=25, columnspan=3)

            start2.grid_columnconfigure(0, weight=1)
            start2.grid_rowconfigure(0, weight=1)
            start2.configure(background='coral1')
            start2.mainloop()



        QR_code = PhotoImage(file="login.png")
        n1 = Button(frame,text="My QR Code",bg="CadetBlue1",fg="brown4",font=("Times 30 bold underline", 20),command=qr,height=2, width=20)
        n1.grid(row=2, column=0, padx=25, pady=25,columnspan=3)

        ma = Label(frame, text='or', font=("Times 30 bold underline", 25))
        ma.grid(row=3, sticky=NSEW, column=0, columnspan=3)

        n2 = Button(frame,text="Get a E-pass",bg="CadetBlue1",fg="brown4",font=("Times 30 bold underline", 20), command=get_pass, height=2, width=20)
        n2.grid(row=4, column=0, padx=25, pady=25,columnspan=3)

        n3 = Button(frame, text="Logout", fg="RED", command=logout, height=1, width=5)
        n3.grid(row=1, column=3, padx=25, pady=25, columnspan=3)


        #name_box = Entry(frame)
        #name_box.grid( row=0, column=0,sticky=NSEW,padx=10,pady=10)

        #global search_photo
        #search_photo = PhotoImage(file="search.png")

        #def search():
           # s1=name_box.get()
            #with open("books.txt", "r") as file:
              #  fh = csv.reader(file, delimiter=",", lineterminator="\n")
               #    if row[0] == s1:
                #        file.close()
                 #       start.destroy()
                  #      break

        #find_button = Button(frame, text='Search',bg="Yellow",fg="RED",command=search,height = 5, width =50)
        #find_button.grid( row=0, column=1,padx=5,pady=5,columnspan=2)

        start.configure(background='coral1')

    la = Label(lf, text='You have already Registered,Login to continue...',fg='Green',font=("Times 30 bold underline", 15))
    la.grid(row=0, sticky=NSEW, column=1, columnspan=3)

    user = Label(lf, text="User name : ",font=("Times 30 bold underline", 15))
    user.grid(row=1, column=1,sticky=NSEW,padx=10,pady=10)

    passw = Label(lf, text="Password : ",font=("Times 30 bold underline", 15))
    passw.grid(row=2, column=1,sticky=NSEW,padx=10,pady=10)

    u1 = Entry(lf)
    u1.grid(row=1, column=2,sticky=NSEW,padx=10,pady=10)

    p1 = Entry(lf,show="*")
    p1.grid(row=2, column=2,sticky=NSEW,padx=10,pady=10)

    login_photo = PhotoImage(file="login.png")

    log = Button(lf, text="Login", command=check,image = login_photo,height=90,width=215)
    log.grid(row=3, column=3,padx=10,pady=10,columnspan=2)



    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.configure(background='coral1')
    root.mainloop()


win = Tk()      #Constructing login and register window
win.title("E-BUS PASS")
#win.iconbitmap("bus2.ico")

photo = PhotoImage(file = "bus.ico")
win.iconphoto(False, photo)


"""def donothing():
    print("Hiiii!!!!!")

menu=Menu(win)
win.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu= subMenu)
subMenu.add_command(label="Developing...",command= quit() )
subMenu.add_command(label="Developing...",command= quit() )
subMenu.add_separator()
subMenu.add_command(label="Quit",command= quit() )"""

f1=Frame(win)
f1.grid(padx=50,pady=50)

la=Label(f1,text='WELCOME TO E-BUS PASS...!!!',font=("Impact",50))
la.grid(row = 0,sticky = NSEW,column=1,columnspan = 3)


login_photo = PhotoImage(file = "signin.png")
l1 = Button(f1, command=log1,image = login_photo,height = 88, width =180)
l1.grid(row=2,column=2,padx=25,pady=25)

ma=Label(f1,text='or',font=("Times 30 bold underline",25))
ma.grid(row = 3,sticky = NSEW,column=1,columnspan = 3)


register_photo = PhotoImage(file = "signupresize.png")
r1 = Button(f1, command=regiuser,image = register_photo,height = 88, width =180)
r1.grid(row=4,column=2,padx=25,pady=25)

win.grid_columnconfigure(0,weight=1)
win.grid_rowconfigure(0,weight = 1)
win.configure(background='coral1')
win.mainloop()