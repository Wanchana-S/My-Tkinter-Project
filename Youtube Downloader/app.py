# Youtube Dowloader
from tkinter import *
from pytubefix import YouTube
from pytubefix.cli import on_progress

#ขนาดหน้าจอ
root = Tk()
root.title("Youtube Dowloader Application")
canvas = Canvas(root,width=400,height=200)
canvas.pack()

#ชื่อโปรแกรม
app_title = Label(root,text="Download in Youtube Video",font=('Arial',18,'bold'))
canvas.create_window(200,30,window=app_title)

#ระบุ link / ปุ่มกดดาวน์โหลด
label = Label(root,text="Link Vedio URL :")
canvas.create_window(200,75,window=label,height=25)
link = Entry(root,width=60)
canvas.create_window(200,100,window=link,height=25)

def download():
    #ดึง URL
    video_path = link.get()
    youtube = YouTube(video_path, on_progress_callback = on_progress)
    mp4 = youtube.streams.get_highest_resolution()
    mp4.download()

download_btn = Button(text="Download",command=download)
canvas.create_window(200,150,window=download_btn)

root.mainloop()