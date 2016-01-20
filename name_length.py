
#Arshdeep Singh
#TCSS480
#Assignment 3

#Originally this project was supposed to count the letters in the person's name and then create that many pop-ups. Essentially it is supposed to annoy people with really long names because they have to sit there and close all of the newly opened windows.
#After realizing that this program can crashes my computer, I've decided to just print the size of the name.


from tkinter import *



def make_pop():
    string = entry_1.get()
    print("Hi {}, your name is {} letters long".format(string, len(string)))

    root2 = Tk()
    label2 = Label(root2, text = "Your first name is {} characters long".format(len(string)))
    label2.pack()
    root2.mainloop()







root = Tk()


label_1 = Label(root, text="First Name")
entry_1 = Entry(root)

label_1.grid(row=0, sticky=E)
entry_1.grid(row=0, column = 1)


button_1 = Button(root, text= "Give me the length", bg = "black", fg= "red", command=make_pop)
button_1.grid(row=1, columnspan = 2)



root.mainloop()


