\# JARVIS AI Personal Voice Assistant



\## 1. Project Overview



JARVIS AI Personal Voice Assistant is a Python-based voice assistant that accepts spoken commands, processes them, and responds using text-to-speech. It includes face authentication before starting the assistant.



This project demonstrates speech recognition, voice interaction, computer vision, command processing, and basic automation.



\## 2. Features



\- \*\*Face Authentication:\*\* Uses OpenCV to authenticate the registered user.

\- \*\*Speech Recognition:\*\* Converts spoken commands into text using SpeechRecognition.

\- \*\*Text-to-Speech:\*\* Provides spoken responses using pyttsx3.

\- \*\*Time and Date:\*\* Announces the current time, day, and date.

\- \*\*Website Opening:\*\* Opens supported websites such as YouTube, Google, GitHub, LinkedIn, Gmail, Wikipedia, Reddit, and Stack Overflow.

\- \*\*Google Search:\*\* Opens Google search results for a spoken query.

\- \*\*Personalized Responses:\*\* Recognizes the registered user's saved name.

\- \*\*Error Handling:\*\* Handles unclear speech and several microphone or recognition errors.

\- \*\*Command-Based Interaction:\*\* Responds to greetings, identity questions, help requests, and exit commands.



\## 3. Technologies Used



\- Python

\- OpenCV

\- NumPy

\- SpeechRecognition

\- PyAudio

\- pyttsx3



\## 4. Project Structure



```text

AI\_Smart\_Assistant/

├── main.py

├── voice\_assistant.py

├── command\_executor.py

├── face\_auth.py

├── requirements.txt

├── README.md

└── models/

&#x20;   └── user\_name.txt

```



The `models` directory may also contain face-authentication data created by the application. Keep required model files and directories when setting up the project.



\## 5. Requirements



\- Python installed on your computer

\- A working microphone

\- A webcam for face authentication

\- An internet connection for online speech recognition and web searches

\- A compatible Windows environment



\## 6. Installation



\### Step 1: Open the project directory



Open PowerShell or a terminal in the project directory.



\### Step 2: Create a virtual environment



```powershell

python -m venv venv

```



\### Step 3: Activate the virtual environment



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### Step 4: Install dependencies



```powershell

python -m pip install --upgrade pip

pip install -r requirements.txt

```



If PyAudio installation fails, install a compatible version for your Python and Windows environment.



\## 7. How to Run



Start the application with:



```powershell

python main.py

```



Choose one of the menu options:



1\. Register or update face

2\. Start Jarvis

3\. Exit



To start the assistant, select option 2 and complete face authentication. Once authentication succeeds, speak a supported command near your microphone.



\## 8. Example Voice Commands



| Voice command | Expected action |

|---|---|

| Hello Jarvis | Responds with a greeting |

| Who are you? | Introduces the assistant |

| Who am I? | Announces the registered user's name |

| What time is it? | Announces the current time |

| What day is today? | Announces the current date |

| Open YouTube | Opens YouTube |

| Open GitHub | Opens GitHub |

| Search Python tutorials | Opens Google search results |

| Jarvis help | Lists supported commands |

| Stop Jarvis | Ends the assistant session |



Speech recognition may occasionally fail in a noisy environment. Speak clearly and retry if the assistant cannot understand a command.



\## 9. Error Handling and Limitations



\- Unclear speech prompts the user to try again.

\- Speech recognition may require an active internet connection.

\- Microphone and speech output errors are handled where implemented.

\- Only the commands implemented in `command\_executor.py` are supported.

\- Face authentication requires the project's registration and model data.

\- This project is a personal assistant prototype, not a full conversational AI system.



\## 10. Future Improvements



\- Add a configurable wake-word detector.

\- Support more desktop applications and system commands.

\- Improve speech recognition and noise handling.

\- Add reminders and task management.

\- Integrate an AI-powered conversational interface.

\- Add configurable user preferences.



\## 11. Author



\*\*Project:\*\* JARVIS AI Personal Voice Assistant



\*\*Program:\*\* Syntecxhub AI Task 4



\## 12. Acknowledgement



This project was developed as part of the Syntecxhub AI task program to practice Python programming, speech recognition, text-to-speech, computer vision, and automation.



