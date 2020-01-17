from platform import system as currentplatform
from os.path import isfile
from requests import get
from time import sleep
from os import system as command
from random import choice as get_random


def getLower(prompt):
    return input(prompt).lower()


def downloadFile(url, filename):
    file = get(url)
    open(filename, "wb").write(file.content)


def clearScreen():
    if currentplatform() == "Windows":
        command("cls")
    else:
        command("clear")


if not isfile("ordliste.txt"):
    print("File not found, downloading...")
    fileLocation = "https://raw.githubusercontent.com/0301/ordliste/master/ordliste_snl_fellesord.txt"
    downloadFile(fileLocation, "./ordliste.txt")
    clearScreen()
    print("Download complete!")
    sleep(2)

# Hangman kode starter her, dette er etter vi har lastet ned filen.
if isfile("ordliste.txt"):
    clearScreen()
    print("Welcome to hangman!\n")
    word_list = open("./ordliste.txt", encoding="utf8").readlines()
    hangman_word = get_random(word_list)
    print(f"Your random word is {hangman_word}")
    guess = getLower("Guess a letter or word: ")
    correct_guesses = []

    # Disassemble the person guess and the hangman word.
    for guess_letter in guess:
        for word_letter in hangman_word:
            if guess_letter == word_letter:
                correct_guesses.append(guess_letter)
                print(guess_letter)

    # Assemble the person guess and the hangman word.
