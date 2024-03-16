import tkinter as tk
import threading
import pyaudio
import wave
import time


class SamplePlayer:
    def __init__(self, master):
        frame = tk.Frame(master=master)
        frame.pack(expand=True, fill="both")

        self.current_lbl = tk.Label(master=frame, text="0/0")
        self.current_lbl.pack()

        self.pause_btn = tk.Button(master=frame, text="Pause", command=self.pause)
        self.pause_btn.pack()

        self.play_btn = tk.Button(master=frame, text="Play", command=self.play)
        self.play_btn.pack()

        # If you aren't going to use `\`s there is no need for the
        # "r" before the start of the string
        self.file = r"sample_wavfile.wav"

        self.paused = True
        self.playing = False

        self.audio_length = 0
        self.current_sec = 0

    def start_playing(self):
        """ # I don't have `pyaudio` so I used this to test my answer:
        self.audio_length = 200
        while self.playing:
            if not self.paused:
                self.current_sec += 1
                time.sleep(1)
        return None
        # """

        p = pyaudio.PyAudio()
        chunk = 1024
        with wave.open(self.file, "rb") as wf:
            self.audio_length = wf.getnframes() / float(wf.getframerate())

            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            data = wf.readframes(chunk)

            chunk_total = 0
            while data != b"" and self.playing:
                if self.paused:
                    time.sleep(0.1)
                else:
                    chunk_total += chunk
                    stream.write(data)
                    data = wf.readframes(chunk)
                    self.current_sec = chunk_total/wf.getframerate()

        self.playing = False
        stream.close()   
        p.terminate()

    def pause(self):
        self.paused = True
    
    def play(self):
        if not self.playing:
            self.playing = True
            threading.Thread(target=self.start_playing, daemon=True).start()

        if self.paused:
            self.paused = False
            self.update_lbl()

    def stop(self):
        self.playing = False

    def update_lbl(self):
        if self.playing and (not self.paused):
            self.current_lbl.config(text=f"{self.current_sec}/{self.audio_length}")
            # There is no need to update the label more than 10 times a second.
            # It changes once per second anyways.
            self.current_lbl.after(100, self.update_lbl)


def handle_close():
    player.stop()
    root.destroy()

## SETUP AND RUN
root = tk.Tk()
player = SamplePlayer(root)

root.protocol("WM_DELETE_WINDOW", handle_close)
root.mainloop()
