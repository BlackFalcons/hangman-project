from time import sleep as wait
from random import choice as rand_choice


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


def gjett_bokstav():  # Returns a valid guessing value
    # lager en definisjon på ordgjetting slik at spilleren kan gjøre feil, men programmet vil ikke påvirkers.

    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

    print(f"\n{hemmelig_ord}")
    bokstav_gjettet = input("Gjett en bokstav: ")

    bokstav_gjettet = bokstav_gjettet.upper()  # slik at man får store bokstaver uavhengig av hva spiller taster

    print()  # et lite mellomrom

    # hvis gjetting allerede er i hemmelig ord printes dette
    if bokstav_gjettet in gjettede_bokstaver:
        print(f"   {bokstav_gjettet}  Har allerede blitt valgt, velg en annen bokstav")
    elif len(bokstav_gjettet) != 1:
        print(f"  Du kan bare skrive en bokstav om gangen")
    elif bokstav_gjettet not in alfabet:
        print(f"  {bokstav_gjettet}  Er ikke en bokstav, du kan bare velge bokstaver")
    else:
        gjettede_bokstaver.append(bokstav_gjettet)  # legger inn gjetting i gjettede bokstaver.
        return bokstav_gjettet


# importerer en laget ordliste fra dokumenter
with open('ordliste.txt') as fil:
    ordliste = fil.readlines()

gjettede_bokstaver = []
tilfeldig = rand_choice(ordliste)  # det blir trukket ut et tilfeldig ord fra ordlisten hver gang programmet kjøres.

# spør om navn for å være hyggelig
navn = input("Hva heter du? ").capitalize()

# en koselig innledning
print(f"Hei {navn}, vi skal spille hangman.")
wait(2)  # Vent 2 sekunder før programmet går videre


# tekststrenger start å gjette kommer opp
print("Start å gjette...")

hemmelig_ord = tilfeldig.upper().strip()
#  .strip() Fjerner mellomrom
#  .upper() slik at det ikke spiller noen rolle om spilleren bruker store eller små bokstaver. Får alt i store bokstaver, det ser kult ut.


blanks = '-' * len(hemmelig_ord)  # printer - for hver bokstav av lengden i hemmelig ord
feil = -1
riktige = []
running = True

while running:
    for index, hemmelig_bokstav in enumerate(hemmelig_ord):  # i er en variabel
        if hemmelig_bokstav in gjettede_bokstaver:
            blanks = blanks[:index] + hemmelig_ord[index] + blanks[index + 1:]
            # blanks = -, så printes ut en - for hver bokstav i hemmelig ord
            print(riktige)
            if hemmelig_ord.count(hemmelig_bokstav) != riktige.count(hemmelig_bokstav):
                riktige.append(hemmelig_bokstav)
            print("\n" * 7)  # får 7 linjeskift.

    if feil < 6:
        print(galge[feil + 1])  # Printer galgen, bygger på mer på galgen etter hver feil.
    else:
        print(galge[feil + 1])
        print(f"\n                  Du har tapt. Ordet var {hemmelig_ord}")  # printer dette etter all feilen.
        #  slutter while løkka hvis dette er sant
        running = False
        break
    print(f"riktige: {len(riktige)}\nOrd lengde: {len(hemmelig_ord)}")
    # Viser at brukeren har vunnet
    if len(riktige) == len(hemmelig_ord):
        print(galge[8])  # printer ut vinner bilde
        # slutter while løkka hvis dette er feil
        running = False
        break

    print("\n               " + blanks + "")
    print("\n\n         ", end='  ')

    for bokstav in gjettede_bokstaver:
        # for hver verdi i gjettede_bokstaver printer den hver verdi i listen
        print("", end='')
        print(bokstav, end='')

    hent_gjetting = gjett_bokstav()  # lager en ny variabel som henter gjettingen
    if hent_gjetting and hent_gjetting not in hemmelig_ord:  # hvis gjetting ikke er i ordet
        feil += 1  # blir et plusset på en feil
