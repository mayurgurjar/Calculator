from tkinter import *
root = Tk()
root.geometry("600x600")
root.config(bg = "grey")
root.title("mayur's first calculator")
l1 = Label(root , text = "MAYUR FIRST CALCULATOR")
l1.pack()

screen =StringVar()
screen.set("")
screenvalue = Entry(root , textvar = screen  , font = "lucida 40 bold" )
screenvalue.pack(fill= X , ipadx = 15 , pady =10 , padx = 10)
def click(event):
    global screen
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if screen.get().isdigit():
            value = int(screen.get())
        else:
            value = eval(screenvalue.get())
        screen.set(value)
        screen.update()
    elif text =="C":
        screen.set("")
        screen.update("")
    else:
        screen.set(screen.get()+ text)
        screenvalue.update()


f1 = Frame(root, bg = "white" )
b1 = Button(f1 , text= "9" , font = "lucida 35 bold" , bg = "blue" , padx = 20)
b1.pack(side = LEFT ,  padx = 20 , pady = 10)
b1.bind("<Button-1>", click)
b2 = Button(f1 , text= "8" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b2.pack(side = LEFT , padx  = 20 , pady = 10 )
b2.bind("<Button-1> " , click )
b3 = Button(f1 , text= "7" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b3.pack(side = LEFT , padx= 20 , pady = 10  )
b3.bind("<Button-1> ", click)

f1.pack()


f1 = Frame(root, bg = "white" )
b1 = Button(f1 , text= "6" , font = "lucida 35 bold" , bg = "blue" , padx = 20)
b1.pack(side = LEFT ,  padx = 20 , pady = 10)
b1.bind("<Button-1>", click)
b2 = Button(f1 , text= "5" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b2.pack(side = LEFT , padx  = 20 , pady = 10 )
b2.bind("<Button-1> " , click )
b3 = Button(f1 , text= "4" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b3.pack(side = LEFT , padx= 20 , pady = 10  )
b3.bind("<Button-1> ", click)

f1.pack()


f1 = Frame(root, bg = "white" )
b1 = Button(f1 , text= "3" , font = "lucida 35 bold" , bg = "blue" , padx = 20)
b1.pack(side = LEFT ,  padx = 20 , pady = 10)
b1.bind("<Button-1>", click)
b2 = Button(f1 , text= "2" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b2.pack(side = LEFT , padx  = 20 , pady = 10 )
b2.bind("<Button-1> " , click )
b3 = Button(f1 , text= "1" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b3.pack(side = LEFT , padx= 20 , pady = 10  )
b3.bind("<Button-1> ", click)

f1.pack()

f1 = Frame(root, bg = "white" )
b1 = Button(f1 , text= "0" , font = "lucida 35 bold" , bg = "blue" , padx = 20)
b1.pack(side = LEFT ,  padx = 20 , pady = 10)
b1.bind("<Button-1>", click)
b2 = Button(f1 , text= "+" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b2.pack(side = LEFT , padx  = 20 , pady = 10 )
b2.bind("<Button-1> " , click )
b3 = Button(f1 , text= "*" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b3.pack(side = LEFT , padx= 20 , pady = 10  )
b3.bind("<Button-1> ", click)

f1.pack()


f1 = Frame(root, bg = "white" )
b1 = Button(f1 , text= "=" , font = "lucida 35 bold" , bg = "blue" , padx = 20)
b1.pack(side = LEFT ,  padx = 20 , pady = 10)
b1.bind("<Button-1>", click)
b2 = Button(f1 , text= "-" , font = "lucida 35 bold" , bg = "blue" , padx = 20 )
b2.pack(side = LEFT , padx  = 20 , pady = 10 )
b2.bind("<Button-1> " , click )
b3 = Button(f1 , text= "C" , font = "lucida 35 bold" ,borderwidth = 10, bg = "orange" , padx = 20 )
b3.pack(side = LEFT , padx= 20 , pady = 10   )
b3.bind("<Button-1> ", click)


f1.pack()






root.mainloop()