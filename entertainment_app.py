import requests
import PySimpleGUI as sg
import random

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    joke = response.json().get("joke")
    return joke

def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    quote = response.json()[0]
    return f"{quote['q']} - {quote['a']}"

def get_trivia():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url)
    trivia = response.json()["results"][0]
    question = trivia["question"]
    correct_answer = trivia["correct_answer"]
    options = trivia["incorrect_answers"] + [correct_answer]
    random.shuffle(options)
    return question, correct_answer, options

def number_guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    while guess != number:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")

# Define the layout
layout = [
    [sg.Text("Welcome to the Entertainment App")],
    [sg.Button("Get a Joke"), sg.Button("Get a Quote"), sg.Button("Get Trivia"), sg.Button("Play a Game")],
    [sg.Multiline(size=(60, 20), key="output")],
    [sg.Button("Exit")]
]

# Create the window
window = sg.Window("Entertainment App", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Get a Joke":
        joke = get_joke()
        window["output"].update(joke)
    elif event == "Get a Quote":
        quote = get_quote()
        window["output"].update(quote)
    elif event == "Get Trivia":
        question, correct_answer, options = get_trivia()
        trivia_text = f"Question: {question}\nOptions: {', '.join(options)}\nAnswer: {correct_answer}"
        window["output"].update(trivia_text)
    elif event == "Play a Game":
        window.hide()
        number_guessing_game()
        window.un_hide()

# Close the window
window.close()
