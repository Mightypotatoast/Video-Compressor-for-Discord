import tkinter as tk  # Import tkinter module and alias tk
from tkinter import *
from tkinter import filedialog
import os
from compress import compress_video


def compress():
    r = compress_video(
        text_entry.get(), limit_file_size.get(), frame_rate.get(), Npass.get()
    )
    if r == True:
        result_lab.config(text="Done !")
    else:
        result_lab.config(text='Error')


def browseFiles():

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Video files", "*.mp4*"), ("all files", "*.*"))
    )
    text_entry.delete(0, len(text_entry.get()))
    text_entry.insert(0, filename)


def RadioRefreshFileSize():
    print(limit_file_size.get())


def RadioRefreshFrameRate():
    print(frame_rate.get())


def RadioRefreshPass():
    print(Npass)


wind = tk.Tk()  # Establishing top level control wind
wind.geometry("250x200")  # Set window size
wind.title("Video transcoding")  # Set window title

# Create pane title, content, font, color
title_lab = tk.Label(wind, text="Video transcoding",
                     font="Arial 16 bold", width=14)
result_lab = tk.Label(wind, text="", font="Arial 16 bold", width=18)

# create a frame containing an Entry and the button to explore files
frame2 = Frame(wind)
text_entry = tk.Entry(frame2, width=15, font="Arial 12 bold")
button_explore = tk.Button(frame2, text="Source file", command=browseFiles)

# create a frame containing 3 radio button for different file size
frame = Frame(wind)
limit_file_size = IntVar()
R1 = tk.Radiobutton(frame, text="8MB", variable=limit_file_size,
                    value=8000, command=RadioRefreshFileSize)
R2 = tk.Radiobutton(frame, text="50MB", variable=limit_file_size,
                    value=50000, command=RadioRefreshFileSize)
R3 = tk.Radiobutton(frame, text="100MB", variable=limit_file_size,
                    value=100000, command=RadioRefreshFileSize)
R1.invoke()  # R1 is selectionned by default

# create a frame containing 2 radio button for different frame rate
frame3 = Frame(wind)
frame_rate = IntVar()
R_fps30 = tk.Radiobutton(frame3, text="30fps", variable=frame_rate,
                         value=30, command=RadioRefreshFrameRate)
R_fps60 = tk.Radiobutton(frame3, text="60fps", variable=frame_rate,
                         value=60, command=RadioRefreshFrameRate)
R_fps30.invoke()

# create a frame containing 2 radio button for different number of passage
frame4 = Frame(wind)
Npass = BooleanVar()
R_2pass = tk.Radiobutton(frame4, text="Slow", variable=Npass,
                         value=True, command=RadioRefreshPass)
R_1pass = tk.Radiobutton(frame4, text="Fast", variable=Npass,
                         value=False, command=RadioRefreshPass)

R_1pass.invoke()  # R_1pass is selectionned by default

# Set the submit button, and set the font style and size
btn = tk.Button(wind, text="Go !", font="Arial 14 bold",
                fg="blue", width=8, command=compress)


title_lab.grid(column=2, row=1)  # Set title position

frame2.grid(column=2, row=5)
text_entry.pack(side=LEFT)  # Set control location
button_explore.pack(side=LEFT)  # Set button position

frame.grid(column=2, row=8)
R1.pack(side=LEFT)  # Set control location
R2.pack(side=LEFT)  # Set control location
R3.pack(side=LEFT)  # Set control location

frame3.grid(column=2, row=9)
R_fps30.pack(side=LEFT)  # Set control location
R_fps60.pack(side=LEFT)  # Set control location

frame4.grid(column=2, row=10)
R_1pass.pack(side=LEFT)  # Set control location
R_2pass.pack(side=LEFT)  # Set control location

btn.grid(column=2, row=11)  # Set button position
result_lab.grid(column=2, row=12)  # Set control location

wind.mainloop()  # Message loop of windows
