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
ampl_value = StringVar(name="amplication value", value="10")
sped = StringVar(name="speed", value="2")
duration_seconds = StringVar(name="Dursation", value="3")

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
    file_types = [('Wav Files', '*.wav'), ('Mp3 Files', '*.mp3')]
    filename_1 = filedialog.askopenfilename(filetypes=file_types)
    audio = filename_1
    print(f"file uploaded:{audio}")


def play_sound(master):
    global audio
    play_window = Toplevel(master)
    play_window.geometry("500x500")

    try:
        play_speed = float(sped.get())
    except:
        play_speed = 1.0

    print("Play speed", play_speed)

    player = SamplePlayer(play_window, audio, rate_ratio = play_speed)


def record(master):
    try:
        duration = float(duration_seconds.get())
    except:
        duration = 3

    recording_window(master, duration)

Label(master, text="Volumne Increase/Decrease").grid(row=4, column=2)
ampl_entry = Entry(master, textvariable=ampl_value).grid(row=4, column=3)

Label(master, text="Speed Ratio").grid(row=2, column=2)
speed_factor = Entry(master, textvariable=sped).grid(row=2, column=3)


Label(master, text="Duration").grid(row=5, column=2)
duration_entry = Entry(master, textvariable=duration_seconds).grid(row=5, column=3)


import_sound_btn = Button(master,
                          text="import",
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
).grid(row=4, column=0)

record = Button(master,
                text="Record",
                height=5, width=20,
                command=partial(record, master),
).grid(row=5, column=0)

master.mainloop()
