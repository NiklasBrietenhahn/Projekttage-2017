while True:
    print('hallo,das ist ein Vervielfacher')
    zahl = int(input('bitte geben sie eine zahl ein: '))
    for i in range(1,11,1):
        ergebnis = [i * zahl]
        print(ergebnis)

    erneut = (input('wollen sie noch einmal(yes/no): '))
    if erneut != 'yes':
        break
    else:
        print('__________________________________________________________________')
