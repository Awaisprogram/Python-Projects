import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

# Initialize Speech Recognition, Text-to-Speech, and API Keys
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""

# Set up Gemini API Key
genai.configure(api_key="")

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")     

def aiProcess(command):
    model = genai.GenerativeModel("gemini-1.5-pro")  
    response = model.generate_content(command,
    generation_config={
            "max_output_tokens": 20,  # Short response limit
            "temperature": 0.7,  # Adjust randomness
        },)
    return response.text if response else "I'm sorry, I couldn't process that."


def processCommand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "play song" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=JVtKEX90SZ0")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in the library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=pk&apiKey={newsapi}")
        if r.status_code == 200:
            articles = r.json().get('articles', [])
            for article in articles[:5]:  # Read only the top 5 headlines
                speak(article['title'])
    else:
        # Let Gemini handle the request
        output = aiProcess(c)
        speak(output) 

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand the audio, please try again.")
            speak("Please say it again.")
        except sr.WaitTimeoutError:
            print("Listening timed out. No voice detected.")
        except sr.RequestError:
            print("Could not request results from Google Speech API")
            speak("There was an issue with speech recognition. Please check your internet.")
        except Exception as e:
            print(f"Error: {e}")
