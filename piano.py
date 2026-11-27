import io
import math
import struct
import wave
import pygame

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label


pygame.mixer.init()
#calculates da frequency for each notesss

def create_piano_sound(frequency):
    sample_rate = 22050
    duration = 0.5
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0 - (i / num_samples)
        sample = 32767 * 0.4 * fade * math.sin(2 * math.pi * frequency * t)
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


# Piano notes that playz da sound, i have kept some limited notes cuz its a protype yettt
sound_c = create_piano_sound(261.63)
sound_d = create_piano_sound(293.66)
sound_e = create_piano_sound(329.63)
sound_f = create_piano_sound(349.23)
sound_g = create_piano_sound(392.00)
sound_a = create_piano_sound(440.00)
sound_b = create_piano_sound(493.88)
sound_c2 = create_piano_sound(523.25)

class PianoWidget(Vertical):
#the tiling for za piano Ui (blue tile btw)
    DEFAULT_CSS = """
    PianoWidget {
        width: 100%;
        height: 18;
        align: center middle;
    }

    #piano-note-label {
        width: 100%;
        content-align: center middle;
        color: #66d9ef;
        margin-bottom: 1;
    }

    #piano-row {
        width: 100%;
        height: 14;
        align: center middle;
    }

    .key-column {
        width: 8;
        height: 14;
        align: center middle;
    }

    .piano-key {
        width: 7;
        height: 10;
        min-width: 7;
        background: white;
        color: black;
        border: solid #888888;
    }

    .piano-key:focus {
        background: white;
        color: black;
        text-style: none;
    }

    .piano-key.active {
        background: #66d9ef;
        color: black;
    }

    .hotkey-text {
        width: 7;
        content-align: center middle;
        color: #888888;
        margin-top: 1;
    }
    """
#hottkeyssszz for the pianooo
    def compose(self) -> ComposeResult:
        yield Label("Piano Ready - Press A S D F G H J K", id="piano-note-label")

        with Horizontal(id="piano-row"):
            with Vertical(classes="key-column"):
                yield Button("C", id="piano-c", classes="piano-key")
                yield Label("[ A ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("D", id="piano-d", classes="piano-key")
                yield Label("[ S ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("E", id="piano-e", classes="piano-key")
                yield Label("[ D ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("F", id="piano-f", classes="piano-key")
                yield Label("[ F ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("G", id="piano-g", classes="piano-key")
                yield Label("[ G ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("A", id="piano-a", classes="piano-key")
                yield Label("[ H ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("B", id="piano-b", classes="piano-key")
                yield Label("[ J ]", classes="hotkey-text")

            with Vertical(classes="key-column"):
                yield Button("C5", id="piano-c2", classes="piano-key")
                yield Label("[ K ]", classes="hotkey-text")

    def play_note(self, note_name, key_id, sound):
        sound.play()

        label = self.query_one("#piano-note-label", Label)
        label.update("Piano Playing: " + note_name)

        button = self.query_one("#" + key_id, Button)
        button.add_class("active")

        def reset_key():
            button.remove_class("active")

        self.set_timer(0.15, reset_key)

    def handle_key(self, key: str) -> None:
        if key == "a":
            self.play_note("C", "piano-c", sound_c)
        elif key == "s":
            self.play_note("D", "piano-d", sound_d)
        elif key == "d":
            self.play_note("E", "piano-e", sound_e)
        elif key == "f":
            self.play_note("F", "piano-f", sound_f)
        elif key == "g":
            self.play_note("G", "piano-g", sound_g)
        elif key == "h":
            self.play_note("A", "piano-a", sound_a)
        elif key == "j":
            self.play_note("B", "piano-b", sound_b)
        elif key == "k":
            self.play_note("C5", "piano-c2", sound_c2)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "piano-c":
            self.play_note("C", "piano-c", sound_c)
        elif btn_id == "piano-d":
            self.play_note("D", "piano-d", sound_d)
        elif btn_id == "piano-e":
            self.play_note("E", "piano-e", sound_e)
        elif btn_id == "piano-f":
            self.play_note("F", "piano-f", sound_f)
        elif btn_id == "piano-g":
            self.play_note("G", "piano-g", sound_g)
        elif btn_id == "piano-a":
            self.play_note("A", "piano-a", sound_a)
        elif btn_id == "piano-b":
            self.play_note("B", "piano-b", sound_b)
        elif btn_id == "piano-c2":
            self.play_note("C5", "piano-c2", sound_c2)






       