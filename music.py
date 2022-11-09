import tkinter as tk
import fnmatch
import os
from pygame import mixer
mixer.init()

app = tk.Tk()
app.title("My Python Music Player")
app.geometry("1000x500")
app.config(bg = 'black')

files_path = "G:\\music" # Music Folder
pattern = "*.mp3" # Files Format

# Control Buttons Images
prev_img = tk.PhotoImage(file = "./img/prev_img.png")
next_img = tk.PhotoImage(file = "./img/next_img.png")
play_img = tk.PhotoImage(file = "./img/play_img.png")
pause_img = tk.PhotoImage(file = "./img/pause_img.png")
stop_img = tk.PhotoImage(file = "./img/stop_img.png")

# Player Functions
def select_music():
    if pauseButton["text"] == "Play":
        mixer.music.unpause()
        pauseButton["text"] = "Pause"
    else:
        label.config(text = listBox.get("anchor"))
        mixer.music.load(files_path + '\\' + listBox.get("anchor"))
        mixer.music.play()

def stop_music():
    mixer.music.stop()
    listBox.select_clear('active')

def next_song():
    next_music = listBox.curselection()
    next_music = next_music[0] + 1
    next_music_name = listBox.get(next_music)
    label.config(text = next_music_name)

    mixer.music.load(files_path + '\\' + next_music_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_music)
    listBox.select_set(next_music)

def prev_song():
    prev_music = listBox.curselection()
    prev_music = prev_music[0] - 1
    prev_music_name = listBox.get(prev_music)
    label.config(text = prev_music_name)

    mixer.music.load(files_path + '\\' + prev_music_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_music)
    listBox.select_set(prev_music)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"

    elif pauseButton["text"] == "Play":
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


# List Of Founded Musics In Folder
listBox = tk.Listbox(app, fg = "white", bg = "black", width = 100, font = ('choir', 19))
listBox.pack(padx = 15, pady = 15)

# Label To Show What Music Is Playing
label = tk.Label(app, text = '', bg = "black", fg = "yellow", font = ('choir', 18))
label.pack(pady = 15)


top = tk.Frame(app, bg = "black")
top.pack(padx = 15, pady = 15, anchor = 'center')


prevButton = tk.Button(app, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = prev_song)
prevButton.pack(pady = 15, in_ = top, side = 'left')


stopButton = tk.Button(app, text = "Stop", image = stop_img, bg = 'black', borderwidth = 0, command = stop_music)
stopButton.pack(pady = 15, in_ = top, side = 'left')


playButton = tk.Button(app, text = "Play", image = play_img, bg = 'black', borderwidth = 0, command = select_music)
playButton.pack(pady = 15, in_ = top, side = 'left')


pauseButton = tk.Button(app, text = "Pause", image = pause_img, bg = 'black', borderwidth = 0, command = pause_song)
pauseButton.pack(pady = 15, in_ = top, side = 'left')


nextButton = tk.Button(app, text = "Next", image = next_img, bg = 'black', borderwidth = 0, command = next_song)
nextButton.pack(pady = 15, in_ = top, side = 'left')


# Check The Path For Any MP3 File
# And Write The Names In The List Space
for root, dirs, files in os.walk(files_path):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


app.mainloop()
