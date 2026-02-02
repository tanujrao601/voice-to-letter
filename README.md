# voice-to-letter

Speech recognition and voice assistant that converts your voice into text and speak also.

## Features

- **Voice Assistant mode** – Speak and hear your words repeated aloud.
- **Simple Voice-to-Text** – Speak and see the text on screen (no TTS).
- **Single conversion** – One-time voice-to-text.

Uses **Google Speech Recognition** (free) and **sounddevice** for microphone input (no PyAudio needed on Windows).

## Requirements

- Python 3.10+
- Microphone
- Internet (for Google Speech Recognition)

## Installation

1. Clone or download this project and open a terminal in its folder.

2. Create and use a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   Or install globally:

   ```bash
   pip install -r requirements.txt
   ```

3. Dependencies from `requirements.txt`:
   - SpeechRecognition
   - sounddevice
   - numpy
   - pyttsx3

## How to Run

**Option 1 – Double-click (Windows)**  
Run `run.bat`. It will install/check requirements and start the app.

**Option 2 – Command line**

```bash
# If using the project venv:
.venv\Scripts\activate
python voicetoletter.py

# Or with the venv Python directly:
.venv\Scripts\python.exe voicetoletter.py
```

## Modes

When you run the app, choose:

| Option | Mode | Description |
| 1 | Voice Assistant | Listens, converts to text, and speaks it back. Say "exit", "quit", or "stop" to end. |
| 2 | Simple Voice-to-Text | Press Enter to listen; your speech is shown as text. Type `q` to quit. |
| 3 | Single conversion | One listen, then the recognized text is printed. |

## Project Structure

```
.
├── voicetoletter.py   # Main application
├── requirements.txt  # Python dependencies
└── README.md          # This file
```

## Notes

- **Microphone**: Ensure your default microphone is working and allowed for the app.
- **Internet**: Google Speech Recognition needs an internet connection.
- **Privacy**: Audio is sent to Google’s servers for recognition.
