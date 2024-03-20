import random
prix = random.randint(1, 10)

essai = 0
score = 100

print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus")

while True:
    nombre = int(input())
    essai += 1
    if nombre < prix:
        print("Le juste prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print("Félicitations, vous avez trouvé le juste prix de {} en {} essais, cotre score est de {} !".format(prix, essai, score / essai))
        break

print("Partie terminée")