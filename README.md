# JARVIS AI Personal Voice Assistant

**Syntecxhub AI Task 4**

JARVIS is a Python-based personal voice assistant that supports voice interaction, text commands, face authentication, spoken responses, and web searches.

## Features

- Face authentication using the project's implemented authentication system.
- Speech recognition using SpeechRecognition.
- Text-to-speech responses using pyttsx3.
- Voice and text command interaction.
- Personal profile, education, skills, projects, and career information.
- Date and time responses.
- Opening supported websites.
- Google search for user queries.
- Error handling for speech recognition and microphone issues.

## Technologies Used

- Python
- OpenCV
- NumPy
- SpeechRecognition
- PyAudio
- pyttsx3

## Project Structure

```text
AI_Smart_Assistant/
├── main.py
├── voice_assistant.py
├── command_executor.py
├── face_auth.py
├── requirements.txt
├── README.md
├── test_voice.py
└── models/
```

## Requirements

- Python installed on your computer.
- A working microphone for voice interaction.
- A webcam for face authentication.
- Internet access for online speech recognition and Google searches.
- The required Python packages listed in `requirements.txt`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/purna00/Syntecxhub_AI_Smart_Assistant.git
   ```

2. Open the project directory:

   ```bash
   cd Syntecxhub_AI_Smart_Assistant
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate it on Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Run the Assistant

Start the application:

```bash
python main.py
```

Follow the on-screen menu to register or update face authentication, start JARVIS, or exit.

## Example Commands

- Hello Jarvis
- Who are you?
- Who am I?
- Tell me about my education.
- What are my skills?
- Tell me about my projects.
- What time is it?
- Open YouTube.
- Open GitHub.
- Search Google for Python tutorials.
- Help
- Switch to text mode.
- Exit

The exact commands supported depend on the implementation in `command_executor.py`.

## Limitations

- Online speech recognition may require an internet connection.
- Recognition accuracy may be affected by background noise.
- Face authentication must be configured locally.
- Only implemented commands are supported.

## Author

**Molugu Purna Shankar**

## Acknowledgement

Developed as part of the Syntecxhub AI Task 4 project to practice Python programming, speech recognition, text-to-speech, computer vision, and automation.
