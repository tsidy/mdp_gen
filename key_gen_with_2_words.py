import random
import string
# La fonction qui génère un mot de passe aléatoire contenant deux mots
def generer_mot_de_passe():
    """La fonction contien 3 parametres obligatoires:
    1 - la longuer du mot de pass à générer
    2 - un mot que vous voulez inserer
    3 - un autre mot que vous voulez aussi"""
    print("Vous devez entrer la longueur du mot de passe à générer et deux mots différent")
    longueur = int(input("Entrer la longueur du mot de passe à générer : "))
    mot1 = str(input("Entrer un mot que vous aimeriez inclure dans le mot de passe : "))
    mot2 = str(input("Entrer un mot que vous aimeriez inclure dans le mot de passe : "))
    # On vérifie que la longueur est suffisante
    if longueur < (len(mot1) + len(mot2)):
        print("La longueur doit être supérieure ou égale à {}".format(len(mot1) + len(mot2)))
        return None
    # La séquence de caractères possibles
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # La liste vide qui va contenir les caractères aléatoires
    liste = []
    # On sélectionne longueur - len (mot) caractères aléatoires sans répétition dans caracteres
    liste = random.sample(caracteres, longueur - (len(mot1) + len(mot2)))
    # On choisit deux positions aléatoires différentes pour insérer les mots dans la liste
    position1 = random.randint(0, longueur - len(mot1))
    position2 = random.randint(0, longueur - len(mot2))
    while position1 == position2 or abs(position1 - position2) < max(len(mot1), len(mot2)):
        position1 = random.randint(0, longueur - len(mot1))
        position2 = random.randint(0, longueur - len(mot2))
        # On insère les mots dans la liste aux positions choisies
    liste.insert(position1, mot1)
    liste.insert(position2, mot2)
    # On convertit la liste en une chaîne avec la méthode join ()
    mot_de_passe = "".join(liste)
    # On renvoie le mot de passe
    return mot_de_passe

# On appelle la fonction
mot_de_passe = generer_mot_de_passe()
# On affiche le résultat
print("Mot de passe généré : {}".format(mot_de_passe))
