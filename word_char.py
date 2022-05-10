from tkinter import *#IMPORTING HEADER FILES
import tkinter as tk
rt=0
def func(strg):#FUNCTION TO UPDATE TEXT AREA
 print(strg)

 root  = Tk()
 rt=root
 root.title('PYTHON-TEXT-EDITOR')#CREATING TITLE
# specify size of window.
 root.geometry("600x300")#SETTING DIMENSIONS
 def pg1(): # FUNCTION TO EDIT BY WORDS
  rt.destroy()
  import main_org
  d= main_org.bychar(strg)



 def pg2():# FUNCTION TO EDIT BY CHARACTERS
     rt.destroy()
     import main_org
     d = main_org.byword(strg)
     root.destroy()


 def exit():#FUNCTION TO EXIT
 	root.destroy()

# Create text widget and specify size.

# Creating Buttons ,text area and label in area below
 l = Label(root, text = "\n\n\n Do you want to edit by characters or by words? ")
 l.config(font =("Courier", 14))

# Create button for next text.


 b1 = Button(root, text = "BY WORDS",command= pg2)

# Create an Exit button.
 b2 = Button(root, text = "BY CHARACTERS",command =  pg1)

 b3=Button(root, text = "EXIT",command = exit)


 l.pack()
 b1.pack()
 b2.pack()
 b3.pack()
# Insert The Fact.
#T.insert(tk.END, Fact)

 tk.mainloop()