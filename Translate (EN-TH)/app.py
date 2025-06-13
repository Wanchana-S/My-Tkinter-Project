# Translate (EN-TH)

#ขนาดหน้าจอ
from cgitb import text
from tkinter import *
from tkinter import font
from googletrans import Translator

root = Tk()
root.title("Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(700,300)
root.minsize(530,300)

#widget
lable=Label(text="English - Thai",font=('Arial',20,'bold'))
lable.pack()

#เก็บข้อความภาษาอังกฤษ
textEN = Text(root,width=30,height=10)
textEN.place(x=10,y=70)

#เก็บข้อความภาษาไทย
textTH = Text(root,width=30,height=10)
textTH.place(x=275,y=70)

#function
def translate():
    mesg = textEN.get('1.0','end-1c') #ดึงข้อความจาก textEN มาเก็บในตัวแปร
    translator = Translator()
    output = translator.translate(text=mesg,src='en',dest='th')
    textTH.insert('end',output.text)
    print(output.text)

def clear():
    textEN.delete(1.0,'end')
    textTH.delete(1.0,'end')

#ปุ่ม
btnTranslate = Button(root,text=("แปลภาษา"),command=translate,width=10)
btnTranslate.place(x=180,y=250)

btnClear = Button(root,text=("เคลียร์"),command=clear,width=10)
btnClear.place(x=280,y=250)

root.mainloop()