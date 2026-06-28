import pyttsx3
import speech_recognition as sr
from datetime import datetime
import sys

# --- STAGE 2: The Mouth (Text-to-Speech) ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 175) 

def speak(text):
    """Prints the text to your screen and speaks it aloud."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# --- STAGE 3: The Ears (Speech-to-Text) ---
def listen_command():
    """Listens to the microphone and returns the speech converted to a string."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n[Listening... Speak now]")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("[Recognizing...]")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
        
    except sr.UnknownValueError:
        speak("I didn't quite catch that. Could you say it again?")
        return ""
    except sr.RequestError:
        speak("Network error. I am having trouble reaching my speech servers.")
        return ""

# --- STAGE 4: The Brain (Command Processing) ---
def process_command(command):
    """Processes the spoken text and determines the response action."""
    if not command:
        return True # Keep looping if nothing was heard

    # Command 1: Basic Greeting
    if "hello" in command or "hi" in command:
        speak("Hello Harsha! I am online and ready to help.")
        
    # Command 2: Telling the Time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        
    # Command 3: Identity check
    elif "who are you" in command or "your name" in command:
        speak("I am your custom Python voice assistant.")
        
    # Command 4: System Shutdown
    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Shutting down the assistant. Goodbye Harsha!")
        return False # Breaks the loop
        
    # Fallback if it doesn't recognize the command
    else:
        speak("I heard you, but I don't know how to handle that command yet.")
        
    return True # Keep looping

# --- STAGE 5: The Infinite Loop ---
if __name__ == "__main__":
    speak("Voice assistant activated. Say 'stop' to exit.")
    is_running = True
    
    while is_running:
        # 1. Listen to the user
        user_input = listen_command()
        
        # 2 & 3. Process the input and speak the output
        is_running = process_command(user_input)