# QR Code
#ขนาดหน้าจอ
from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image

root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root,width=400,height=600)
canvas.pack()

#ชื่อโปรแกรม
app_label = Label(root,text="QRCode Generator",font=('Arial',22,'bold'))
canvas.create_window(200,50,window=app_label)

#ระบุชื่อพร้อมกับลิ้ง -> QRCode
name_label = Label(root,text="QRCode Name :",font=('Arial',12))
canvas.create_window(200,100,window=name_label)

link_label = Label(root,text="URL :",font=('Arial',12))
canvas.create_window(200,200,window=link_label)

#สร้าง Textbox
name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry,width=200,height=25)

link_entry = Entry(root)
canvas.create_window(200,230,window=link_entry,width=200,height=25)

def generate():
    #ดึงข้อมูล link มาสร้าง  QRCode
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name +".png"
    #สร้าง QRCode
    url = pyqrcode.create(link)
    url.png(file_name,scale=5)
    #แสดงภาพ QRCode
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image=image
    canvas.create_window(200,440,window=image_label)

#ปุ่มสร้าง QRCode
btn = Button(text="Generate",command=generate)
canvas.create_window(200,280,window=btn)


root.mainloop()