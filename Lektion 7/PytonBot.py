print('Hallo ich bin PytonBot')
while True:
    MONAT = ['0','Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
    name = input('gib deinen Namen ein: ')
    print('Wilkommen', name ,)
    print ('Bitte alle angaben in Zahlenform (zb.5)')
    jahr = int(input('in welchen jahr bist du geboren: '))
    alter = 2017 - jahr
    monat = input('Monat bitte in Wortform (ZB. Januar) : ')
    monat = MONAT.index(monat)
    tag = int(input('an welchen tag bist du geboren(wieder in zahlenform): '))
    if tag == 20 and monat == 7:
        print('Herzlichen Glückwunsch zum Geburtstag du bist' , alter, 'jahre alt')
    if monat < 7:
            print ('du bist' , alter - 2 , 'jahre alt und du hast heute keinen Geburtstag')
    if monat > 7:
        print('du bist' , alter - 1, 'jahre alt und du hast heute keinen Geburtstag')
    fortfahren = input('drücke f um fortzufahren :')
    if fortfahren == 'f':
        print('------------------------------------------------------------')
    else:
        break
    antwort = input('willst du einmal? (yes/no)')
    if antwort == 'yes' or antwort == 'y':
        print('###########################################################')
    else:
        print('sie haben beendet')
    break
while True:
    print('hallo',name,'nun kannst du eine zahlenreihe herausfinden')
    zahl = int(input('bitte geben sie eine zahl ein: '))
    for i in range(1,11,1):
        ergebnis = [i * zahl]
        print(ergebnis)

    erneut = (input('willst du noch einmal(yes/no): '))
    if erneut != 'yes':
        break
    else:
        print('__________________________________________________________________')

print('nun kommt ein Quiz')
Eisbären = (input('leben die eisbären auf der Arktis oder Antarktis ?: '
if Eisbären == Arktis
                  print('richtig')
