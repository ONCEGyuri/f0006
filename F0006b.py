elso = int(input('Mi az első szám? '))
masodik = int(input('Mi a második szám? '))
if elso > masodik:
    amitkiir = 'A ' + str(elso) + ' a nagyobb!'
elif elso == masodik:
    amitkiir = 'Egyenlő a két szám értéke.'
else:
    amitkiir = 'A ' + str(masodik) + ' a nagyobb!'
print(amitkiir)