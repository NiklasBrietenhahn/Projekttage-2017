

    
    
 print ('Bitte alle angaben in Zahlenform (zb.5)')
jahr = int(input('in welchen jahr bist du geboren: '))
alter = 2017 - jahr
monat = int(input('in welchen monat bist du geboren: '))
tag = int(input('an welchen tag bist du geboren: '))
if tag == 19 and monat == 7:
     print('Herzlichen Glückwunsch zum Geburtstag du bist' , alter, 'jahre alt')
 if monat < 19:
         print ('du bist' , alter - 1 , 'jahre alt und du hast heute keinen Geburtstag')
if monat > 19:
    print('du bist' , alter , 'jahre alt und du hast heute keinen Geburtstag')
    
