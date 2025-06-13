#Calculator
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("เครื่องคิดเลข")

content = ""
txt_input = StringVar(value=0)

# 7 + 10
def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

#แสดงผล 5 x 4
display = Entry(font=('arial',30,'bold'),fg="black",bg="light gray",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#รับค่าผ่านปุ่ม

#row1
btn7 = Button(fg="black",font=('arial',22,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(fg="black",font=('arial',22,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(fg="black",font=('arial',22,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnc = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="C",command=clear,padx=30,pady=15).grid(row=1,column=3)

#row2
btn4 = Button(fg="black",font=('arial',22,'bold'),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',22,'bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',22,'bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
btnplus = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="+",command=lambda:btn("+"),padx=30,pady=15).grid(row=2,column=3)

#row3
btn1 = Button(fg="black",font=('arial',22,'bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(fg="black",font=('arial',22,'bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(fg="black",font=('arial',22,'bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
btnminus = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="-",command=lambda:btn("-"),padx=30,pady=15).grid(row=3,column=3)

#row4
btn0 = Button(fg="black",font=('arial',22,'bold'),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=0)
btndot = Button(fg="black",font=('arial',22,'bold'),text=".",command=lambda:btn("."),padx=30,pady=15).grid(row=4,column=1)
btndivision = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="÷",command=lambda:btn("/"),padx=30,pady=15).grid(row=4,column=2)
btnmultiply = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="x",command=lambda:btn("*"),padx=30,pady=15).grid(row=4,column=3)

#row5
btnopen = Button(fg="black",bg="orange",font=('arial',22,'bold'),text="(",command=lambda:btn("("),padx=30,pady=15).grid(row=5,column=0)
btnclose = Button(fg="black",bg="orange",font=('arial',22,'bold'),text=")",command=lambda:btn(")"),padx=30,pady=15).grid(row=5,column=1)
btnequal = Button(fg="black",bg="light blue",font=('arial',22,'bold'),text="=",command=equal,padx=90,pady=15).grid(row=5,column=2,columnspan=2)



root.mainloop()