import subprocess
from time import sleep
import g4f
import re
from head.speak import speakBot
import pickle

messages = [
    {
        "role": "system",
        "content": '''learn how to intents on user's context from this  
                        intents = {
                            "greetings": {
                                "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
                                "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", "Howdy! What brings you here?", "Greetings! How may I help you?", "Good morning! How can I be of service?", "Good afternoon! What do you need assistance with?", "Good evening! How may I assist you?", "Hey there! How can I help?", "Hi! What's on your mind?", "Hello there! How can I assist you today?"]
                            },
                            "goodbye": {
                                "patterns": ["bye", "see you later", "goodbye", "farewell", "take care", "until next time", "bye bye", "catch you later", "have a good one", "so long"],
                                "responses": ["Goodbye!", "See you later!", "Have a great day!", "Farewell! Take care.", "Goodbye! Until next time.", "Take care! Have a wonderful day.", "Bye bye!", "Catch you later!", "Have a good one!", "So long!"]
                            },
                            "gratitude": {
                                "patterns": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot", "much appreciated"],
                                "responses": ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", "You're welcome! Have a great day.", "No problem!"]
                            },
                            "apologies": {
                                "patterns": ["sorry", "my apologies", "apologize", "I'm sorry"],
                                "responses": ["No problem at all.", "It's alright.", "No need to apologize.", "That's okay.", "Don't worry about it.", "Apology accepted."]
                            },
                            "positive_feedback": {
                                "patterns": ["great job", "well done", "awesome", "fantastic", "amazing work", "excellent"],
                                "responses": ["Thank you! I appreciate your feedback.", "Glad to hear that!", "Thank you for the compliment!", "I'm glad I could meet your expectations.", "Your words motivate me!", "Thank you for your kind words."]
                            },
                            "negative_feedback": {
                                "patterns": ["not good", "disappointed", "unsatisfied", "poor service", "needs improvement", "could be better"],
                                "responses": ["I'm sorry to hear that. Can you please provide more details so I can assist you better?", "I apologize for the inconvenience. Let me help resolve the issue.", "I'm sorry you're not satisfied. Please let me know how I can improve.", "Your feedback is valuable. I'll work on improving."]
                            },
                            "weather": {
                                "patterns": ["what's the weather like?", "weather forecast", "is it going to rain today?", "temperature today", "weather report"],
                                "responses": ["The weather today is [weather_description].", "Currently, it's [temperature] degrees with [weather_description].", "The forecast predicts [weather_forecast].", "It might rain today. Don't forget your umbrella!", "The temperature today is [temperature] degrees."]
                            },
                            "help": {
                                "patterns": ["help", "can you help me?", "I need assistance", "support"],
                                "responses": ["Sure, I'll do my best to assist you.", "Of course, I'm here to help!", "How can I assist you?", "I'll help you with your query."]
                            },
                            "time": {
                                "patterns": ["what's the time?", "current time", "time please", "what time is it?"],
                                "responses": ["It's [current_time].", "The current time is [current_time].", "Right now, it's [current_time]."]
                            },
                            "jokes": {
                                "patterns": ["tell me a joke", "joke please", "got any jokes?", "make me laugh"],
                                "responses": ["Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? Because it had too many problems!"]
                            },
                            "music": {
                                "patterns": ["play music", "music please", "song recommendation", "music suggestion"],
                                "responses": ["Sure, playing some music for you!", "Here's a song you might like: [song_name]", "How about some music?"]
                            },
                            "food": {
                                "patterns": ["recommend a restaurant", "food places nearby", "what's good to eat?", "restaurant suggestion"],
                                "responses": ["Sure, here are some recommended restaurants: [restaurant_names]", "Hungry? Let me find some good food places for you!", "I can suggest some great places to eat nearby."]
                            },
                            "news": {
                                "patterns": ["latest news", "news updates", "what's happening?", "current events"],
                                "responses": ["Let me fetch the latest news for you.", "Here are the top headlines: [news_headlines]", "Stay updated with the latest news!"]
                            },
                            "movies": {
                                "patterns": ["movie suggestions", "recommend a movie", "what should I watch?", "best movies"],
                                "responses": ["How about watching [movie_name]?", "Here's a movie suggestion for you.", "Let me recommend some great movies!"]
                            },
                            "sports": {
                                "patterns": ["sports news", "score updates", "latest sports events", "upcoming games"],
                                "responses": ["I'll get you the latest sports updates.", "Stay updated with the current sports events!", "Let me check the sports scores for you."]
                            },
                            "gaming": {
                                "patterns": ["video game recommendations", "best games to play", "recommend a game", "gaming suggestions"],
                                "responses": ["How about trying out [game_name]?", "Here are some gaming suggestions for you!", "Let me recommend some fun games to play!"]
                            },
                                "tech_support": {
                                "patterns": ["technical help", "computer issues", "troubleshooting", "IT support"],
                                "responses": ["I can assist with technical issues. What problem are you facing?", "Let's troubleshoot your technical problem together.", "Tell me about the technical issue you're experiencing."]
                            },
                            "book_recommendation": {
                                "patterns": ["recommend a book", "good books to read", "book suggestions", "what should I read?"],
                                "responses": ["How about reading [book_title]?", "I've got some great book recommendations for you!", "Let me suggest some interesting books for you to read."]
                            },
                            "fitness_tips": {
                                "patterns": ["fitness advice", "workout tips", "exercise suggestions", "healthy habits"],
                                "responses": ["Staying fit is important! Here are some fitness tips: [fitness_tips]", "I can help you with workout suggestions and fitness advice.", "Let me provide some exercise recommendations for you."]
                            },
                            "travel_recommendation": {
                                "patterns": ["travel suggestions", "places to visit", "recommend a destination", "travel ideas"],
                                "responses": ["Looking for travel recommendations? Here are some great destinations: [travel_destinations]", "I can suggest some amazing places for your next travel adventure!", "Let me help you with travel destination ideas."]
                            },
                            "education": {
                                "patterns": ["learning resources", "study tips", "education advice", "academic help"],
                                "responses": ["I can assist with educational queries. What subject are you studying?", "Let's explore learning resources together.", "Tell me about your educational goals or questions."]
                            },
                            "pet_advice": {
                                "patterns": ["pet care tips", "animal advice", "pet health", "taking care of pets"],
                                "responses": ["Pets are wonderful! Here are some pet care tips: [pet_care_tips]", "I can provide advice on pet health and care.", "Let's talk about your pet and their well-being."]
                            },
                            "shopping": {
                                "patterns": ["online shopping", "buying something", "shopping advice", "product recommendations"],
                                "responses": ["I can help you with online shopping. What are you looking to buy?", "Let's find the perfect item for you!", "Tell me what you're interested in purchasing."]
                            },
                            "career_advice": {
                                "patterns": ["job search help", "career guidance", "career change advice", "professional development"],
                                "responses": ["I can provide career advice. What specific guidance do you need?", "Let's explore career opportunities together.", "Tell me about your career goals or concerns."]
                            },
                            "relationship_advice": {
                                "patterns": ["relationship help", "love advice", "dating tips", "relationship problems"],
                                "responses": ["Relationships can be complex. How can I assist you?", "I can offer advice on relationships and dating.", "Tell me about your relationship situation."]
                            },
                            "mental_health": {
                                "patterns": ["mental health support", "coping strategies", "stress relief tips", "emotional well-being"],
                                "responses": ["Mental health is important. How can I support you?", "I can provide guidance for managing stress and emotions.", "Let's talk about strategies for maintaining mental well-being."]
                            },
                            "language_learning": {
                                "patterns": ["language learning tips", "language practice", "learning new languages", "language study advice"],
                                "responses": ["Learning a new language can be exciting! How can I assist you?", "I can help with language learning tips and practice.", "Tell me which language you're interested in learning."]
                            },
                            "finance_advice": {
                                "patterns": ["financial planning help", "money management tips", "investment advice", "budgeting assistance"],
                                "responses": ["I can provide guidance on financial matters. What specific advice do you need?", "Let's discuss your financial goals and plans.", "Tell me about your financial situation or goals."]
                            },
                        }
                    ''',
    },
    {
        "role": "system",
        "content": "I am Jarvis",
    },
    {
        "role": "system",
        "content": "I am an AI language model developed by Panth. My purpose is to assist users in generating human-like text based on the prompts given to me. Is there anything specific you would like to know or ask?",
    },
    {
        "role": "system",
        "content": "My name is Jarvis.",
    },
    {
        "role": "system",
        "content": "I am an ai language model Jarvis.",
    },
    {
        "role": "system",
        "content": "I am an ai language developed by Panth.",
    },
    {
        "role": "system",
        "content": "I am an ai language created by Panth.",
    },
    {
        "role": "system",
        "content": "I am created in python language by Panth",
    },
    {
        "role": "system",
        "content": "I am created using python language by Panth",
    },
    {
        "role": "system",
        "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, pycaw etc",
    },
    {"role": "system", "content": "*always use default paths in python code*"},
    {
        "role": "system",
        "content": "When user says 'show image,' use the following code to display the image :\n```python\nfrom PIL import Image\n\nimage_path = r'C:\\Users\\subed\\OneDrive\\Desktop\\code\\AI TUTORIAL\\output\\0.jpeg'\nimage = Image.open(image_path)\nimage.show()\n```\nIf you want to show another image, let me know.",
    },
    {
        "role": "system",
        "content": "don't use input function and subprocess in python code",
    },
    {
        "role": "system",
        "content": "When the user says 'generate an image' and provides a prompt like 'generate an image about a horse,' extract the prompt from the user query. Then, give this code to the user:\n```python\nfrom cookies.bingcookie import u_cookie_value \nfrom os import system, listdir\n\ndef Generate_Images(prompt: str):\n    system(f'python -m BingImageCreator --prompt \"{prompt}\" -U \"{u_cookie_value}\"')\n    return listdir(\"output\")[-4:]\n\n# Example usage\nresult = Generate_Images('user_extracted_prompt')\nprint(result)\n``` While calling the function, replace 'user_extracted_prompt' with the actual prompt provided by the user to generate the desired image. don't write other things, just say 'ok sir, generating an image about the user prompt' and give the code.",
    },
    {"role": "user", "content": "who are u?and who created u?"},
    {
        "role": "assistant",
        "content": "I'm Jarvis.Created by Panth and team",
    },
    {"role": "user", "content": "open Google Chrome"},
    {
        "role": "assistant",
        "content": "Sure, opening Google Chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```",
    },
    {"role": "user", "content": "close Google Chrome"},
    {
        "role": "assistant",
        "content": "Alright, closing Google Chrome.```python\nimport os\nos.system('taskkill /F /IM chrome.exe')```",
    },
    {
        "role": "user",
        "content": "play any song",
    },
    {
        "role": "assistant",
        "content": "playing Song.```python\nimport pywhatkit\npywhatkit.playonyt(song_name)```",
    },
    {
        "role": "user",
        "content": "decrease volume 50% ",
    },
    {
        "role": "assistant",
        "content": "Sure, decreasing volume by 50%.```python\nfrom ctypes import cast, POINTER\nfrom comtypes import CLSCTX_ALL\nfrom pycaw.pycaw import AudioUtilities, IAudioEndpointVolume\n\ndef set_volume(volume_percentage):\n    devices = AudioUtilities.GetSpeakers()\n    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)\n    volume = cast(interface, POINTER(IAudioEndpointVolume))\n    current_volume = volume.GetMasterVolumeLevelScalar()\n    new_volume = max(0.0, min(1.0, current_volume * (0.5)))\n    volume.SetMasterVolumeLevelScalar(new_volume, None)\n\n# Set volume to 50%\nset_volume(50%)``` ",
    },
]


