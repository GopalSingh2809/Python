import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Websites list
sites=[["Youtube","https://www.youtube.com/"],["Google","https://www.google.com/"],
       ["Mail","https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],["Amazon","https://www.amazon.in/"],
       ["Flipkart","https://www.flipkart.com/"],["Spotify","https://open.spotify.com/"]]

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}")

print("Welcome of the world of Artificial Intelligence.")
query=listen().lower()


if not query :
    print("Sorry, I couldn't understand that.")

if "open" in query:
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])

elif "the time" in query:
    hour = datetime.datetime.now().strftime("%H")
    min = datetime.datetime.now().strftime("%M")
    speak(f"Sir time is {hour} and {min} minutes")

elif query == "Who are you":
    intro="I am a Virtual Assistant , made for making our life easier and comfortable."
    speak(f"{intro}")
    print(f"Jarvis said:{intro}")
else:
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(f"Jarvis said:{summary}")
        speak(summary)
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information about that.")







