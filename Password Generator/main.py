import os
import random
import string
import term


# Générer un mot de passe
def GeneratePassword(pwlength):
    alphabet = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = ''
    for i in range(pwlength):
        charset = random.randint(1, 3)
        if charset == 1:
            password += random.choice(alphabet)
        elif charset == 2:
            password += random.choice(digits)
        else:
            password += random.choice(symbols)

    return password


# Main
def main():
    numPasswords = int(input("Combien de mots de passe voulez-vous ? "))
    if numPasswords <= 0:
        print("Veuillez entrer un nombre valide de mots de passe.")
        return

    passwords = []
    term.clear()
    print("Chaque mot de passe doit faire au minimum 3 caractères !")

    for i in range(numPasswords):
        length = int(input("Entrez la longueur du mot de passe #" + str(i + 1) + " : "))
        if length < 3:
            print("La longueur doit être d'au moins 3 caractères. Réessayez.")
            return
        passwords.append(GeneratePassword(length))

    term.clear()
    with open("passwords.txt", "w") as file:
        if file.tell() != 0:
            file.truncate()
        else:
            for i, password in enumerate(passwords):
                print("Mot de passe #" + str(i + 1) + " : " + password)
                file.write("Mot de passe #" + str(i + 1) + " : " + password + "\n")


if __name__ == "__main__":
    main()
