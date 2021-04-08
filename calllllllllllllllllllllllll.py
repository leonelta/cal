from tkinter import*

cal = Tk()
cal.title("calculator")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal,font=('arail', 20, 'bold') ,textvariable=text_input , bd=30, insertwidth=4,
                              bg="powder blue", justify='right').grid(columnspan=4)

ubtn7 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "7", bg="powder blue").grid(row = 1, column = 0)

btn8 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "8", bg="powder blue").grid(row = 1, column = 1)

btn9 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "9", bg="powder blue").grid(row = 1, column = 2)

Addition =  Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "+", bg="powder blue").grid(row = 1, column = 3)

btn7 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "7", bg="powder blue").grid(row = 1, column = 0)

btn8 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "8", bg="powder blue").grid(row = 1, column = 1)

btn9 = Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "9", bg="powder blue").grid(row = 1, column = 2)

Addition =  Button(cal, padx = 16, bd = 8, fg = "black", font=('arail', 20, 'bold'),
              text= "+", bg="powder blue").grid(row = 1, column = 3)

cal.mainloop()
