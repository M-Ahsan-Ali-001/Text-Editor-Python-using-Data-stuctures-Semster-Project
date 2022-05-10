from tkinter import *#IMPORTING HEADER FILES
import tkinter as tk
rt=0
def func(strg):#FUNCTIONS TO UPDATE TEXT AREA
 print('ddl-sletion++++')
 print(strg)

 root  = Tk()
 rt=root
 root.title('PYTHON-TEXT-EDITOR')
# specify size of window.
 root.geometry("600x300")#SETTING DIMESIONS
 def pg1():#FUNCTION TO OPEN STACK HEADER FILE
  rt.destroy()
  import stack
  d= stack.func(strg)

 def pg2():#FUNCTION TO OPEN QUE HEADER FILE
   rt.destroy()
   import que
   d = que.func(strg)

 def dd(): # FUNCTIONS TO OPEN DBLY (DOUBLY LINKED LIST)HEADER FILE
   rt.destroy()
   import dbly
   dbly.func(strg)

 def exit():#FUNCTION TO EXIT
 	root.destroy()

# Create text widget and specify size.

# Creating buttons , text area and labels below
 l = Label(root, text = "\n\n\n Do you want to edit by characters or by words? ")
 l.config(font =("Courier", 14))

# Create button for next text.


 b1 = Button(root, text = 'STACK',command= pg1)

# Create an Exit button.
 b2 = Button(root, text = "QUEUE",command =  pg2)


 # Create an Exit button.

 b3=Button(root, text = "EXIT",command = exit)
 b4=Button(root, text = "DOUBLLY LLT",command = dd)


 l.pack()
 b1.pack()
 b2.pack()
 b4.pack()
 b3.pack()
# Insert The Fact.
#T.insert(tk.END, Fact)

 tk.mainloop()