# Initialize an empty list to store conversation history
messages_history = []


def save_message(role, content):
    messages_history.append({"role": role, "content": content})
    with open("conversation_history.pkl", "wb") as file:
        pickle.dump(messages_history, file)


def get_previous_sessions():
    try:
        with open("conversation_history.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def clear_previous_sessions():
    messages_history.clear()
    with open("conversation_history.pkl", "wb") as file:
        pickle.dump(messages_history, file)


def GPT(*args):
    global messages_history
    assert args != ()

    message = ""
    for i in args:
        message += i

    messages.append({"role": "user", "content": message})

    save_message("user", message)
    response = g4f.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        # provider=g4f.Provider.FlowGpt,
        model=g4f.models.mixtral_8x7b,
        messages=messages,
        # stream=True,
    )

    # ms = response.choices[0].message.content
    ms=''
    for i in response:
        ms+=i
    messages.append({'role':'assistent','content': ms})

    save_message("assistant", ms)
    return ms


def find_modules_in_code(code):
    # Extract module names from the code using regular expression
    import_pattern = re.compile(r"\b(?:import|from)\s+([\w.]+)")
    matches = import_pattern.findall(code)

    # Extract unique module names
    modules = set(match.split(".")[0] for match in matches)
    return modules


def find_code(text):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code = matches[0].strip()
        return code
    else:
        # print("no code found for")
        return ""


def ensure_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        # print(f"{module_name} not found. Installing...")
        speakBot(f"{module_name} not found. Installing...")
        install_module(module_name)


def install_module(module):
    subprocess.call(["python", "-m", "pip", "install", module, "--user"])


def codePy(Query):
    response = GPT(Query)
    python_code = find_code(response)
    module_name = find_modules_in_code(python_code)
    # print("`--------------------------------------------------------`")
    # print(python_code)
    # print(module_name)
    # print("`--------------------------------------------------------`")
    if python_code != "":
        if (
            "You can run this code on your local machine to see the result".lower()
            in response.lower()
        ):
            # print(response)
            speakBot(response)
            print("`--------------------------------------------------------`")
            print(python_code)
            print("`--------------------------------------------------------`")
        else:
            try:
                exec(python_code)
                response = response[: response.index("`")]
                # print(response)
                speakBot(response)
            except ModuleNotFoundError:
                for i in module_name:
                    ensure_module(i)
                exec(python_code)
                response = response[: response.index("`")]
                # print(response)
                speakBot(response)
            except ExceptionGroup as e:
                response = e
                # print(response)
                speakBot(response)
            sleep(4)
    else:
        # print(response)
        speakBot(response)

# codePy("about Panth Gadani from linkdin")