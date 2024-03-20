import os


def ShowTray(t, player):  # Afficher le tableau
    print(" " + t[0] + "|" + t[1] + "|" + t[2] + " ")
    print("---+---+---")
    print(" " + t[3] + "|" + t[4] + "|" + t[5] + " ")
    print("---+---+---")
    print(" " + t[6] + "|" + t[7] + "|" + t[8] + " ")
    print("C'est au tour du joueur", player)


Tray = [" " for _ in range(9)]  # crée un tableau de 9 caractères


def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def Morpion():
    player = "X"
    Round = 0

    while True:  # 9 Rounds maximum avant la fin
        ClearConsole()
        print("> Tour du joueur {}. Entrez un nombre de 1 et 9!".format(player))
        ShowTray(Tray, player)

        move = int(input()) - 1

        # Vérifier les cases disponibles
        if Tray[move] == " ":
            Tray[move] = player
            Round += 1
        else:
            print("Case indisponible, choisissez-en une autre")
            continue

        # Les différentes manières de gagner
        if Tray[0] == Tray[1] == Tray[2] != " " \
                or Tray[3] == Tray[4] == Tray[5] != " " \
                or Tray[6] == Tray[7] == Tray[8] != " " \
                or Tray[0] == Tray[3] == Tray[6] != " " \
                or Tray[1] == Tray[4] == Tray[7] != " " \
                or Tray[2] == Tray[5] == Tray[8] != " " \
                or Tray[0] == Tray[4] == Tray[8] != " " \
                or Tray[2] == Tray[4] == Tray[6] != " ":
            ShowTray(Tray, player)
            print("Le joueur", player, "a gagné !")
            break

        if Round == 9:
            print("Egalité")
            break

        # Change le joueur du round
        player = "O" if player == "X" else "X"


# Lance le fichier
if __name__ == "__main__":
    Morpion()
