import warnings
import pyautogui
from gpt4 import GPT
from gpt4 import codePy
from head.speak import speakBot
from head.listen import speechrecognition
from datetime import datetime
from functions.emailsender import email_send

try:
    import pywhatkit
except:
    internet = False
else:
    internet = True

warnings.simplefilter("ignore")
x = 0


def checker():
    global internet
    while not internet:
        import time
        import socket
        import sys

        try:
            socket.create_connection(("www.google.com", 80))
            internet = True
            x = 0
        except OSError:
            if x == 0:
                speakBot("There's no Internet! Waiting for Internet.")
                x = 1
            max_dots = 3
            dots = 1
            for i in range(6):
                sys.stdout.write(
                    "\r" + "Waiting for internet" + "." * dots + " " * (max_dots - dots)
                )
                sys.stdout.flush()
                time.sleep(1)
                dots = (dots + 1) % (max_dots + 1)


def main():
    flag = True
    speakBot("Hello Sir! How can I assist you?")
    while True:
        if flag:
            checker()
            Query = str(speechrecognition()).lower()

        if "exit" in Query or "bye" in Query or "close self" in Query:
            speakBot("Goodbye Sir!")
            exit()

        elif "switch tab" in Query:
            pyautogui.hotkey("ctrl", "tab")

        elif "close tab" in Query:
            pyautogui.hotkey("ctrl", "w")

        elif "close" in Query or "open" in Query:
            codePy(Query)

        elif "play" in Query:
            # song_name = Query.replace("play", "")
            # pywhatkit.playonyt(song_name)
            codePy(Query)

        elif "time" in Query:
            if "current" in Query:
                currunttime = datetime.now().strftime("%H:%M %p")
                speakBot("Current Time Is: " + currunttime)
            else:
                speakBot(GPT(Query))

        elif "sleep" in Query:
            if flag:
                speakBot("Okay Sir! Just say wake up and I will be there")

            while True:
                Query = speechrecognition().lower()
                if "wake up" in Query or "jarvis" in Query:
                    speakBot("Yes Sir! how can I help u?")
                    flag = True
                    break

        elif (
            "send an email" in Query
            or "send email" in Query
            or "write an email" in Query
            or "compose an email" in Query
        ):
            speakBot("To Whom u want to send Mail?: ")
            to_whome = input("Enter Email: ")
            speakBot("What's the Subject?: ")
            subject = speechrecognition()
            speakBot("What should be the content? just provide me some prompt")
            email_prompt = input()
            content = GPT(
                "write a basic email on "
                + email_prompt
                + f" to {to_whome} don't write code"
            )
            email_send(to_whome, subject, content)

        elif "generate image" in Query or "give image" in Query:
            GPT(Query)

        elif Query == "":
            speakBot("Sorry! I didn't get any command so I'm on sleep")
            Query = "sleep"
            flag = False

        else:
            codePy(Query)


try:
    checker()
    main()
except Exception as e:
    print(e)