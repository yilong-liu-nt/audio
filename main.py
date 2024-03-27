from tkinter import * 
import wave
import numpy as np
import struct
from functools import partial
from tkinter import filedialog
import pyaudio
import pygame
import threading
import time
from player import SamplePlayer
from pydub import AudioSegment
from recorder import *


global audio
global ampl_value

master = Tk()
ampl_value = StringVar()
master.geometry("1000x600")
def enhance_volume(master):
    global audio
    global ampl_value

    song = AudioSegment.from_wav(audio)

    # reduce volume by 10 dB
    song = song + int(ampl_value.get())


    # save the output
    song.export(audio, "wav")


def import_sound(master):
    global audio
    file_types = [('Wav Files', '*.Wav'), ('Mp3 Files', '*.Mp3')]
    filename_1 = filedialog.askopenfilename(filetypes=file_types)
    audio = filename_1
    print(f"file uploaded:{audio}")


def play_sound(master):
    global audio
    play_window = Toplevel(master)
    play_window.geometry("500x500")
    player = SamplePlayer(play_window, audio)


ampl_entry = Entry(master, textvariable=ampl_value).grid(row=1, column=2)

import_sound_btn = Button(master,
                          text="import ",
                          height=5, width=20,
                          command=partial(import_sound, master)
                          ).grid(row=1, column=0)

play = Button(master,
              text="Play",
              height=5, width=20,
              command=partial(play_sound, master),
              ).grid(row=2, column=0)

make_louder = Button(master,
                     text="Make Louder",
                     height=5, width=20,
                     command=partial(enhance_volume, master),
).grid(row=3, column=2)

record = Button(master,
                text="Record",
                height=5, width=20,
                command=partial(recording_window, master),
).grid(row=3, column=3)

master.mainloop()
