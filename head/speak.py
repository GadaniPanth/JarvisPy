import pyttsx3  # converts text to voice


def speakBot(text):
    engine = pyttsx3.init()
    engine.setProperty(
        "voice",
        r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
    )
    engine.say(text)
    print("Jarvis: ", end="")
    print(text, flush=True)
    engine.runAndWait()
