
#Arshdeep Singh
#TCSS480
#Assignment 3

#This project prints to the console a bunch of times


from tkinter import *



def make_pop():
    string = entry_1.get()
    print("Hi {}, your name is {} letters long".format(string, len(string)))



root = Tk()


label_1 = Label(root, text="First Name")
entry_1 = Entry(root)

label_1.grid(row=0, sticky=E)
entry_1.grid(row=0, column = 1)


button_1 = Button(root, text= "Give me the length", bg = "black", fg= "red", command=make_pop)
button_1.grid(row=1, columnspan = 2)



root.mainloop()


