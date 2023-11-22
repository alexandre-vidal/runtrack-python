x = input('Tapez un mot avec la lettre "e" : ')

x = str(x)

index = x.find('e')

if index !=-1:
    print("Yes")
else:
    print('No')