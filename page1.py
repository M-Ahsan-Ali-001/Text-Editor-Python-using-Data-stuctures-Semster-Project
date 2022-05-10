import os# IMPORTING HEADER FILES
from tkinter import *
from tkinter import messagebox





root = Tk()# creating a root  variable for TK()
root.geometry("500x300")#SETTING THE DIMENSIONS OF PAGE
root.title("  PYTHON-TEXT-EDITOR/INPUT A FILE ")#SETTING TITLE OF PAGE


def Take_input():#FUNCTION TO TAKE TEXT FROM TEXT AREA AND NAVIGATION OTHER PAGES

    INPUT = inputtxt.get("1.0", "end-1c")#CREATING A VARAIBLE TO STORE INPUT FEOM TEXT AREA
    import main_org#OPENING BACKEND CODING
    root.destroy()#CLOSING CURRENTLY OPENED PAGE
    INPUT = INPUT + '.txt'#ADDING .txt AT END OF ENTERE NAME FOR CALLING A FILE
    if os.path.exists(INPUT ) == True:#CHECKING IF A FILE EXIST
     d=main_org.file(INPUT)#PASSING FILE NAME TO FUNCTION  file () IN MAIN
    else:#CHECKING IF FILE DOES NOT EXIST THAN PRINT MESSAGE ON SCREEN
        messagebox.showinfo("Save as", INPUT + ' Does not exists!')#PRINT MESSAGE ON SCREEN







l = Label(text='\n\n\n\nPLEASE FIRST PASTE THE FILE INTO PYTHON DIRECTORY!')#CREATING A LABEL
inputtxt = Text(root, height=3,
                width=20,
                bg="white") #CREATING A TEXT AREA


Display = Button(root, height=2,
                 width=20,
                 text="ENTER",
                 command=lambda: Take_input())#CREATING A BUTTON

l.pack()#CALLING FUNCTION TO CREATE LABEL
inputtxt.pack()#CALLING FUNCTION TO CREATE TEXT AREA
Display.pack()#CALLING FUNCTION TO CREATE BUTTON


mainloop()#CLOSING TKINTER