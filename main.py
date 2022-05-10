from tkinter import * # IMPORTING HEADER FILES
import tkinter as tk
import os


root  = Tk()# creating a root  variable for TK()


root.title('PYTHON-TEXT-EDITOR')#SETTING TITLE OF PAGE
# specify size of window.
root.geometry("500x300")#SETTING THE DIMENSIONS OF PAGE

# Create text widget and specify size.

# Create label
l = Label(root, text = "\n\n\nPYTHON TEXT EDITOR")#SETTING A LABEL FOR PAGE
l.config(font =("Courier", 14))# SELECTING FONT FOR THE LABEL

# Create button for next text.
def pg1():#A FUNCTION TO INPUT A FILE NAME
	root.destroy()# CLOSING THE CURRENT PAGE
	import page1 #OPENING PAGE 1
def pg2():#A FUNCTION TO INPUT A STRING
	root.destroy() # CLOSING THE CURRENT PAGE
	import page2 #OPENING PAGE 1
def exit():#A FUNCTION TO EXIT
	root.destroy() # HELPS IN EXITING



b1 = Button(root, text = "INPUT AS A FILE",command= pg1 ) # Create an button to input file.


b2 = Button(root, text = "INPUT AS STRING",command =  pg2) # Create an button to input string.

b3=Button(root, text = "EXIT",command = exit) # Create an Exit button.


l.pack()#CALIING FUNCTION TO CREATE LABEL
b1.pack()#CALIING FUNCTION TO CREATE BUTTON
b2.pack()#CALIING FUNCTION TO CREATE BUTTON
b3.pack()#CALIING FUNCTION TO CREATE BUTTON


tk.mainloop() #CLOSING TKINTER
