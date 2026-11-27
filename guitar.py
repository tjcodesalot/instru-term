# this is the code for guitar lesgoo
import io
import math
import struct
import wave
import pygame

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label


pygame.mixer.init()


def create_guitar_sound(frequency):
    sample_rate = 22050
    duration = 0.7
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0 - (i / num_samples)
        # Dis Adds harmonics for a plucked string sound
        wave1 = math.sin(2 * math.pi * frequency * t)
        wave2 = 0.5 * math.sin(2 * math.pi * (frequency * 2) * t)
        sample = 32767 * 0.3 * fade * (wave1 + wave2)
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


# useddd 6 Guitar Strings (E A D G B E)
str_e_low = create_guitar_sound(164.81)
str_a = create_guitar_sound(220.00)
str_d = create_guitar_sound(293.66)
str_g = create_guitar_sound(392.00)
str_b = create_guitar_sound(493.88)
str_e_high = create_guitar_sound(659.25)


class GuitarWidget(Vertical):
#the guitars UI (green Tile btw)
    DEFAULT_CSS = """
    GuitarWidget {
        width: 100%;
        height: 18;
        align: center middle;
    }

    #guitar-label {
        width: 100%;
        content-align: center middle;
        color: #a6e22e;
        margin-bottom: 1;
    }

    #guitar-row {
        width: 100%;
        height: 14;
        align: center middle;
    }

    .string-column {
        width: 10;
        height: 14;
        align: center middle;
    }

    .guitar-key {
        width: 8;
        height: 10;
        min-width: 8;
        background: #3b2314;
        color: #f8f8f2;
        border: solid #c28b59;
    }

    .guitar-key.active {
        background: #a6e22e;
        color: black;
    }
    """
#hotkeys for the guitarr notess
    def compose(self) -> ComposeResult:
        yield Label("Guitar Ready - Press 1 2 3 4 5 6 to pluck strings", id="guitar-label")

        with Horizontal(id="guitar-row"):
            with Vertical(classes="string-column"):
                yield Button("E2", id="gtr-e1", classes="guitar-key")
                yield Label("[ 1 ]", classes="hotkey-text")

            with Vertical(classes="string-column"):
                yield Button("A2", id="gtr-a", classes="guitar-key")
                yield Label("[ 2 ]", classes="hotkey-text")

            with Vertical(classes="string-column"):
                yield Button("D3", id="gtr-d", classes="guitar-key")
                yield Label("[ 3 ]", classes="hotkey-text")

            with Vertical(classes="string-column"):
                yield Button("G3", id="gtr-g", classes="guitar-key")
                yield Label("[ 4 ]", classes="hotkey-text")

            with Vertical(classes="string-column"):
                yield Button("B3", id="gtr-b", classes="guitar-key")
                yield Label("[ 5 ]", classes="hotkey-text")

            with Vertical(classes="string-column"):
                yield Button("E4", id="gtr-e2", classes="guitar-key")
                yield Label("[ 6 ]", classes="hotkey-text")

    def pluck_string(self, name, btn_id, sound):
        sound.play()

        label = self.query_one("#guitar-label", Label)
        label.update("Plucked String: " + name)

        button = self.query_one("#" + btn_id, Button)
        button.add_class("active")

        def reset_string():
            button.remove_class("active")

        self.set_timer(0.15, reset_string)

    def handle_key(self, key: str) -> None:
        if key == "1":
            self.pluck_string("Low E", "gtr-e1", str_e_low)
        elif key == "2":
            self.pluck_string("A", "gtr-a", str_a)
        elif key == "3":
            self.pluck_string("D", "gtr-d", str_d)
        elif key == "4":
            self.pluck_string("G", "gtr-g", str_g)
        elif key == "5":
            self.pluck_string("B", "gtr-b", str_b)
        elif key == "6":
            self.pluck_string("High E", "gtr-e2", str_e_high)



           