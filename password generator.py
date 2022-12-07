import random
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox

root = tk.Tk()
root.geometry("450x350")
root.title("Password generator")
root.config(bg="black")

def code():
    if var.get()==8:
        code8()
    elif var.get()==12:
        code12()
    elif var.get()==16:
        code16()
    else :
        code20()
        
def code8():
    global A
    code= ""
    A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
         "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
         '1','2','3','4','5','6','7','8','9','0',
         "~","!","@","#","$","%","^","&","*","?","<",">"]
    
    for i in range(8):
        code = code + random.choices(A)[0]
    t1.delete('1.0',END)
    t1.insert(END,code)   

def code12():
    code=""
    for i in range(12):
        code = code + random.choices(A)[0]
    t1.delete('1.0',END)
    t1.insert(END,code)
     
    
def code16():
    code=""
    for i in range(16):
        code = code + random.choices(A)[0]
    t1.delete('1.0',END)
    t1.insert(END,code)
    

def code20():
    code=""
    for i in range(20):
        code = code + random.choices(A)[0]
    t1.delete('1.0',END)
    t1.insert(END,code)
    
    
def exit():
    result = tkMessageBox.askquestion('Do you want to exit ? (y/n)', icon ="warning")
    if result == 'yes':
        root.destroy()    

menubar = Menu(root)
filemenu = Menu(menubar)

var = IntVar()


l1 = Label(root, width = 350,font= ("Comic Sans MS",20), text = "Password Generator",fg="white",bg="black")
l1.pack(side=TOP)

frame = Frame(root,bg="black",width=400,height=100)
frame.pack(pady= 20, padx= 60, fill="both", expand= True)

bottom = Frame(root,bg="black",width =400,height=50)
bottom.pack(pady=20,padx=60, fill="both",expand =True)
bottom1 = Frame(root,bg="black",width =400,height=100)
bottom1.pack(pady=20,padx=60, fill="both",expand =True)

l2 = Label(frame,text = "Select length of Characters :",bg="black",fg="white",font= ("Roboto",10),justify=RIGHT)
l2.pack(side= TOP,pady=10,padx=8)

l3 =Label(frame,text="*Default length is 20",fg="white",bg="black",font=("Roboto",8))
l3.pack(pady=10,padx=8)
    
#Radiobuttons
R1 = Radiobutton(frame,text="8",fg="white",bg="black",variable=var,value=8)
R1.pack(side =LEFT,pady =20, padx= 18)
R2 = Radiobutton(frame,text="12",fg="white",bg="black",variable=var,value=12)
R2.pack(side =LEFT,pady =15, padx= 12)
R3 = Radiobutton(frame,text="16",fg="white",bg="black",variable=var,value=16)
R3.pack(side =LEFT,pady =15, padx= 12)
R4 = Radiobutton(frame,text="20",fg="white",bg="black",variable=var,value=20)
R4.pack(side =LEFT,pady =15, padx= 12)

b1 = Button(bottom,text="Generate",height=2,width=8,relief ="raised",command=code)
b1.pack(side=RIGHT,pady=8,padx=5)

          
t1 = Text(bottom,height=1,width=23)
t1.pack(side = LEFT,pady=0,padx=8)

filemenu.add_command(label = 'Exit',command = exit)
filemenu.add_separator()

menubar.add_cascade(label= "File",menu = filemenu)
root.config(menu=menubar)

if __name__=='__main__':
    root.mainloop()
    