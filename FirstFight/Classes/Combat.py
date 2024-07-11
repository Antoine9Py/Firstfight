from Classes.Joueur import Joueur
from Classes.Adversaire import Ennemi
import random as r
def combat(joueur, ennemi):
    tour = 0
    print(f"Le combat commence entre {joueur.nom} et un gobelin : {ennemi.nom}!")

    while joueur.hp > 0 and ennemi.hp > 0:
        # Tour du joueur
        if tour != 0 & (joueur.energie + 1) <= 5:
            joueur.energie += 1
            print("Vous regagnez 1 points d'énergies\n")
        print(f"{joueur.nom}: {joueur.hp} HP, Energie : {joueur.energie}, Ennemi: {ennemi.hp} HP")
        choix = input("Choisissez une action: (1) Attaque normale (2) Attaque lourde (3) Soin (4) Mediter : ")
        if choix == "1":
            degats = joueur.attaque_normale()
            print(f"{joueur.nom} attaque et inflige {degats} degats.")
            ennemi_en_vie = ennemi.prendre_degats(degats)
            if not ennemi_en_vie:
                print(f"{joueur.nom} a vaincu l'ennemi !")
                break
        elif choix == "2":
            degats = joueur.attaque_lourde()
            print(f"{joueur.nom} lance une attaque lourde et inflige {degats} degats.")
            ennemi_en_vie = ennemi.prendre_degats(degats)
            if not ennemi_en_vie:
                print(f"{joueur.nom} a vaincu l'ennemi !")
                break
        elif choix == "3":
            soins = joueur.soin()
            print(f"{joueur.nom} se soigne et recupere {soins} points de vie.")
        elif choix == "4":
            joueur.mediter()
            print("Vous mediter et recuperer 3 points d'energie")
        else:
            print("Choix invalide. Tour perdu.")
            continue  # Passe le tour de l'ennemi

        # Tour de l'ennemi
        if ennemi.hp > 0:
            if r.choice([True, False]):
                degats = ennemi.dague()
                print(f"L'ennemi attaque avec une dague et inflige {degats} degats.")
            else:
                degats = ennemi.epee()
                print(f"L'ennemi attaque avec une epee et inflige {degats} degats.")
            
            joueur_en_vie = joueur.prendre_degats(degats)
            if not joueur_en_vie:
                print(f"{joueur.nom} a ete vaincu par l'ennemi...")
            tour += 1

def jeu():
    joueur = Joueur()
    while True:
        ennemi = Ennemi()
        combat(joueur, ennemi)
        if joueur.hp > 0:
            print(f"Felicitations {joueur.nom}, vous avez gagne le combat !")
            joueur.ameliorer_attributs()
            print("Un nouvel adversaire s'avance !")
        else:
            print("Vous avez perdu. Fin du jeu.")
            break
