# 1 บาทไทย = 0.026 EUR (ยูโร)
# 1 บาทไทย = 3.486 JPY (เยน)
# 1 บาทไทย = 0.031 USD (ดอลล่า)
# 1 บาทไทย = 0.023 GBP (ปอนด์)

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

#Input
money = IntVar()
Label(text="จำนวนเงิน (THB)",padx=10,font=22).grid(row=0,sticky=W)
et1 = Entry(font=22,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกุลเงิน",padx=10,font=22).grid(row=1,sticky=W)
combo = ttk.Combobox(font=22,width=30,textvariable=choice)
combo["values"] = ("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#Output
Label(text="ผลการคำนวณ",padx=10,font=22).grid(row=2,sticky=W)
et2 = Entry(font=22,width=30)
et2.grid(row=2,column=1)

def calculate():
    amount = money.get()
    currency = choice.get()
    et2.delete(0,END)
    if currency == "EUR":
        result = ((amount * 0.026),"EUR(ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        result = ((amount * 3.486),"JPY(เยน)")
        et2.insert(0,result)
    elif currency == "USD":
        result = ((amount * 0.031),"USD(ดอลล่า)")
        et2.insert(0,result)
    elif currency == "GBP":
        result = ((amount * 0.023),"GBP(ปอนด์)")
        et2.insert(0,result)
    else:
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)
    # print(money.get(),choice.get())

def clear():
    et1.delete(0,END)
    et2.delete(0,END)

Button(text="คำนวณ",font=22,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้าง",font=22,width=15,command=clear).grid(row=3,column=1,sticky=E)

root.mainloop()