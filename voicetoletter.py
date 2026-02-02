"""
Voice-to-Letter Assistant - Speech Recognition & Voice Assistant
Converts your voice into text smoothly, Alexa-style.
"""

import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore
import sounddevice as sd  # type: ignore
import numpy as np  # type: ignore

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure TTS for smoother voice
engine.setProperty('rate', 150)   # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)


def speak(text: str):
    """Speak text aloud (Alexa-like response)."""
    engine.say(text)
    engine.runAndWait()


# Audio settings for speech (compatible with Google Speech Recognition)
SAMPLE_RATE = 16000
CHANNELS = 1
MAX_PHRASE_SECONDS = 10


def listen_and_convert():
    """
    Listen to microphone and convert voice to text.
    Uses sounddevice (no PyAudio needed). Returns the recognized text or None if failed.
    """
    print("  Adjusting for ambient noise... Please wait.")
    # Short calibration recording (discarded)
    _ = sd.rec(int(0.5 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="int16")
    sd.wait()
    print("  Speak now! (listening...)")

    recording = sd.rec(
        int(MAX_PHRASE_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
    )
    sd.wait()

    audio_bytes = recording.tobytes()
    audio = sr.AudioData(audio_bytes, SAMPLE_RATE, 2)  # 2 = 16-bit sample width

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return text.strip()
    except sr.UnknownValueError:
        print("  Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"  Speech service error: {e}")
        return None


def voice_assistant_mode():
    """Interactive voice assistant mode - like Alexa."""
    speak("Hello! I'm your voice assistant. Say something and I'll convert it to text.")
    print("\n" + "="*50)
    print("  VOICE ASSISTANT MODE voice to letter")
    print("  Say 'exit' or 'quit' to stop")
    print("="*50 + "\n")

    while True:
        print("\n  Listening...")
        text = listen_and_convert()
        
        if text:
            print(f"\n  >> You said: {text}")
            speak(f"You said: {text}")
            
            if text.lower() in ("exit", "quit", "stop"):
                speak("Goodbye!")
                print("\n  Assistant stopped.")
                break


def simple_voice_to_text_mode():
    """Simple mode: just convert voice to text, no TTS."""
    print("\n" + "="*50)
    print("  SIMPLE VOICE-TO-TEXT MODE")
    print("  Speak and see the text appear")
    print("="*50 + "\n")

    while True:
        print("\n  [Press Enter to listen, or type 'q' to quit]")
        if input().lower() == 'q':
            break
            
        text = listen_and_convert()
        if text:
            print(f"\n  >> {text}\n")


def main():
    print("\n  Voice-to-Letter Assistant")
    print("  -------------------------")
    print("  1. Voice Assistant (voice to letter, speaks back)")
    print("  2. Simple Voice-to-Text (only converts to text)")
    print("  3. Single conversion (one-time)")
    choice = input("\n  Choose (1/2/3): ").strip() or "3"

    if choice == "1":
        voice_assistant_mode()
    elif choice == "2":
        simple_voice_to_text_mode()
    else:
        print("\n  Speak when ready...")
        text = listen_and_convert()
        if text:
            print(f"\n  >> {text}\n")
        else:
            print("  No text recognized.")


if __name__ == "__main__":
    main()
