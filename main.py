from tkinter import *
import wave
from functools import partial
from tkinter import filedialog
import pyaudio
import pygame


master = Tk()
master.geometry("1000x600")


def import_sound(master):
    global audio
    file_types = [('Wav Files', '*.Wav'), ('Mp3 Files', '*.Mp3')]
    filename_1 = filedialog.askopenfilename(filetypes=file_types)
    audio = filename_1
    print(f"file uploaded:{audio}")

def play_sound(master):
    global audio
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio)
    sound.play()
    pygame.time.wait(int(sound.getlength() * 0.1))





import_sound_btn = Button(master,
    text= "import ",
    height= 5, width = 20,
    command=partial(import_sound, master)
).grid(row=1, column=0)

play = Button(master,
    text="Play",
    height= 5, width= 20,
    command= partial(play_sound, master),
).grid(row=2, column=0)
master.mainloop()