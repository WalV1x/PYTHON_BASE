import random

round = int(input("Combien de manches voulez-vous faire ? "))

computerScore = 0
playerScore = 0

options = ["pierre", "papier", "ciseau"]

while playerScore < round and computerScore < round:
    playerChoice = input("Choisissez votre coup : ")

    while playerChoice not in options:
        input("Choisissez entre les options pierre, papier ou ciseau:\n")

    computerChoice = random.choice(options)

    if playerChoice == computerChoice:
        print("Vous faites égalité")
    elif playerChoice == "pierre" and computerChoice == "ciseau" \
            or playerChoice == "papier" and computerChoice == "pierre" \
            or playerChoice == "ciseau" and computerChoice == "papier":
        print("Vous avez gagné cette manche, car", playerChoice, "bat", computerChoice)
        playerScore += 1
    else:
        print("L'ordinateur a gagné, car", computerChoice, "bat", playerChoice)
        computerScore += 1

if playerScore > round:
    print("Vous avez gagné")
else:
    print("L'ordinateur a gagné :(")

print("\nJoueur :", playerScore, "contre ordinateur : ", computerScore)