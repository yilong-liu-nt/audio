from tkinter import *
import threading
import pyaudio
import wave
import time
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from functools import partial
import numpy as np

def start_recording_sound_device(duration):
    freq = 44100

    print("Duration", duration)

    recording = sd.rec(int(duration * freq), 
                samplerate=freq, channels=2, dtype=np.int16)
    sd.wait()
    write('output.wav', freq, recording)

    
def recording_window(master, duration):
    recording_window = Toplevel(master)
    recording_window.geometry("500x500")

    start_recording_butt = Button(recording_window,
                         text="Record",
                         command=partial(start_recording_sound_device, duration)).grid(row=0, column=0) 