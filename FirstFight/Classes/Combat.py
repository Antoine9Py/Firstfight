from Classes.Joueur import Joueur
from Classes.Adversaire import Ennemi
import random as r
def combat(joueur, ennemi):
    print(f"Le combat commence entre {joueur.name} et un ennemi !")

    while joueur.hp > 0 and ennemi.hp > 0:
        # Tour du joueur
        print(f"{joueur.name}: {joueur.hp} HP, Energie : {joueur.energie}, Ennemi: {ennemi.hp} HP")
        choix = input("Choisissez une action: (1) Attaque normale (2) Attaque lourde (3) Soin: ")
        if choix == "1":
            degats = joueur.attaque_normale()
            print(f"{joueur.name} attaque et inflige {degats} degats.")
            ennemi_en_vie = ennemi.prendre_degats(degats)
            if not ennemi_en_vie:
                print(f"{joueur.name} a vaincu l'ennemi !")
                break
        elif choix == "2":
            degats = joueur.attaque_lourde()
            print(f"{joueur.name} lance une attaque lourde et inflige {degats} degats.")
            ennemi_en_vie = ennemi.prendre_degats(degats)
            if not ennemi_en_vie:
                print(f"{joueur.name} a vaincu l'ennemi !")
                break
        elif choix == "3":
            soins = joueur.soin()
            print(f"{joueur.name} se soigne et recupere {soins} points de vie.")
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
                print(f"{joueur.name} a ete vaincu par l'ennemi...")

def jeu():
    joueur = Joueur()
    while True:
        ennemi = Ennemi()
        combat(joueur, ennemi)
        if joueur.hp > 0:
            print(f"Felicitations {joueur.name}, vous avez gagne le combat !")
            joueur.ameliorer_attributs()
            print("Un nouvel adversaire s'avance !")
        else:
            print("Vous avez perdu. Fin du jeu.")
            break
