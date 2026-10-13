
import re
from pathlib import Path

from face_auth import register_face, authenticate_face
from voice_assistant import VoiceAssistant
from command_executor import execute_command


BASE_DIR = Path(__file__).resolve().parent
USER_NAME_FILE = BASE_DIR / "models" / "user_name.txt"
DEFAULT_USER_NAME = "User"


def get_user_name():
    try:
        if USER_NAME_FILE.exists():
            name = USER_NAME_FILE.read_text(encoding="utf-8").strip()
            if name:
                return name
    except OSError as error:
        print(f"Could not read user name: {error}")

    return DEFAULT_USER_NAME


def normalize_command(command):
    command = command.lower().strip()
    command = re.sub(r"[^\w\s]", "", command)
    command = re.sub(r"\s+", " ", command).strip()
    command = re.sub(r"^(hey|hi)\s+jarvis\b\s*", "", command)
    command = re.sub(r"^jarvis\b\s*", "", command)
    return command.strip()


EXIT_COMMANDS = {
    "stop", "exit", "quit", "bye", "goodbye",
    "stop jarvis", "exit jarvis", "quit jarvis",
    "stop assistant", "exit assistant", "quit assistant",
    "close assistant", "shutdown jarvis", "shut down jarvis"
}

VOICE_MODE_COMMANDS = {
    "switch to voice command", "switch to voice commands",
    "switch to voice mode", "voice mode",
    "enable voice mode", "start voice mode"
}

TEXT_MODE_COMMANDS = {
    "switch to text command", "switch to text commands",
    "switch to text mode", "text mode",
    "enable text mode", "start text mode"
}


def start_jarvis():
    print("\nStarting JARVIS...")

    try:
        authenticated = authenticate_face()
        if not authenticated:
            print("\nFace authentication failed. Please try again.")
            return
    except Exception as error:
        print(f"\nAuthentication error: {error}")
        return

    user_name = get_user_name()
    print(f"\nWelcome, {user_name}!")

    try:
        assistant = VoiceAssistant()
    except Exception as error:
        print(f"Could not initialize voice assistant: {error}")
        return

    mode = "voice"

    print("\nJARVIS is ready.")
    print("Current mode: VOICE")
    print("\nAvailable commands:")
    print("  Voice: Speak your command")
    print("  Text:  Switch to text mode")
    print("  Return to voice: Switch to voice command")
    print("  Exit: Stop Jarvis")

    assistant.speak(
        f"Welcome back, {user_name}. "
        "Jarvis is ready. How can I help you?"
    )

    try:
        while True:
            if mode == "voice":
                command = assistant.listen()
                if not command:
                    continue
                print(f"\nYou said: {command}")

            else:
                try:
                    command = input("\nYou: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print("\nReturning to the main menu.")
                    break

                if not command:
                    continue

            normalized = normalize_command(command)

            if normalized in TEXT_MODE_COMMANDS:
                if mode == "text":
                    message = "Sir, you are already in text mode."
                else:
                    mode = "text"
                    message = (
                        "Switching to text mode, sir. "
                        "Please type your commands."
                    )

                print(f"\nJARVIS: {message}")
                assistant.speak(message)
                continue

            if normalized in VOICE_MODE_COMMANDS:
                if mode == "voice":
                    message = "Sir, you are already in voice mode."
                else:
                    mode = "voice"
                    message = (
                        "Switching to voice mode, sir. "
                        "Please speak your commands."
                    )

                print(f"\nJARVIS: {message}")
                assistant.speak(message)
                continue

            if normalized in EXIT_COMMANDS:
                message = "Goodbye, sir. JARVIS is shutting down."
                print(f"\nJARVIS: {message}")
                assistant.speak(message)
                break

            try:
                response = execute_command(command, user_name)

                if response:
                    print(f"\nJARVIS: {response}", flush=True)
                    assistant.speak(response)

            except Exception as error:
                print(f"\nCommand execution error: {error}")
                message = "Sorry, sir. Something went wrong."
                print(f"\nJARVIS: {message}")
                assistant.speak(message)

    except KeyboardInterrupt:
        print("\nJARVIS interrupted by the user.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")

    finally:
        print("\nJARVIS session ended.")


def main():
    while True:
        print("\n" + "=" * 42)
        print("       JARVIS AI SMART ASSISTANT")
        print("=" * 42)
        print("1. Register / Update Face")
        print("2. Start JARVIS")
        print("3. Exit")
        print("=" * 42)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            try:
                register_face()
            except Exception as error:
                print(f"Face registration error: {error}")

        elif choice == "2":
            start_jarvis()

        elif choice == "3":
            print("\nThank you for using JARVIS. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
