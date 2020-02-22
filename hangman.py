from platform import system as currentplatform
from os.path import isfile
from requests import get
from time import sleep
from os import system as command
from random import choice as get_random


def get_lower(prompt):
    return input(prompt).lower()


def download_file(url, filename):
    file = get(url)
    open(filename, "wb").write(file.content)


def clear_screen():
    if currentplatform() == "Windows":
        command("cls")
    else:
        command("clear")


if not isfile("ordliste.txt"):
    print("File not found, downloading...")
    fileLocation = "https://raw.githubusercontent.com/0301/ordliste/master/ordliste_snl_fellesord.txt"
    download_file(fileLocation, "./ordliste.txt")

    clear_screen()
    print("Download complete!")
    sleep(2)

# Hangman kode starter her, dette er etter vi har lastet ned filen.
if isfile("ordliste.txt"):
    clear_screen()

    print("Welcome to hangman!\n")
    word_list = open("./ordliste.txt", encoding="utf8").readlines()
    hangman_word = get_random(word_list)

    while len(hangman_word) < 3:
        hangman_word = get_random(word_list)

    print(f"Your random word is {hangman_word}")
    while True:
        guess = get_lower("\nGuess a letter or word: ")
        if hangman_word == guess:
            print(f"You guessed the correct word which was {hangman_word}")
            break
        else:
            for character in guess:
                if character in hangman_word:
                    print(character, end='')
                else:
                    print("_", end='')