from tkinter import * 
root = Tk()
root.title("โปรแกรมคำนวณพื้นที่วงกลม")
root.geometry("400x100")

# พื้นที่วงกลม πr² โดยให้ค่า π มีค่า 3.14
Label(text="รัศมี",font=22).grid(row=0,sticky=W)
radius = IntVar()
et = Entry(width=30,textvariable = radius,font=22)
et.grid(row=0,column=1)

Label(text="พื้นที่วงกลม",font=22).grid(row=1,sticky=W)
et2 = Entry(width=30,font=22)
et2.grid(row=1,column=1)

def cal():
    et2.delete(0,END)
    r = radius.get()
    area = 3.14 * r * r
    et2.insert(0,area)

def clear():
    et.delete(0,END)
    et2.delete(0,END)

btn1 = Button(text="คำนวณ",command=cal).grid(row=2,column=1,sticky=W)
btn2 = Button(text="ล้างข้อมูล",command=clear).grid(row=2,column=1,sticky=E)

root.mainloop()