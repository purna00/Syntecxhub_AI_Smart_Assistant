
import speech_recognition as sr
import pyttsx3


class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = None

        # Test speech engine initialization.
        self._test_engine = pyttsx3.init("sapi5")
        self._test_engine.setProperty("rate", 170)
        self._test_engine.setProperty("volume", 1.0)
        self._test_engine.stop()
        del self._test_engine

        print("[JARVIS] Voice assistant initialized.", flush=True)

    def speak(self, text):
        """Speak a response using a fresh Windows SAPI5 engine."""
        if text is None or not str(text).strip():
            return

        engine = None

        try:
            message = str(text).strip()
            print(f"[JARVIS SPEAKING] {message}", flush=True)

            engine = pyttsx3.init("sapi5")
            engine.setProperty("rate", 170)
            engine.setProperty("volume", 1.0)

            engine.say(message)
            engine.runAndWait()
            engine.stop()

            print("[JARVIS] Speech playback completed.", flush=True)

        except Exception as error:
            print(
                f"[JARVIS SPEECH ERROR] {type(error).__name__}: {error}",
                flush=True,
            )

        finally:
            if engine is not None:
                try:
                    engine.stop()
                except Exception:
                    pass

    def listen(self):
        """Listen for a voice command and convert it to text."""
        try:
            with sr.Microphone() as source:
                print("[JARVIS] Adjusting microphone...", flush=True)
                self.recognizer.adjust_for_ambient_noise(
                    source, duration=0.5
                )

                print("[JARVIS] Listening...", flush=True)
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10,
                )

            print("[JARVIS] Recognizing speech...", flush=True)

            command = self.recognizer.recognize_google(
                audio,
                language="en-IN",
            )

            command = command.strip()
            print(f"[JARVIS] Recognized: {command}", flush=True)
            return command

        except sr.WaitTimeoutError:
            print("[JARVIS] No speech detected. Try again.", flush=True)
            return ""

        except sr.UnknownValueError:
            print("[JARVIS] Sorry, I couldn't understand.", flush=True)
            return ""

        except sr.RequestError as error:
            print(
                f"[JARVIS] Speech recognition service error: {error}",
                flush=True,
            )
            return ""

        except Exception as error:
            print(
                f"[JARVIS LISTEN ERROR] {type(error).__name__}: {error}",
                flush=True,
            )
            return ""
