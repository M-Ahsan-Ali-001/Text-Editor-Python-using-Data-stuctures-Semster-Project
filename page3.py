from tkinter import * # IMPORTING HEADER FILE
import tkinter as tk
rt=0
def input(z):#FUNCTION TO UPDATE TEXT AREA

    root = Tk()
    root.title('PYTHON-TEXT-EDITOR')
    # specify size of window.
    root.geometry("900x600")
    rt=root
    def byw(): #FUNCTION INPUT TEXT BY WORDS
        rt.destroy()
        import main_org
        d=main_org.byword(z)

    def bych():#FUNCTION INPUT TEXT BY CHARACTERS
        rt.destroy()
        import main_org
        d=main_org.bychar(z)
    # Create text widget and specify size.
    #IN THE AREA BELOW CREATING BUTTONS, TEXT AREA AND LABEL
    T = Text(root, height=27, width=100)

    # Create label
    l = Label(root, text="DATA to be stored in  DOUBLY LINKED LIST:")
    l.config(font=("Courier", 14))
    l1 = Label(root, text="How do you want to edit?")
    l.config(font=("Courier", 19))

    # Create button for next text.
    b1 = Button(root, text=" BY WORDS ",command=byw  )

    # Create an Exit button.
    b2 = Button(root, text=" BY CHARACTERS ",
                command=bych)

    b3 = Button(root, text=" EXIT ",
                command=root.destroy)

    l.pack()
    T.pack()
    l1.pack()
    b1.pack()
    b2.pack()
    b3.pack()


    # Insert The Fact.
    T.insert(tk.END, z)

    tk.mainloop()

