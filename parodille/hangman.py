from time import sleep as wait
from random import choice as rand_choice


def avstand(antall: int) -> str: # Function annotation kan du lese om her: https://www.python.org/dev/peps/pep-3107/
    return " " * antall


def gjett_bokstav() -> str:  # Returnerer en gjettet bokstav om den følger kriteriene.
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

    bokstav_gjettet = input("\nGjett en bokstav: ").upper()

    # hvis gjetting allerede er i hemmelig ord printes dette
    if bokstav_gjettet in gjettede_bokstaver:
        print(f"  \"{bokstav_gjettet}\" Har allerede blitt valgt, velg en annen bokstav.")
    elif len(bokstav_gjettet) != 1:
        print(f"  Du kan bare skrive en bokstav om gangen.")
    elif bokstav_gjettet not in alfabet:
        print(f"  \"{bokstav_gjettet}\" Er ikke en bokstav, du kan kun velge bokstaver.")
    else:
        gjettede_bokstaver.append(bokstav_gjettet)  # legger inn gjetting i gjettede bokstaver.
        return bokstav_gjettet


def galgen(antall_feil: int) -> bool:
    if antall_feil <= 6:
        print(galge[antall_feil])  # Printer galgen etter hvor mange feil brukeren har.
        return False
    else:
        print(galge[antall_feil])
        print(f"\n{avstand(18)}Du har tapt. Ordet var {hemmelig_ord}")
        #  slutter while løkka hvis dette er sant
        return True


def seier(riktige_bokstaver: list, hemmelige_ordet: list) -> bool:
    riktige_bokstaver_len = len(riktige_bokstaver)
    hemmelig_ord_len = len(hemmelige_ordet)

    print(f"riktige: {riktige_bokstaver_len}\nOrd lengde: {hemmelig_ord_len}")
    # Viser at brukeren har vunnet
    if riktige_bokstaver_len == hemmelig_ord_len:
        print(galge[8])  # printer ut vinner bilde
        # slutter while løkka hvis dette er feil
        return True


"""Dette programmet er spillet hangman. Så det tar et tilfeldig ord og
spilleren/personen som leser dette programmet får
 7 sjanser til å gjette ordet."""
# tar med denne "grafikken for å gjøre det mer spennende"
galge = ['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\\    |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\\    |
                |     |
               / \\   _|_''', '''

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆

                    \\O/
          ~VINNER~   |   ~VINNER~
                     |
                    / \\

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']

# importerer en laget ordliste fra dokumenter
with open('ordliste.txt', encoding="utf8") as fil:
    ordliste = fil.readlines()

hemmelig_ord = rand_choice(ordliste).upper().strip()  # Hent hemmelig ord fra ordliste

# Spør om navn for å være hyggelig
navn = input("Hva heter du? ").capitalize()

# En koselig innledning
print(f"Hei {navn}, vi skal spille hangman.")
wait(2)  # Vent 2 sekunder før programmet går videre

# Tekststrenger start å gjette kommer opp
print("Start å gjette...")

blanks = '-' * len(hemmelig_ord)  # Printer - for hver bokstav av lengden i hemmelig ord

feil = 0
riktige = []

gjettede_bokstaver = []

while True:
    for index, hemmelig_bokstav in enumerate(hemmelig_ord):  # Lager en index og iterer over bokstavene
        if hemmelig_bokstav in gjettede_bokstaver:
            # Printer ut en - for hver bokstav i hemmelig_ord variabelen
            blanks = blanks[:index] + hemmelig_ord[index] + blanks[index + 1:]
            if hemmelig_ord.count(hemmelig_bokstav) != riktige.count(
                    hemmelig_bokstav):  # Sjekker om det er mange nok bokstaver i programmet
                riktige.append(hemmelig_bokstav)
            print("\n" * 7)  # Får 7 linjeskift.

    if galgen(feil):  # Returnerer "True" om spilleren har for mange feil.
        break

    if seier(riktige, hemmelig_ord):  # Returnerer "True" om spilleren gjetter hele ordet.
        break

    print(f"\n{avstand(16)}{blanks}\n")
    if len(gjettede_bokstaver) > 0:
        print(f"Gjettede bokstaver: {', '.join(gjettede_bokstaver)}")

    hent_gjetting = gjett_bokstav()
    if hent_gjetting and hent_gjetting not in hemmelig_ord:
        feil += 1  # Sporer antall feil spilleren tar.
