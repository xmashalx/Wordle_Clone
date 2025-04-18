import pyinputplus as pyip
import pathlib
import random 
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=40)

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")


def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def get_user_guess():
    guess = pyip.inputStr(
    prompt='Enter a five-letter word: ',
    allowRegexes=[r'^[A-Za-z]{5}$'],
    blockRegexes=[r'.*'])  # Block everything not explicitly allowed
    return guess.upper()

def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


def main():
    print("Welcome to Wyrdle!")
    print("You have 6 attempts to guess the word.")
    print("The word is 5 letters long.")
    print("you guess a word and I will tell you which letters are correct, misplaced, or wrong.")
    print("Correct letters are in the correct position.")
    print("Misplaced letters are in the word but in the wrong position.")
    print("Wrong letters are not in the word.")
    print("Good luck!")

    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    WORD = get_random_word(words_path.read_text(encoding="utf-8").split("\n"))


    for i in range(1,7):
        print(f'Attempt {i} of 6')
        guess=get_user_guess()
        if guess==WORD:
            print("Correct")
            break
        show_guess(guess, WORD)

    else:
        print("You have used all your attempts.")
        print(f"The word was {WORD}")
