from tkinter import *#importing HEADER FILES
import tkinter as tk
rt=0 #GLOBAL VARAIBLE
def func(strg):#FUNCTION TO UPDATE TEXT AREA WHEN AN ADD/DELETE BUTTON IS PRESSED
 print(strg)#TESTING

 root  = Tk()#CREATING A VARIABLE TO MAKE ROOT OF TK()
 rt=root#DOING SO WE CAN DESTROY CURRENTLY OPENED PAGE
 root.title('PYTHON-TEXT-EDITOR/QUE')#MAKING A TITLE
# specify size of window.
 root.geometry("900x650")#SETTING THE DIMENSIONS
 def pg1():#A FUNCTION TO DELETE END WHEN pop button will be pressed
  #rt.destroy()
  import main_org # IMPORTING BACK END FILE
  d= main_org #MAKING VARIABLE TO CALL FUNCTONS OF MAIN FILE
  d.editor.del_end() # CALLING DELETE END FNCTION
  var=d.editor.t_rt()#AFTER DELETING STROING LIST in VAR
  t.delete("1.0", "end")#DELETING PREVIOUSLY WRITTEN DATA
  t.insert(tk.END, var)#UPDATING NEW DATA
  print(d.editor.test_print())#TESTING



 def undoo():#FUNCTION TO CALL UNDO OPERATION IN MAIN FILE
   #rt.destroy()
   import main_org
   d = main_org
   d.editor.undo()
   varr = d.editor.t_rt()
   t.delete("1.0", "end")
   t.insert(tk.END, varr)

   #import stack
   #f = stack.func(varr)

 def redoo():#AFUNCTION TO CALL REDO OPERATION IN MAIN FILE
  # rt.destroy()
   import main_org
   d = main_org
   d.editor.redo()
   varr = d.editor.t_rt()
   t.delete("1.0", "end")
   t.insert(tk.END, varr)

   #import stack
   #f = stack.func(varr)



 def pg2():# FUNCTION TO CALL INSET BEG FROM MAIN FILE
     inputt=i1.get("1.0", "end-1c")
     #rt.destroy()
     import main_org
     d = main_org
     d.editor.insert_beg(inputt)
     var=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, var)

     print(d.editor.test_print())

     #import que
     #que.func(var)


 def exit():# AFUNCTION TO EXIT
     import main_org
     var = main_org.editor.t_rt()
     rt.destroy()
     import save_as
     save_as.func(var)

 # Create text widget and specify size.

# IN THE AREA BELOW WE ARE CREATING LABLE BUTTONS AND TEXT AREAS
 t = Text(root, height=27, width=100,bg='grey')
 l = Label(root, text = "\n Data Stored in List: ")
 l.config(font =("Courier", 14))
 i1=Text(root,height=1,width=20)
# Create button for next text.


 b1 = Button(root, text = "PUSH",command= pg2)

# Create an Exit button.
 b2 = Button(root, text = "POP",command =  pg1)

 b3=Button(root, text = "  EXIT & SAVE  ",command = exit)

 b4=Button(root, text = "UNDO",command = undoo)

 b5=Button(root, text = "REDO",command = redoo)

 l.pack()
 t.pack()
 b1.pack()
 i1.pack()
 b2.pack()
 b3.pack()
 b4.pack()
 b5.pack()

 # Insert The Fact.
 t.insert(tk.END, strg)

 tk.mainloop()