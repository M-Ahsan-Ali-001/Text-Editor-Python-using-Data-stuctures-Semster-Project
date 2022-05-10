from tkinter import *#IMPORTING HEADER FILES
import tkinter as tk
rt=0
def func(strg):#AFUNCTION TO UPDATE TEXT AREA
 print(strg)

 root  = Tk()
 rt=root
 root.title('PYTHON-TEXT-EDITOR')#CREATING TITLE
# specify size of window.
 root.geometry("900x700")#SETTING DIMENSIONS
 def pg1():#FUNCTION TO CALL DELETE END FUNCTIN MAIN FILE
   import main_org
   d=main_org
   d.editor.del_end()
   varr=d.editor.t_rt()
   t.delete("1.0", "end")
   t.insert(tk.END, varr)
   print('\ntestihgg \n')
   d.editor.test_print()
   #rt.destroy()
   #import stack
   #d=stack.func(varr)



 def pg2():#FUNCTION TO CALL insert END FUNCTIN MAIN FILE
     #rt.destroy()
     input=i1.get("1.0", "end-1c")
     print(input)
     import main_org
     d=main_org.editor.test_print()
     import main_org
     obj=main_org
     obj.editor.ipt_word(input)
     var=obj.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, var)


     #rt.destroy()
     #import stack
     #f=stack.func(var)


 def exit():#FUNCTION TO EXIT
     import main_org
     var = main_org.editor.t_rt()
     rt.destroy()
     import save_as
     save_as.func(var)

 def undoo():#FUNCTION TO CALL UNDO OPERATION MAIN FILE
     #rt.destroy()
     import main_org
     d=main_org
     d.editor.undo()
     print('\ntestihgg UNDOOO\n')
     d.editor.test_print()
     varr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, varr)

     #import stack
     #f = stack.func(varr)
 def redoo():#FUNCTION TO CALL REDO FUNCTION FROM MAIN FILE
     #rt.destroy()
     import main_org
     d=main_org
     d.editor.redo()

     print('\ntestihgg UNDOOO\n')
     d.editor.test_print()
     varr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, varr)

     #import stack
    # f = stack.func(varr)

# Create text widget and specify size.

# CREATING BUTTONS,LABEL and TEXT AREA IN THE area BELOW
 t=Text(root,height=27,width=100,bg='grey')
 l = Label(root, text = "\n\n\n Data Stored in List: ")
 l.config(font =("Courier", 14))

# IN THIS AREA AND BELOW CREATING BUTTONS<TEXT AREA AND LABEL
 i1=Text(root,height=1,width=20)

 b1 = Button(root, text = "PUSH",command= pg2)

# Create an Exit button.
 b2 = Button(root, text = "POP",command =  pg1)

 b3=Button(root, text = "   EXIT & SAVE   ",command = exit)

 b4=Button(root, text = "   UNDO    ",command = undoo)

 b5=Button(root, text = "   REDO   ",command = redoo)

 l.pack()
 t.pack()

 b1.pack()
 i1.pack()
 b2.pack()
 b4.pack()
 b5.pack()
 b3.pack()
# Insert The Fact.
 t.insert(tk.END, strg)

 tk.mainloop()