import tkinter as tk  # Import tkinter module and alias tk
from tkinter import *
from tkinter import filedialog
import os
from compress import compress_video

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Video files","*.mp4*"),("all files","*.*")))
    text_entry.insert(1,filename)

def radioRefresh():
    print(limit_file_size.get())

wind = tk.Tk()  # Establishing top level control wind
wind.geometry("500x200")  # Set window size
wind.title("Video transcoding")  # Set window title
frame = Frame(wind)
# Create pane title, content, font, color
title_lab = tk.Label(wind, text="Video transcoding", font="Arial 16 bold",width=14)
result_lab = tk.Label(wind, text="", font="Arial 16 bold",width=18)
textlab = tk.Label(wind, text="Fichier source", font="Arial 14 bold",fg="blue", width=12)  # Create a form name, and set the font, color, and size
button_explore = tk.Button(wind,text = "Browse Files",command = browseFiles)
# Create the input control entry, that is, the form
text_entry = tk.Entry(wind, width=15, font="Arial 14 bold")

limit_file_size = IntVar()
R1 = tk.Radiobutton(frame, text="8MB", variable=limit_file_size, value=8000,command=radioRefresh)
R2 = tk.Radiobutton(frame, text="50MB", variable=limit_file_size, value=50000,command=radioRefresh)
R3 = tk.Radiobutton(frame, text="100MB", variable=limit_file_size, value=100000,command=radioRefresh)
R1.invoke()

def compress():
    r = compress_video(text_entry.get(), limit_file_size.get())
    if r != Exception:
        result_lab.config(text="Done !")
    else:
        result_lab.config(text=str(r))


# Set the submit button, and set the font style and size
btn = tk.Button(wind, text="Go !",font="Arial 14 bold", fg="blue", width=8,command=compress)


title_lab.grid(column = 2, row = 1)  # Set title position
textlab.grid(column = 1, row = 5)  # Set form name location
button_explore.grid(column = 3, row = 5)  # Set button position
text_entry.grid(column = 2, row = 5)  # Set control location

frame.grid(column = 2, row = 8)
R1.pack(side= LEFT)  # Set control location
R2.pack(side= LEFT)  # Set control location
R3.pack(side= LEFT)  # Set control location

btn.grid(column = 2, row = 9)  # Set button position
result_lab.grid(column = 2, row = 10)  # Set control location

wind.mainloop()  # Message loop of windows