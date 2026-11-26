#im using pythons textual library for making the UI in here



from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label
from textual import events

try:
    from piano import PianoWidget
except ImportError:
    PianoWidget = None

try:
    from guitar import GuitarWidget
except ImportError:
    GuitarWidget = None

try:
    from drums import DrumsWidget
except ImportError:
    DrumsWidget = None

try:
    from violin import ViolinWidget
except ImportError:
    ViolinWidget = None

#Ui for the termnial izz here
class TerminalMusicPlayer(App):

    CSS = """
    Screen {
        align: center middle;
        background: #121212;
        color: white;
    }

    #main-box {
        width: 80;
        height: 28;
        border: solid #444444;
        padding: 1 2;
        background: #1a1a1a;
    }

    #title {
        width: 100%;
        content-align: center middle;
        text-style: bold;
        margin-bottom: 1;
    }

    #menu-bar {
        width: 100%;
        height: 3;
        align: center middle;
        margin-bottom: 1;
    }

    .unlocked-btn {
        margin: 0 1;
        min-width: 15;
    }

    .locked-btn {
        margin: 0 1;
        min-width: 17;
        background: #2a2a2a;
        color: #666666;
    }

    #main-status {
        width: 100%;
        content-align: center middle;
        color: #aaaaaa;
        margin-bottom: 1;
    }

    #instrument-container {
        width: 100%;
        height: 18;
        align: center middle;
    }
    """

    def __init__(self):
        super().__init__()
        self.current_instrument = None

 #as i post updates of this project i will slowly make it all and unlock different instruments
    def compose(self) -> ComposeResult:
        with Vertical(id="main-box"):
            yield Label("  (Press Q to Quit)", id="title")

            #these are the buttons which will help to choose iqnstrument that will be played in terminal
            with Horizontal(id="menu-bar"):
                if PianoWidget is not None:
                    yield Button("Piano", id="opt-piano", classes="unlocked-btn", variant="primary")
                else:
                    yield Button("Piano (Locked)", id="opt-piano", classes="locked-btn")

                if GuitarWidget is not None:
                    yield Button("Guitar", id="opt-guitar", classes="unlocked-btn", variant="success")
                else:
                    yield Button("Guitar (Locked)", id="opt-guitar", classes="locked-btn")

                if DrumsWidget is not None:
                    yield Button("Drums", id="opt-drums", classes="unlocked-btn", variant="warning")
                else:
                    yield Button("Drums (Locked)", id="opt-drums", classes="locked-btn")

                if ViolinWidget is not None:
                    yield Button("Violin", id="opt-violin", classes="unlocked-btn", variant="error")
                else:
                    yield Button("Violin (Locked)", id="opt-violin", classes="locked-btn")

            yield Label("Select an instrument above or use hotkeys below", id="main-status")

            # Area where the active instrument appears
            with Vertical(id="instrument-container"):
                if PianoWidget is not None:
                    yield PianoWidget(id="view-piano")
                if GuitarWidget is not None:
                    yield GuitarWidget(id="view-guitar")
                if DrumsWidget is not None:
                    yield DrumsWidget(id="view-drums")
                if ViolinWidget is not None:
                    yield ViolinWidget(id="view-violin")

    def on_mount(self) -> None:
        self.hide_all_instruments()

        
        if PianoWidget is not None:
            piano = self.query_one("#view-piano")
            piano.display = True
            self.current_instrument = piano

    def hide_all_instruments(self) -> None:
        if PianoWidget is not None:
            self.query_one("#view-piano").display = False
        if GuitarWidget is not None:
            self.query_one("#view-guitar").display = False
        if DrumsWidget is not None:
            self.query_one("#view-drums").display = False
        if ViolinWidget is not None:
            self.query_one("#view-violin").display = False

    def on_key(self, event: events.Key) -> None:
        key = event.key.lower()

        if key == "q":
            self.exit()
        elif self.current_instrument is not None:
            # Send the key press to whichever instrument is currently active
            self.current_instrument.handle_key(key)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id
        status = self.query_one("#main-status", Label)

        if btn_id == "opt-piano":
            if PianoWidget is None:
                status.update("Piano is locked! ")
            else:
                self.hide_all_instruments()
                piano = self.query_one("#view-piano")
                piano.display = True
                self.current_instrument = piano
                status.update("Switched to: Piano")

        elif btn_id == "opt-guitar":
            if GuitarWidget is None:
                status.update("Guitar is locked! ")
            else:
                self.hide_all_instruments()
                guitar = self.query_one("#view-guitar")
                guitar.display = True
                self.current_instrument = guitar
                status.update("Switched to: Guitar")

        elif btn_id == "opt-drums":
            if DrumsWidget is None:
                status.update("Drums are locked! ")
            else:
                self.hide_all_instruments()
                drums = self.query_one("#view-drums")
                drums.display = True
                self.current_instrument = drums
                status.update("Switched to: Drums")

        elif btn_id == "opt-violin":
            if ViolinWidget is None:
                status.update("Violin is locked! ")
            else:
                self.hide_all_instruments()
                violin = self.query_one("#view-violin")
                violin.display = True
                self.current_instrument = violin
                status.update("Switched to: Violin")


if __name__ == "__main__":
    app = TerminalMusicPlayer()
    app.run()