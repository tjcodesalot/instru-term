import io
import math
import random
import struct
import wave
import pygame

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label


pygame.mixer.init()

#sound fix :) kinda tiring
def create_kick_sound():
    sample_rate = 22050
    duration = 0.3
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0 - (i / num_samples)
        # Frequency drops from 130Hz down to 40Hz for a bass thump
        freq = 130 - (90 * (i / num_samples))
        sample = 32767 * 0.7 * fade * math.sin(2 * math.pi * freq * t)
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


def create_snare_sound():
    sample_rate = 22050
    duration = 0.25
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0 - (i / num_samples)
        noise = random.uniform(-1, 1)
        tone = math.sin(2 * math.pi * 180 * t)
        sample = 32767 * 0.4 * fade * (0.7 * noise + 0.3 * tone)
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


def create_hihat_sound():
    sample_rate = 22050
    duration = 0.12
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        fade = 1.0 - (i / num_samples)
        # Fast sharp decay with white noise
        noise = random.uniform(-1, 1)
        sample = 32767 * 0.3 * (fade * fade) * noise
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


def create_tom_sound():
    sample_rate = 22050
    duration = 0.3
    num_samples = int(sample_rate * duration)

    buffer = io.BytesIO()
    wav_file = wave.open(buffer, "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    for i in range(num_samples):
        t = i / sample_rate
        fade = 1.0 - (i / num_samples)
        freq = 200 - (80 * (i / num_samples))
        sample = 32767 * 0.5 * fade * math.sin(2 * math.pi * freq * t)
        data = struct.pack("<h", int(sample))
        wav_file.writeframesraw(data)

    wav_file.close()
    buffer.seek(0)
    return pygame.mixer.Sound(file=buffer)


sound_kick = create_kick_sound()
sound_snare = create_snare_sound()
sound_hihat = create_hihat_sound()
sound_tom = create_tom_sound()


class DrumsWidget(Vertical):
#the tiling for the drumms
    DEFAULT_CSS = """
    DrumsWidget {
        width: 100%;
        height: 18;
        align: center middle;
    }

    #drums-label {
        width: 100%;
        content-align: center middle;
        color: #fd971f;
        margin-bottom: 1;
    }

    #drums-row {
        width: 100%;
        height: 14;
        align: center middle;
    }

    .pad-column {
        width: 14;
        height: 14;
        align: center middle;
    }

    .drum-pad {
        width: 12;
        height: 8;
        min-width: 12;
        background: #2d2d2d;
        color: white;
        border: heavy #fd971f;
    }

    .drum-pad.active {
        background: #fd971f;
        color: black;
    }
    """
#keybinds/hotkeyz
    def compose(self) -> ComposeResult:
        yield Label("Drums Ready - Press Z X C V to hit pads", id="drums-label")

        with Horizontal(id="drums-row"):
            with Vertical(classes="pad-column"):
                yield Button("KICK", id="pad-kick", classes="drum-pad")
                yield Label("[ Z ]", classes="hotkey-text")

            with Vertical(classes="pad-column"):
                yield Button("SNARE", id="pad-snare", classes="drum-pad")
                yield Label("[ X ]", classes="hotkey-text")

            with Vertical(classes="pad-column"):
                yield Button("HI-HAT", id="pad-hihat", classes="drum-pad")
                yield Label("[ C ]", classes="hotkey-text")

            with Vertical(classes="pad-column"):
                yield Button("TOM", id="pad-tom", classes="drum-pad")
                yield Label("[ V ]", classes="hotkey-text")

    def hit_pad(self, name, pad_id, sound):
        sound.play()

        label = self.query_one("#drums-label", Label)
        label.update("Drum Hit: " + name)

        button = self.query_one("#" + pad_id, Button)
        button.add_class("active")

        def reset_pad():
            button.remove_class("active")

        self.set_timer(0.15, reset_pad)

    def handle_key(self, key: str) -> None:
        if key == "z":
            self.hit_pad("Kick Drum", "pad-kick", sound_kick)
        elif key == "x":
            self.hit_pad("Snare Drum", "pad-snare", sound_snare)
        elif key == "c":
            self.hit_pad("Hi-Hat", "pad-hihat", sound_hihat)
        elif key == "v":
            self.hit_pad("Tom Drum", "pad-tom", sound_tom)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "pad-kick":
            self.hit_pad("Kick Drum", "pad-kick", sound_kick)
        elif btn_id == "pad-snare":
            self.hit_pad("Snare Drum", "pad-snare", sound_snare)
        elif btn_id == "pad-hihat":
            self.hit_pad("Hi-Hat", "pad-hihat", sound_hihat)
        elif btn_id == "pad-tom":
            self.hit_pad("Tom Drum", "pad-tom", sound_tom)






