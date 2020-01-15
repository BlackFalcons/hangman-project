from platform import system as currentplatform
from os.path import isfile
from requests import get
from time import sleep
from os import system as command
from random import choice as get_random


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
    hangman_word = open("./ordliste.txt", encoding="utf8").readlines()
    print(f"Your random word is {get_random(hangman_word)}")
