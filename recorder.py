from tkinter import *
import threading
import pyaudio
import wave
import time
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from functools import partial

duration = 5
freq = 44100
def start_recording_sound_device():
    recording = sd.rec(int(duration * freq), 
                samplerate=freq, channels=2)
    sd.wait()
    write('output.mp3', freq, recording)



def start_recording():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = 3
    filename = output.wav

    p = pyaudio.PyAudio
    
    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('Finished Recording')
    wf = wave.open(filename, 'wb')
    wf.setchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframs(b''.join(frames))
    wf.close()
def recording_window(master):
    recording_window = Toplevel(master)
    recording_window.geometry("500x500")

    start_recording_butt = Button(recording_window,
                         text="Record",
                         command=partial(start_recording)).grid(row=0, column=0) 