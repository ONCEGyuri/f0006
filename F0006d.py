helyezese = int(input('Hanyadik helyet érted el? '))
if helyezese > 3:
    print('Nem vagy dobogós!')
elif helyezese == 3:
    print('Bronzérmet kaptál!')
elif helyezese == 2:
    print('Ezüstérmet kaptál!')
elif helyezese == 1:
    print('Aranyérmet kaptál!')