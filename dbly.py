from tkinter import *# HEADER FILES IMPORTING
import tkinter as tk
rt=0
def func(strg):# A FUNCTION TO UPADTE TEXT AREA
 print('dounly ltestst')
 print(strg)

 root  = Tk()
 rt=root
 root.title('PYTHON-TEXT-EDITOR/DOUBLY')#CREATING TITLE
# specify size of window.
 root.geometry("900x1000")#SETTING  DIMENSIONS
 def ins_st():#FUNCTION to INSERT AT BEGINNING

    p=i2.get('1.0','end-1c')
    import main_org
    d=main_org
    d.editor.insert_beg(p)
    vr=d.editor.t_rt()
    t.delete("1.0","end")
    t.insert(tk.END,vr)
    print(d.editor.test_print())
    #rt.destroy()
    #import dbly
    #dbly.func(vr)
 def del_end():#A FUNCTION TO DELETE END ELEMENT FROM MAIN LIST
     import main_org
     d=main_org
     d.editor.del_end()
     vr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, vr)
     print(d.editor.test_print())

     #rt.destroy()
     #import dbly
     #dbly.func(vr)
 def ins_end():#A FUNCTION TO INSERT AT END IN MAIN LIST
     p=i1.get('1.0','end-1c')
     import main_org
     d=main_org
     d.editor.ipt_word(p)
     var=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, var)
     print(d.editor.test_print())

     #rt.destroy()
     #import dbly
     #dbly.func(var)
 def del_frt():# A FUNCTION TO DELETE FRONT FORM MAIN LIST
     import main_org
     d=main_org
     d.editor.del_beg()
     vr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, vr)
     print(d.editor.test_print())

     #rt.destroy()
     #import   dbly
     #dbly.func(vr)
 def undo():#FUNCTION TO CALL UNDO FUNCTION IN MAIN FILE
     import main_org
     d=main_org
     d.editor.undo()
     var=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, var)
     print(d.editor.test_print())
     #rt.destroy()
     #import dbly
     #dbly.func(var)
 def redo():#FUNCTION TO CALL REDO FUNCTION FROM MAIN FILE
     import main_org
     d=main_org
     d.editor.redo()
     vr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, vr)
     print(d.editor.test_print())

     #rt.destroy()
     #import dbly
     #dbly.func(vr)
 def in_arbi():#FUNCTION CALL IN_ARBI FUCTION FROM MAIN FILE
     word=i3.get('1.0','end-1c')
     idx=eval(idx_1.get('1.0','end-1c'))
     import main_org
     d=main_org
     d.editor.insert_arbitary(word,idx,'test')
     vr=d.editor.t_rt()
     t.delete("1.0", "end")
     t.insert(tk.END, vr)
     print(d.editor.test_print())

     #rt.destroy()
     #import dbly
     #dbly.func(vr)
 def del_arbi():#FUNCTION TO CALL DELETE ARBITRARY IN MAIN LIST
   idx=eval(idx_2.get('1.0','end-1c'))
   import main_org
   d=main_org
   d.editor.del_arbitary(idx,'test')
   vr=d.editor.t_rt()
   t.delete("1.0", "end")
   t.insert(tk.END, vr)
   print(d.editor.test_print())

   #rt.destroy()
   #import dbly
   #dbly.func(vr)
 def exit():#FUNCTION TO EXIT
     import main_org
     var=main_org.editor.t_rt()
     rt.destroy()
     import save_as
     save_as.func(var)
# Create text widget and specify size.

# Creating buttons , text area and labels below
 t = Text(root, height=25, width=100,bg='grey')
 l = Label(root, text = "Data in list: ")
 l.config(font =("Courier", 14))
 i1 = Text(root, height=1, width=20)
 i2 = Text(root, height=1, width=20)
 i3 = Text(root, height=1, width=20)
 idx_1= Text(root, height=1, width=20)
 idx_2 = Text(root, height=1, width=20)

 # Create button for next text.


 b1 = Button(root, text = "insert_start",command= ins_st)

# Create an Exit button.
 b2 = Button(root, text = "delete_end",command =  del_end)

 b7 = Button(root, text="insert_end", command=ins_end)

 # Create an Exit button.
 b8 = Button(root, text="delete_front", command=del_frt)

 b3=Button(root, text = "EXIT AND SAVE",command = exit)

 b4=Button(root, text = "   UNDO   ",command = undo)

 b5=Button(root, text = "   REDO   ",command = redo)

 b9 = Button(root, text="   insert at arbitary   ", command=in_arbi)

 # Create an Exit button.
 b10 = Button(root, text="   delete at arbitary   ", command=del_arbi)
 b3.pack()
 l.pack()
 t.pack()
 b1.pack()
 i2.pack()
 b9.pack()
 i3.pack()
 idx_1.pack()
 b10.pack()
 idx_2.pack()
 b7.pack()
 i1.pack()
 b2.pack()
 b8.pack()

 b4.pack()
 b5.pack()
# Insert The Fact.
 t.insert(tk.END, strg)
 idx_1.insert(tk.END,'INDEX')
 idx_2.insert(tk.END,'INDEX')


 tk.mainloop()