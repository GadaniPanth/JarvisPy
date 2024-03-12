import speech_recognition as sr


def speechrecognition():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Listening...", flush=True)
        audio = r.listen(source, timeout=2)
    try:
        print("Recogizing...")
        query = r.recognize_google(audio)
        # print()
        print("You: ", query)
        return query.lower()
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    while True:
        query = speechrecognition()
        if query:
            if query.lower() == "exit":
                print("Exiting...")
                break
