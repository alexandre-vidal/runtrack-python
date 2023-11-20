montant = 5000
rendement = 15
gain = (montant*rendement) / 100
print("Montant initial :")
print(montant)
print("Rendement initial :")
print(rendement)
print("Gain initial :")
print(gain)

montant = (montant + 5000)
rendement = (rendement + 2)
gain = (montant*rendement)
print("Montant après augmentation du capital :")
print(montant)
print("Rendement après augmentation du capital :")
print(rendement)
print("Gain après augmentation du capital :")
print(gain)

montant = montant - (montant*10/100)
rendement = (rendement - 1)
print("Montant final :")
print(montant)
print("Rendement final :")
print(rendement)
print("Gain final :")
print(gain)