n=int(input("Saisissez un entier supérieur à 0 : "))
if (n) > 0:
    print("Table de multiplication de", (n), ":")
    for x in range(1, 11):
        print((n), "x", (x), "=", (n*x))
else:
    print("Utilisez un entier supérieur à 0 !")