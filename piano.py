import io 
import math
import struct
import wave
import pygame

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label

pygame.mixer.init()

def create_piano_sound(frequency):
    sample_rate = 22050
    duration = 0.5
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setchannels(1)
    wav_file.sersampwidth(2)
    wav_file.setframerate(sample_rate)

for i in range(num_samples):
    t=i / sample_rate
    fade=1.0 - (i/ num_samples)
    sample = 32767 * 0.4 * fade * math.sin(2 * math.pi * frequency * t)
    data = struct.pack("<h",int(sample))
    wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return.pygame.mixer.Sound(file=buffer)

#these are the notes for piano

sound_c = create_piano_sound(261.63)
sound_d = create_piano_sound(293.66)
sound_e = create_piano_sound(329.63)
sound_f = create_piano_sound(349.23)
sound_g = create_piano_sound(392.00)