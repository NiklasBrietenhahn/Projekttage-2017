while True:
    print('dies ist ein Addierer! ')
    zahl1 = int(input('zahl 1: '))
    zahl2 = int(input('zahl 2 : '))
    ergebnis = 0
    if zahl1 > 0:
        i = 0
        while i < zahl1:
            ergebnis += 1
            i += 1
    elif zahl1 < 0:    
        i = 0
        while i > zahl1:
            ergebnis -= 1
            i -= 1

    if zahl2 > 0:
        i = 0
        while i < zahl2:
            ergebnis -= 1
            i -= 1
    print ('ergebnis: ', ergebnis ,)
