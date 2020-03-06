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


# def compare_strings(first_string, secound_string):
#     correct_guesses = []
#     for letter_one, letter_two in zip(first_string, secound_string):
#         if letter_one == letter_two:
#             correct_guesses.append(letter_one)
#     return correct_guesses


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
    print(f"Your random word is {hangman_word}")
    guess = get_lower("Guess a letter or word: ")

    word_set = {}  # contains a set of uniqe letters https://docs.python.org/3.8/library/stdtypes.html#set
    print(word_set)
