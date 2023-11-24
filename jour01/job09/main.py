nom = "Jus d'orange"
prix = 5
stock = 60

print("Stock actuel :")
print(nom)
print(prix)
print(stock)

stock = stock + 5

print("Mise à jour du stock :")
print(stock)

x = input("Combien de produits souhaitez-vous acheter ? : ")

x = int(x)

stock = stock - x

prix = prix + (prix*10/100)

print("Mise à jour du stock :")
print(nom)
print(prix)
print(stock)