from tkinter import *
window=Tk()
window.title('Simple Calculator')
display=Entry(window,width=11,bg='#242424',font=("Calibri",42),justify="right",fg='white')

display.grid(row=0,column=0,rowspan=2,columnspan=4)
# display_label=Label(window,width=45,height=7,bg='#242424')
# display_label.grid(row=0,column=0,rowspan=2,columnspan=4)

myicon=PhotoImage(file='Calculator GUI\calc_icon.png')
window.iconphoto(False,myicon)

def insert_num(num):
    current=display.get()
    display.delete(0,END)
    display.insert(0,str(current)+str(num))

def clear():
    display.delete(0,END)

def add():
    first=display.get()
    global fnum
    global operation
    operation='addition'
    fnum=int(first)
    display.delete(0,END)

def sub():
    first=display.get()
    global fnum
    global operation
    operation='subtraction'
    fnum=int(first)
    display.delete(0,END)

def mult():
    first=display.get()
    global fnum
    global operation
    operation='multiplication'
    fnum=int(first)
    display.delete(0,END)

def div():
    first=display.get()
    global fnum
    global operation
    operation='division'
    fnum=int(first)
    display.delete(0,END)

def equal():
    new_num=display.get()
    display.delete(0,END)
    if operation=='addition':
        display.insert(0,fnum+int(new_num))
    if operation=='subtraction':
        display.insert(0,fnum-int(new_num))
    if operation=='multiplication':
        display.insert(0,fnum*int(new_num))
    if operation=='division':
        display.insert(0,fnum/int(new_num))


#Defining Button
button_1=Button(window,text='1',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(1)) 
button_2=Button(window,text='2',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(2))
button_3=Button(window,text='3',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(3))
button_4=Button(window,text='4',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(4))
button_5=Button(window,text='5',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(5))
button_6=Button(window,text='6',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(6))
button_7=Button(window,text='7',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(7))
button_8=Button(window,text='8',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(8))
button_9=Button(window,text='9',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(9))
button_0=Button(window,text='0',width=10,height=3,bg='#070707',fg='white',command=lambda:insert_num(0))
button_add=Button(window,text='+',width=10,height=3,bg='#161616',fg='white',command=add)
button_sub=Button(window,text='-',width=10,height=3,bg='#161616',fg='white',command=sub)
button_mult=Button(window,text='X',width=10,height=3,bg='#161616',fg='white',command=mult)
button_div=Button(window,text='/',width=10,height=3,bg='#161616',fg='white',command=div)
button_equal=Button(window,text='=',width=10,height=3,bg='#15456b',fg='white',command=equal)
button_pos_neg=Button(window,text='+/-',width=10,height=3,bg='#070707',fg='white')
button_dot=Button(window,text='.',width=10,height=3,bg='#070707',fg='white')
button_per=Button(window,text='%',width=10,height=3,bg='#161616',fg='white')
button_clear1=Button(window,text='CE',width=10,height=3,bg='#161616',fg='white')
button_clear2=Button(window,text='C',width=10,height=3,bg='#161616',fg='white',command=clear)
button_back=Button(window,text='<]',width=10,height=3,bg='#161616',fg='white')
button_onebyx=Button(window,text='1/x',width=10,height=3,bg='#161616',fg='white')
button_sq=Button(window,text='x^2',width=10,height=3,bg='#161616',fg='white')
button_sqrt=Button(window,text='x^1/2',width=10,height=3,bg='#161616',fg='white')

#Positioning
button_1.grid(row=6 , column=0)
button_2.grid(row=6 , column=1)
button_3.grid(row=6 , column=2)
button_4.grid(row=5 , column=0)
button_5.grid(row=5 , column=1)
button_6.grid(row=5 , column=2)
button_7.grid(row=4 , column=0)
button_8.grid(row=4 , column=1)
button_9.grid(row=4 , column=2)
button_0.grid(row=7 , column=1)
button_add.grid(row=6 , column=3)
button_sub.grid(row=5 , column=3)
button_mult.grid(row=4 , column=3)
button_div.grid(row=3 , column=3)
button_equal.grid(row=7 , column=3)
button_pos_neg.grid(row=7 , column=0)
button_dot.grid(row=7 , column=2)
button_per.grid(row=2 , column=0)
button_clear1.grid(row=2 , column=1)
button_clear2.grid(row=2 , column=2)
button_back.grid(row=2 , column=3)
button_onebyx.grid(row=3 , column=0)
button_sq.grid(row=3 , column=1)
button_sqrt.grid(row=3 , column=2)

window.mainloop()