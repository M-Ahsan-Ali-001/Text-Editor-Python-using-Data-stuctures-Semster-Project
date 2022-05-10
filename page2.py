from tkinter import * # IMPORTING HEADER FILES




root = Tk()# creating a root  variable for TK()
root.geometry("900x600")#SETTING THE DIMENSIONS OF PAGE
root.title(" PYTHON-TEXT-EDITOR/ENTER A STRING ")#SETTING TITLE OF PAGE
def Take_input():#A FUNCTION FOR BUTTON ENTERY
    INPUT = inputtxt.get("1.0", "end-1c")#Storing the entered string in Text area to INPUT
    root.destroy()#CLOSING THE CURRENT OPENED PAGE
    #print(INPUT)
    import page3#OPENING THE NEXT PAGE
    d=page3
    d.input(INPUT)#CALLING THE FUNCTION IN HEADER FILE page3


l = Label(text='\n\n\n\nENTER YOUR PARAGRAPH HERE:')# CREATING A LABEL
inputtxt = Text(root, height=27,#CREATING A TEXT AREA AND SELECTING COLOR AND WIDTH
                width=100,
                bg="white")


Display = Button(root, height=2,#CREATING A BUTTON
                 width=20,
                 text="ENTER",
                 command=lambda: Take_input())#SETTING COLOR , WIDTH, AND BUTTON RECIVER

l.pack()#CALLING FUNCTION TO CREATE LABEL
inputtxt.pack()#CALLING FUNCTION TO CREATE TEXT AREA
Display.pack()#CALLING FUNCTION TO CREATE BUTTON
mainloop()#CLOSING TKINTER