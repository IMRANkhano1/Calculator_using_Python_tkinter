#import tkinter
from tkinter import *
#create gui window
root=Tk()
#add title for window
root.title("calculator")
#give size
root.geometry("350x350")

def press(n):
    global st
    if n=="C":
        e.delete(0,END)
    elif n=="=":
        e.delete(0,END)
        e.insert(0,eval(st))
    else:
      st=e.get()
      st=st+str(n)
      e.delete(0,END)
      e.insert(0,st)

#add widgets
e=Entry(root,width=55,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,pady=20)

b=Button(root,text='1',width=8,command=lambda:press(1))
b.grid(row=1,column=0,sticky='w',padx=5,pady=20)

b1=Button(root,text='2',width=8,command=lambda:press(2))
b1.grid(row=1,column=1,sticky='w',padx=5,pady=20)
b2=Button(root,text='3',width=8,command=lambda:press(3))
b2.grid(row=1,column=2,sticky='w',pady=20)
b3=Button(root,text='+',font=('arial',10,'bold'),width=7,command=lambda:press('+'))
b3.grid(row=1,column=3,sticky='w',padx=15,pady=20)

#
b4=Button(root,text='4',width=8,command=lambda:press(4))
b4.grid(row=2,column=0,sticky='w',padx=5,pady=20)

b5=Button(root,text='5',width=8,command=lambda:press(5))
b5.grid(row=2,column=1,sticky='w',padx=5,pady=20)
b6=Button(root,text='6',width=8,command=lambda:press(6))
b6.grid(row=2,column=2,sticky='w',padx=5,pady=20)
b7=Button(root,text="-",font=('arial',10,'bold'),width=7,command=lambda:press('-'))
b7.grid(row=2,column=3,sticky='w',padx=15,pady=20)

#
b8=Button(root,text='7',width=8,command=lambda:press(7))
b8.grid(row=3,column=0,sticky='w',pady=20,padx=5)

b9=Button(root,text='8',width=8,command=lambda:press(8))
b9.grid(row=3,column=1,sticky='w',padx=5,pady=20)
b10=Button(root,text='9',width=8,command=lambda:press(9))
b10.grid(row=3,column=2,sticky='w',padx=5,pady=20)
b11=Button(root,text="*",font=('arial',10,'bold'),width=7,command=lambda:press('*'))
b11.grid(row=3,column=3,sticky='w',padx=15,pady=10)

#
b8=Button(root,text='0',width=8,command=lambda:press(0))
b8.grid(row=4,column=0,sticky='w',pady=20,padx=5)

b9=Button(root,text='C',font=('arial',10,'bold'),width=7,command=lambda:press('C'))
b9.grid(row=4,column=1,sticky='w',padx=5,pady=20)
b10=Button(root,text='=',font=('arial',10,'bold'),width=7,command=lambda:press('='))
b10.grid(row=4,column=2,sticky='w',padx=5,pady=20)
b11=Button(root,text="/",font=('arial',10,'bold'),width=7,command=lambda:press('/'))
b11.grid(row=4,column=3,sticky='w',padx=15,pady=10)

root.mainloop()