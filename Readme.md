1. The Idea:
The idea of this project was to make a minimal retro style terminal running musical instrument player, It runs smoothly on term without cluttering the screen with heavy graphics. I wanted Clean keyboard operated UI where pressing keys will play real musical notes.

More importantly, I didn't want all instruments hardcoded into one massive file. I wanted a modular "unlockable" architecture—starting with a working Piano, while keeping Guitar, Drums, and Violin locked in the menu until their individual code modules are dropped into the project folder.

2. Tech Stacks
Textual: Its a termnial UI framework and Standard terminal scripts only print text line-by-line in this. Textual will help us build actual layout(rows, column buttons etc)

Pygame : I use pygame.mixer strictly for its audio engine so multiple notes can ring out without freezing or altering.

Python Standard Library: Insted of downloading external .wav or .mp3 for every single note, i used built in modules like math, wave, struct and io to generate our own audio waves in memory when the app starts

One of the coolest parts of this project is create_piano_sound(frequency). Sound is just a vibrating wave at a specific frequency (for example, Middle C is 261.63 Hz and the A note is 440.00 Hz).

RoadMap:
I will update and make my project according to this roadmap
main.py 
piano.py
guitar.py
drums.py
violin.py

**AI USAGE**
I used ai for calculating the required frequencies and calculating sine wave math

