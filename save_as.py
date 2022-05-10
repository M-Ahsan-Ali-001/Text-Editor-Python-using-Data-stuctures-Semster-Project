import os#IMPORTING HEADER FILES
from tkinter import *
from tkinter import messagebox
rt=0
def func(st):# FUNCIONS TO SEND STRING TO A FILE
 root = Tk()
 root.geometry("500x300")#SEETTING DIMENSIONS
 root.title("  PYTHON-TEXT-EDITOR/INPUT A FILE ")#SETTING TITEL
 rt=root

 def Take_input():#FUNCTIONS TO MAKE A FILE

    INPUT = inputtxt.get("1.0", "end-1c")

    rt.destroy()
    if os.path.exists(INPUT+'.txt') == True:#CHECKING IF file name EXISTS
        messagebox.showinfo("Save as", INPUT + '.txt already exists!')
        import save_as
        save_as.func(st)

    else:#CHECKING FILE NAME DOESNOT EXIST THAN MAKING A NEW FILE
      messagebox.showinfo("Save as", INPUT + '.txt has been saved!')
      fil = open(INPUT + '.txt', 'w')
      fil.write(st)
      fil.close




#CREATING BUTTON , TEXT AREA AND LABEL  BELOW

 l = Label(text='\n\n\n\nPlease Enter a name to save: ')
 inputtxt = Text(root, height=3,
                width=20,
                bg="white")


 Display = Button(root, height=2,
                 width=20,
                 text="Save",
                 command=lambda: Take_input())

 l.pack()
 inputtxt.pack()
 Display.pack()


 mainloop()