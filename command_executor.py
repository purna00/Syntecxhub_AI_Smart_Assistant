
from datetime import datetime
from urllib.parse import quote_plus
import webbrowser
import re


# ============================================================
# USER PROFILE
# ============================================================

USER_NAME = "Molugu Purna Shankar"


# ============================================================
# COMMAND NORMALIZATION
# ============================================================

def normalize_command(command):
    """Normalize recognized or typed commands."""
    command = command.lower().strip()
    command = re.sub(r"[^\w\s]", "", command)
    command = re.sub(r"\s+", " ", command).strip()

    command = re.sub(
        r"^(hey|hi)\s+jarvis\b\s*", "", command
    )
    command = re.sub(r"^jarvis\b\s*", "", command)

    return command.strip()


# ============================================================
# COMMAND EXECUTOR
# ============================================================

def execute_command(command, user_name=USER_NAME):
    """Process commands and return a response for JARVIS."""

    command = normalize_command(command)

    if not command:
        return "Yes, sir. How can I help you?"

    # --------------------------------------------------------
    # EXIT COMMANDS
    # --------------------------------------------------------

    exit_commands = {
        "stop", "exit", "quit", "bye", "goodbye",
        "stop assistant", "exit assistant",
        "quit assistant", "close assistant",
        "shutdown assistant", "shut down assistant",
        "stop jarvis", "exit jarvis", "quit jarvis",
        "shutdown jarvis", "shut down jarvis"
    }

    if command in exit_commands:
        return "Goodbye, sir. JARVIS is shutting down."

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    if command in {
        "hello", "hi", "hey", "good morning",
        "good afternoon", "good evening"
    }:
        return f"Hello, sir. I am ready to help you, {user_name}."

    # --------------------------------------------------------
    # ABOUT ME
    # --------------------------------------------------------

    about_me_commands = {
        "who am i",
        "who m i",
        "my name",
        "what is my name",
        "whats my name",
        "tell me about myself",
        "tell me about me",
        "about me",
        "introduce me",
        "give me my profile",
        "describe me",
        "what do you know about me",
        "tell me my details",
        "tell me about my background",
        "who is my user"
    }

    if command in about_me_commands:
        return (
            f"Sir, your name is {user_name}. You completed your "
            "B.Tech in Electronics and Communication Engineering "
            "at Avanthi's Research and Technological Academy, "
            "Vizianagaram, in 2026, with a CGPA of 7.0 out of 10. "
            "Your skills include Python, SQL, JavaScript, machine "
            "learning, deep learning, computer vision, natural "
            "language processing, HTML, CSS, React, and MySQL. "
            "You have completed internships in PCB Design and "
            "Fabrication, SQL, and Embedded Systems. Your projects "
            "include aircraft surface defect detection using "
            "YOLOv8, fake news detection using NLP, Indian currency "
            "recognition, a temple website, and this JARVIS AI "
            "Smart Assistant. You are interested in entry-level "
            "roles in Python development, software engineering, "
            "AI, machine learning, and computer vision."
        )

    # --------------------------------------------------------
    # EDUCATION AND QUALIFICATIONS
    # --------------------------------------------------------

    education_commands = {
        "my education",
        "my qualifications",
        "my qualification",
        "what are my qualifications",
        "what are my qualification",
        "what is my qualification",
        "what is my educational qualification",
        "tell me my qualifications",
        "tell me about my qualifications",
        "what did i study",
        "tell me about my education",
        "my degree",
        "what is my degree",
        "where did i study"
    }

    if command in education_commands:
        return (
            "Sir, you completed your B.Tech in Electronics and "
            "Communication Engineering at Avanthi's Research and "
            "Technological Academy, Vizianagaram, from 2023 to "
            "2026, with a CGPA of 7.0 out of 10. You completed "
            "your diploma in Electronics and Communication "
            "Engineering at Government Polytechnic College, "
            "Chodavaram, from 2019 to 2022, with a CGPA of "
            "7.0 out of 10. You completed your SSC at Ideal "
            "English Medium School, Anakapalle, in 2019, "
            "with a CGPA of 9.3 out of 10."
        )

    # --------------------------------------------------------
    # TECHNICAL SKILLS
    # --------------------------------------------------------

    skill_commands = {
        "my skills",
        "my technical skills",
        "what are my skills",
        "what are my technical skills",
        "tell me my skills",
        "tell me about my skills",
        "tell me my technical skills",
        "tell me about my technical skills",
        "what are my programming skills",
        "what technologies do i know",
        "my programming skills",
        "my technical knowledge",
        "what programming languages do i know",
        "which programming languages do i know",
        "what skills do i have"
    }

    if command in skill_commands:
        return (
            "Sir, your programming languages include Python, SQL, "
            "and JavaScript. Your AI skills include machine learning, "
            "deep learning, computer vision, and natural language "
            "processing. Your web development skills include HTML5, "
            "CSS3, and React.js. You also know MySQL, Git, GitHub, "
            "embedded systems, PCB Design and Fabrication, and "
            "networking fundamentals."
        )

    # --------------------------------------------------------
    # PROJECTS
    # --------------------------------------------------------

    project_commands = {
        "my projects",
        "tell me about my projects",
        "tell me my projects",
        "what projects have i done",
        "list my projects",
        "my technical projects",
        "what are my projects",
        "describe my projects"
    }

    if command in project_commands:
        return (
            "Sir, you have worked on five main projects. First, "
            "aircraft surface defect detection using YOLOv8 and "
            "the NEU Surface Defect Dataset, achieving 73.3 percent "
            "mAP at 50 and 39.2 percent mAP at 50 to 95. Second, "
            "a fake news detection system using natural language "
            "processing and machine learning. Third, Indian currency "
            "recognition using OpenCV and TensorFlow. Fourth, a "
            "website for Mithranandapuram Vamanamoorthy Temple using "
            "HTML, CSS, and JavaScript. Fifth, your JARVIS AI Smart "
            "Assistant, which supports face authentication, speech "
            "recognition, spoken responses, and website automation."
        )

    # --------------------------------------------------------
    # INTERNSHIPS AND EXPERIENCE
    # --------------------------------------------------------

    internship_commands = {
        "my internships",
        "tell me about my internships",
        "tell me my internships",
        "what internships have i completed",
        "my work experience",
        "tell me about my experience",
        "where did i intern",
        "my internship experience"
    }

    if command in internship_commands:
        return (
            "Sir, you completed three internships. You worked "
            "as a PCB Design and Fabrication Intern at Skill Dzire "
            "from October 2025 to April 2026. You completed a SQL "
            "Internship through Infosys Springboard from September "
            "to December 2025. You also completed an Embedded "
            "Systems Internship at Skill Dzire from March to "
            "June 2025."
        )

    # --------------------------------------------------------
    # CERTIFICATIONS
    # --------------------------------------------------------

    certification_commands = {
        "my certifications",
        "tell me about my certifications",
        "tell me my certifications",
        "what certifications do i have",
        "list my certifications",
        "my certificates"
    }

    if command in certification_commands:
        return (
            "Sir, your certifications include Embedded Systems "
            "from SkillDzire in 2025, PCB Design and Fabrication "
            "from SkillDzire in 2026, Database and SQL from "
            "Infosys Springboard in 2026, and Developing "
            "Interpersonal Skills from IBM in 2024."
        )

    # --------------------------------------------------------
    # CAREER GOALS
    # --------------------------------------------------------

    career_commands = {
        "my career goal",
        "my career goals",
        "my career objective",
        "what job am i looking for",
        "what are my career goals",
        "what are y career goals",
        "what job do i want",
        "which job am i looking for",
        "my future goals",
        "what is my career goal",
        "tell me about my career goals",
        "what career am i looking for"
    }

    if command in career_commands:
        return (
            "Sir, you are looking for entry-level opportunities "
            "in Python development, software engineering, artificial "
            "intelligence, machine learning, and computer vision. "
            "Your Python, SQL, computer vision, and web development "
            "skills can help you grow in these fields."
        )

    # --------------------------------------------------------
    # ASSISTANT IDENTITY
    # --------------------------------------------------------

    if command in {
        "who are you",
        "who r you",
        "your name",
        "what are you",
        "introduce yourself"
    }:
        return "I am JARVIS, your personal AI assistant."

    # --------------------------------------------------------
    # ASSISTANT STATUS
    # --------------------------------------------------------

    if command in {"how are you", "how are u", "how r u"}:
        return "All systems are running smoothly, sir."

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if (
        command == "time"
        or "what time" in command
        or "current time" in command
        or "tell me the time" in command
        or "clock" in command
    ):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Sir, the current time is {current_time}."

    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    if (
        command == "date"
        or "date" in command
        or "today" in command
        or "what day" in command
        or "which day" in command
    ):
        current_date = datetime.now().strftime("%A, %d %B %Y")
        return f"Sir, today is {current_date}."

    # --------------------------------------------------------
    # SUPPORTED WEBSITES
    # --------------------------------------------------------

    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
        "linkedin": "https://www.linkedin.com",
        "gmail": "https://mail.google.com",
        "stackoverflow": "https://stackoverflow.com",
        "wikipedia": "https://www.wikipedia.org",
        "reddit": "https://www.reddit.com"
    }

    # --------------------------------------------------------
    # OPEN WEBSITE
    # --------------------------------------------------------

    if command.startswith("open "):
        site = command[5:].strip()
        site = re.sub(r"\s+website$", "", site)

        if site in websites:
            try:
                webbrowser.open(websites[site])
                return f"Opening {site.title()}, sir."
            except Exception as error:
                print(f"Website opening error: {error}")
                return "Sorry, sir. I could not open that website."

        if "." in site and " " not in site:
            url = site

            if not url.startswith(("https://", "http://")):
                url = "https://" + url

            try:
                webbrowser.open(url)
                return f"Trying to open {site}, sir."
            except Exception as error:
                print(f"Website opening error: {error}")
                return "Sorry, sir. I could not open that website."

        return (
            f"I don't have a shortcut for {site} yet, sir. "
            "Try Google, YouTube, GitHub, LinkedIn, or Gmail."
        )

    # --------------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------------

    search_prefixes = (
        "search for ",
        "search ",
        "google ",
        "look up ",
        "find information about "
    )

    for prefix in search_prefixes:
        if command.startswith(prefix):
            query = command[len(prefix):].strip()

            if query:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(query)
                )

                try:
                    webbrowser.open(url)
                    return f"Searching Google for {query}, sir."
                except Exception as error:
                    print(f"Search error: {error}")
                    return "Sorry, sir. I could not perform that search."

            return "What would you like me to search for, sir?"

    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    if command in {
        "help",
        "what can you do",
        "commands",
        "list commands",
        "your commands"
    }:
        return (
            "Sir, I can tell you about yourself, your education, "
            "skills, projects, internships, certifications, and "
            "career goals. I can tell you the time and date, open "
            "websites, and search Google. You can also switch "
            "between voice and text modes from the main assistant."
        )

    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    return (
        "I'm not sure how to do that yet, sir. "
        "Say Jarvis help to hear my available commands."
    )
