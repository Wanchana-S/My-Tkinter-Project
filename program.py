from tkinter import * 
from tkinter.colorchooser import *
from tkinter.filedialog import *
from tkinter import ttk
import tkinter.messagebox


#หน้าจอที่ 1 TEST
root = Tk()
root.title("My GUI")
#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x500")



# def showMessage1():
#     msg = txt.get()
#     Label(root,text=msg,fg="white",bg="green").pack()

# def showMessage2():
#     Label(root,text="ยกเลิกแล้ว !",fg="white",bg="red").pack()

# def openWindow():
#     #หน้าจอที่ 2
#     myWindow = Tk()
#     myWindow.title("รายงานการทำงาน")
#     #กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
#     myWindow.geometry("800x400+600+300")

# def openMenuFile1():
#     #หน้าจอที่ 2
#     myMenuFile = Tk()
#     myMenuFile.title("New File")
#     #กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
#     myMenuFile.geometry("800x400+600+300")

# def showAbout():
#     tkinter.messagebox.showinfo("About","Wanchan Saelue")

# def showExit():
#     confirm = tkinter.messagebox.askokcancel("Exit","คุณต้องการปิดโปรแกรมหรือไม่ ?")
#     if confirm == True:
#         root.destroy()

# def selectFile():
#     fileOpen = askopenfilename()
#     # warpper = io.TextIOWrapper(fileOpen,encoding="utf8")
#     fileContent = open(fileOpen,encoding="utf8")
#     myLabelFile = Label(root,text=fileContent.read()).pack()

# def selectColor():
#     color = askcolor()
#     myLableColor = Label(root,text="Color Python",fg="black",bg=color[1]).pack()

# def showChoice():
#     choice = language.get()
#     if choice == 1:
#         tkinter.messagebox.showinfo("แจ้งเตือน","Python")
#     elif choice == 2:
#         tkinter.messagebox.showinfo("แจ้งเตือน","Java")
#     elif choice == 3:
#         tkinter.messagebox.showinfo("แจ้งเตือน","PHP")
#     else:
#         tkinter.messagebox.showinfo("แจ้งเตือน","C#")
#     print(choice)

# def showCheck():
#     choice1 = language1.get()
#     choice2 = language2.get()
#     choice3 = language3.get()
#     choice4 = language4.get()

#     if choice1 == 1:
#         Label(text="Python").pack(anchor=W)
#     if choice2 == 1:
#         Label(text="Java").pack(anchor=W)
#     if choice3 == 1:
#         Label(text="PHP").pack(anchor=W)
#     if choice4 == 1:
#         Label(text="C#").pack(anchor=W)
    
#     print(language1.get(),language2.get(),language3.get(),language4.get())
    

# btnColor = Button(text="เลือกสี",command=selectColor).pack()

# #สร้างเมนู
# myMenu = Menu()
# root.config(menu=myMenu)

# #เพิ่มเมนูย่อย (Menu Item)
# menuItem = Menu()
# menuItem.add_command(label="New File",command=openMenuFile1)
# menuItem.add_command(label="Open File",command=selectFile)
# menuItem.add_command(label="Save File")
# menuItem.add_command(label="About",command=showAbout)
# menuItem.add_command(label="Exit",command=showExit)

# #เพิ่มเมนูหลัก
# myMenu.add_cascade(label="File",menu=menuItem)
# myMenu.add_cascade(label="Edit")
# myMenu.add_cascade(label="View")
# myMenu.add_cascade(label="Help")

# #ใส่ Label บนหน้าจอ

# myLable1 = Label(root,text="Hello World",fg="red",font=20,bg="yellow").pack()

# #กล่องข้อความ
# txt=StringVar()
# myText = Entry(root,textvariable=txt).pack()

# #ใส่ปุ่ม
# btn1 = Button(root,text="บันทึก",fg="white",bg="green",width=5,command=showMessage1).pack()
# btn1 = Button(root,text="เปิดรายงาน",fg="white",bg="red",command=openWindow).pack()
# btn1 = Button(root,text="เลือกไฟล์",fg="white",bg="red",command=selectFile).pack()

# language = IntVar()
# language1 = IntVar()
# language2 = IntVar()
# language3 = IntVar()
# language4 = IntVar()
# language.set(2)

# Radiobutton(root,text="Python",variable=language,value=1,command=showChoice).pack()
# Radiobutton(root,text="Java",variable=language,value=2,command=showChoice).pack()
# Radiobutton(root,text="PHP",variable=language,value=3,command=showChoice).pack()
# Radiobutton(root,text="C#",variable=language,value=4,command=showChoice).pack()

# Checkbutton(root,text="Python",variable=language1).pack(anchor=W)
# Checkbutton(root,text="Java",variable=language2).pack(anchor=W)
# Checkbutton(root,text="PHP",variable=language3).pack(anchor=W)
# Checkbutton(root,text="C#",variable=language4).pack(anchor=W)
# Button(text="แสดง",command=showCheck).pack(anchor=W)

# Label(text="Name").grid(row=0)
# Label(text="Surname").grid(row=1)
# Label(text="Phone").grid(row=2)

# et1 = Entry()
# et1.grid(row=0,column=1)
# et1.insert(0,"Wanchana")

# et2 = Entry()
# et2.grid(row=1,column=1)
# et2.insert(0,"Saelue")

# et3 = Entry()
# et3.grid(row=2,column=1)
# et3.insert(0,"09x-xxx-xxxx")

# def delete():
#     et1.delete(0,END)
#     et2.delete(0,END)
#     et3.delete(0,END)

# Button(text="ลบข้อมูล",command=delete).grid(row=3,column=1)

Label(text="Address",font=20).grid(row=0,column=0)
choice = StringVar(value="เลือกจังหวัดของคุณ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("กรุงเทพ","เชียงใหม่","กระบี่","ภูเก็ต","ชลบุรี")
combo.grid(row=0,column=1)

def selectCity():
    Label(text="คุณเลือก "+choice.get(),font=20).grid(row=2,column=1)

btn=Button(text="ส่งข้อมูล",command=selectCity)
btn.grid(row=1,column=1)

root.mainloop()