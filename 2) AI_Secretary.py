import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit

text = None
i = 0

def say(line):
    """Converts given text to speech."""
    engine = pyttsx3.init()
    engine.say(line)
    engine.runAndWait()

def listen(phrase):
    """Listens to microphone input and returns recognized text."""
    r = sr.Recognizer()
    print('')
    while True:
        try:
            with sr.Microphone() as source:
                print(f"Listening to {phrase}.....")
                audio = r.listen(source=source, timeout=0, phrase_time_limit=2)
            global text
            text = r.recognize_google(audio)
            return text
        except:
            print('Please speak clearly\n')

def speak():
    """Repeats whatever the user speaks."""
    say('Listening to speak')
    while True:
        text = listen("speak")
        say(text)
        return intro()

def open():
    """Opens common websites based on voice commands."""
    say('Listening to open')
    while True:
        text = listen('open')
        if 'youtube' in text.lower():
            say('opening youtube')
            webbrowser.open("https://www.youtube.com")
            return intro()
        elif 'google' in text.lower():
            say('opening google')
            webbrowser.open("https://www.google.com")
            return intro()
        elif 'chat' in text.lower():
            say('opening chat')
            webbrowser.open("https://chat.openai.com")
            return intro()

def play_song():
    """Plays requested song directly on YouTube."""
    say('Sure, please tell the name of the song')
    text = listen('song')
    pywhatkit.playonyt(text)
    return intro()
        
def intro():
    """Main interaction loop that routes user commands."""
    global i
    if i == 0:
        print('Hello sir!, How can i help you?')
        say('Hello sir!, How can i help you?')
        i = 1
    else:
        print("Any more commands?")
    while True:
        text = listen('command')
        if 'speak' in text.lower():
            return speak()
        elif 'open' in text.lower():
            return open()
        elif 'play song' in text.lower():
            return play_song()
        elif 'stop' in text.lower():
            print('AI listener stopped successfully')
            break

intro()
