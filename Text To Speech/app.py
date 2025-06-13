# Text To Speech
from tkinter import *
from gtts import gTTS

#ขนาดหน้าจอ
root = Tk()
root.title("Text To Speech")
canvas = Canvas(root,width=400,height=300)
canvas.pack()

app_label = Label(root, text="Text To Speech", font=('Arial', 24, 'bold'))  
canvas.create_window(200, 100, window=app_label)

text_entry = Entry(root)
canvas.create_window(200, 150, window=text_entry)

def convert_to_speech():
    word= text_entry.get()
    language = 'th'
    gTTS(text=word, lang=language, slow=False).save("Sound.mp3")
    # print("Converting to speech:", word)

button = Button(root, text="Convert to Speech", command=convert_to_speech)
canvas.create_window(200, 200, window=button)

root.mainloop()