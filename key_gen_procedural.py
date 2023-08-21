import random
import string

# La longueur du mot de passe
longueur = int(input("Entrer la longueur du mot de pass à générer: "))

# Le mot à inclure dans le mot de passe
mot1 = str(input("Entrer un mot que vous aimeriez inclure dans le mot de passe : "))
mot2 = str(input("Entrer un mot que vous aimeriez inclure dans le mot de passe : "))
if longueur > (len(mot1) + len(mot2)):
    # La séquence de caractères possibles
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # La liste vide qui va contenir les caractères aléatoires
    liste = []

    # On sélectionne longueur - len (mot) caractères aléatoires sans répétition dans caracteres
    liste = random.sample (caracteres, longueur - (len (mot1) + len (mot2)))

    # On choisit une position aléatoire pour insérer le mot dans la liste
    position1 = random.randint (0, longueur - len (mot1))
    position2 = random.randint (0, longueur - len (mot2))

    # On insère le mot dans la liste à la position choisie
    liste.insert (position1, mot1)
    liste.insert (position2, mot2)

    # On convertit la liste en une chaîne avec la méthode join ()
    mot_de_passe = "".join (liste)
    print ("Mot de passe généré : {}".format (mot_de_passe))
else:
    print("trop court par rapport aux mots d'ajout")
