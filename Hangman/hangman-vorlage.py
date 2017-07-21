print('wilkommen bei Hangman')

from hangman_renderer import render_hangman


def convert_upper_case(string):
    if "ß" in string:
        chars = []
        for char in string:
            if char == "ß":
                chars.append("ß")
            else:
                chars.append(char.upper())
        return "".join(chars)
    else:
        return string.upper()


def spielmodus_fragen():
    try:
        spielmodus = input('wollen sie alleine oder mit einem Freund spielen(singleplayer/multiplayer): ')
        if spielmodus == 'singleplayer':
            worte = ["schmetterling", "schokokuchen", "kuhmist", "faupax", "rhythmus", "Rhesusfaktor", "Physiognomie", "Jazz", "Fahrradkette", "Steppe" ]

            import random
            return worte[random.randint(0, len(worte) - 1)]     # diese zwei Zeilen sorgen für die zufällige Auswahl

        else:
            while True: 
                eigeneswort = input('bitten sie einen Partner ein Wort einzugeben : ')  
                    
                if eigeneswort.isalpha() :
                    print('gültiges Wort')
                    return eigeneswort
                    
                else:
                    print('eingabe ungültig')
    except:
        print('ungültige eingabe')


def zeichne_spiel():
    global falsche_buchstaben, meldung, erratenes_wort, fehlversuche

    print("\n" * 100)       # 100 leere Zeilen, damit der Bildschirm "leer" ist

    render_hangman(fehlversuche)    # zeichnet den Hangman abhängig der bisherigen Fehlversuche

    
    print(convert_upper_case(", ".join(falsche_buchstaben)))

    print(convert_upper_case(" ".join(erratenes_wort)))


def rate_buchstabe():
    global übrige_buchstaben, meldung

    buchstabe = input('raten sie einen Buchstaben: ').lower()
    if len(buchstabe) != 1:
        return False
    if buchstabe.lower() not in list("abcdefghijklmnopqrstuvwxyzäöüß"):
        return False

    elif buchstabe not in übrige_buchstaben:
        return False

    
    return buchstabe.lower()

def eingabe_auswerten(buchstabe):
    global fehlversuche, falsche_buchstaben, übrige_buchstaben, meldung, wort, erratenes_wort

    if buchstabe in wort:
        for i in range (len(wort)):

            if wort[i] == buchstabe:
                erratenes_wort [i] = buchstabe
    else:
        fehlversuche += 1
        falsche_buchstaben.append(buchstabe)
    übrige_buchstaben.remove(buchstabe)

    
    if "_" not in erratenes_wort:
        meldung = 'du hast gewonnen'
        return True

    if fehlversuche == 6:
        meldung = 'du hast verlohren'
        
        return True
    return False

print("\n" * 100)
print("=== H A N G M A N ===\n\n\n")

while True:

    
    fehlversuche = 0       # Anzahl der Fehlversuche auf null setzen

    falsche_buchstaben = []   # falsche Buchstaben als leere Liste setzen

    übrige_buchstaben = list("abcdefghijklmnopqrstuvwxyzäöüß")      # erzeugt eine Liste mit allen Buchstaben

    meldung = ''              # Meldung zu einer leeren Zeichenkette setzen
    wort = spielmodus_fragen ()

                    # Funktion spielmodus_fragen() aufrufen um Wort zu erhalten, Wort in Kleinbuchstaben konvertieren

    erratenes_wort = ["_"] * len(wort)      # erzeugt eine Liste mit so vielen "_" wie das Wort lang ist
    
    while True:

        zeichne_spiel()

        buchstabe = rate_buchstabe()

        if not buchstabe:
            continue

        else:
            if eingabe_auswerten (buchstabe):
                break
            
    zeichne_spiel()

    print("\n\n")
    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
