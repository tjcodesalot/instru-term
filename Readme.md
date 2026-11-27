1. **The Idea:**
The idea of this project was to make a minimal retro style terminal running musical instrument player, It runs smoothly on term without cluttering the screen with heavy graphics. I wanted Clean keyboard operated UI where pressing keys will play real musical notes.

More importantly, I didn't want all instruments hardcoded into one massive file. I wanted a modular "unlockable" architecture—starting with a working Piano, while keeping Guitar, Drums, and Violin locked in the menu until their individual code modules are dropped into the project folder.

2. **Tech Stacks**
Textual: Its a termnial UI framework and Standard terminal scripts only print text line-by-line in this. Textual will help us build actual layout(rows, column buttons etc)

Pygame : I use pygame.mixer strictly for its audio engine so multiple notes can ring out without freezing or altering.

Python Standard Library: Insted of downloading external .wav or .mp3 for every single note, i used built in modules like math, wave, struct and io to generate our own audio waves in memory when the app starts

One of the coolest parts of this project is create_piano_sound(frequency). Sound is just a vibrating wave at a specific frequency (for example, Middle C is 261.63 Hz and the A note is 440.00 Hz).

**RoadMap:**
I will update and make my project according to this roadmap
main.py 
piano.py
guitar.py
drums.py
violin.py

**AI USAGE**
I used ai for calculating the required frequencies and calculating sine wave math





**LOGS:**


Log.1:

Today I created Main.py and init i made UI and a different preplanned system like the more i make this project more it will unlock other instruments, Like i make piano and save the file it will be ready to use without touching main.py again. I am planning to add widgets to different instrument so i have already imported it in main.py. The main.py app will try to import PianoWidget, GuitarWidget, DrumsWidget, and ViolinWidget from their respective .py files:

   from guitar import GuitarWidget
except ImportError:
   GuitarWidget = None
If guitar.py does not exist in the folder yet, Python catches the ImportError and sets GuitarWidget = None instead of crashing. Menu shows locked if it doesnt find the instruments widgets like If PianoWidget exists -> Renders an active "Piano" button. If GuitarWidget is None -> Renders a grayed-out "Guitar (Locked)" button.


Log.2:

What i built today:
Today i made the first instrument piano. I built a 8-key layout (c4-C5) in piano.py with the keyboard hotkyes ( A S D F G H J K) 

How it works:
It calculates a pure sine wave i.e (math.sin(2*pi*freq*t) at a 22,050 Hz sample rate and writes the 16 bit audio(data) directly into a virtual RAM before loading it into pygame.mixer.Sound.Label


Fixes and challanges:
Problem: At first, the raw sine wave sounded like a microwave beep insted of a musical key.Label
Fix: I added a linear fadew out multiplier( fade= 1.0 - (i/num_samples)) inside the loop so the volume naturally decays after the initial key strike.

Log.3:

what i built today:
Today i built guitar.py to represent a acoustic 6-string guitar tuned to standard tuning(E2, A2, D3, G3, B3, E4), mapped 
to the number keys 1,2,3,4,5,6. 

How it works:
Making it sound like a sting: if i used plain sine wave like a piano then the guitar would just sound like a lower-pitched piano.
To give it a warmer, metallic plucked-string sound, I layred harmonics into da wave generator-combining the base frequency (wave1)
with a overtone with double the frequency ```(wave2= 0.5 * sin(2*pi*(frequency*2)*t)).```

I also increased da note duration fromm 0.5s to 0.7s so the string ring out longer when plucked.

Challanges and fixes:
Problems: combining two audio waves doubled the amplitude and caused audio clipping(distortion)
fixx: I scaled down the master volume multiplier to 0.3 before packing it into a 16 bit integer so the combined harmonic wave stays clean..