
import pyttsx3

print("Initializing speech engine...")

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

print("Speaking test message...")
engine.say("Hello sir. JARVIS voice output is working.")
engine.runAndWait()

print("Speech test completed.")
