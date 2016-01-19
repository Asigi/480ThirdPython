from tkinter import *




def doNothing():
    print("OK I wont")


root = Tk() # constructor that creates a blank window.

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu) #subMenu is within menu
menu.add_cascade(label="File", menu = subMenu) #gives dropdown functionality to File button
subMenu.add_command(label="New Project...", command=doNothing) #this is the item in our submenu.
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="Redo", command=doNothing)














''' #LESSON 1
    
# theLabel = Label(root, text = "This is too easy") # a label is used to put text on screen
# theLabel.pack() # tells python to just put theLabel wherever it can on the root window.
'''

''' #LESSON 2
    
topFrame = Frame(root)
topFrame.pack() #At the top by default, explicitly:

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

#first create the widgets
button1 = Button(topFrame, text = "Button 1", fg = "red") #text color is red BUT not not supported on Mac.
button2 = Button(topFrame, text = "Button 2", fg = "blue")
button3 = Button(topFrame, text = "Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "purple")

#pack in the button widgets
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
'''


''' #LESSON 3
    
one = Label(root, text="ONE", bg = "red", fg = "white")
one.pack()
two = Label(root, text="TWO", bg = "green", fg = "black")
two.pack(fill=X) #causes widget to grow as wide as the parent.
three = Label(root, text="THREE", bg= "blue", fg ="white")
three.pack(side=LEFT, fill = Y) #causes widget to grow as tall as possible, and on the left side.
'''

''' #LESSON 4
    
label_1 = Label(root, text="name")
label_2 = Label(root, text="password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) #by default, the column is 0.
label_2.grid(row=1, sticky=E) #by default, sticky will center-allign you label in its space. E is east.

entry_1.grid(row=0, column = 1)
entry_2.grid(row=1, column = 1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan = 2)
'''


''' #LESSON 5
    
#PART 1:
    
def printName():
    print("Hello, my name is Arsh") # this will be printed to command line/terminal
    
button_1 = Button(root, text="Print my name", command = printName) #calls printName function when clicked.
button_1.pack()

#PART 2:

def printName(event):
    print("Hello, my name is Arsh") # this will be printed to command line/terminal

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName) # <Button-1> is the left mouse button, when its clicked printName is called.
button_1.pack()
'''


''' #Lesson 6
    
def leftClick(event):
    print("left")

def rightClick(event):
    print("right")

def middleClick(event):
    print("middle")

frame = Frame(root, width=300, height=250) #creates a 300 pixel by 250 pixel frame
frame.bind("<Button-1>" , leftClick)
frame.bind("<Button-2>" , middleClick) #Button-2 is the scrollwheel button on Windows, BUT 2-finger click on MacBook Pro
frame.bind("<Button-3>" , rightClick)
frame.pack()
'''


''' #LESSON 7
    
class ArshButtons:
    
    def __init__(self, master): #master is like root
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text="Quit", command= frame.quit)
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
        print("Wow, this actually worked")



root = Tk() # constructor that creates a blank window. NOTE: this is outside of ArshButtons class.
b = ArshButtons(root)
'''


root.mainloop() # This puts the window continuously on the computer screen, so that it doesn't popup and disapear




