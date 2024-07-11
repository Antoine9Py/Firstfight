# -*- coding: utf-8 -*-
import random as r

class Joueur:
    def __init__(self, nom=None):
        if nom is None:
            self.nom = input("Entrez votre nom: ")
        else:
            self.nom = nom
        self.hp = 100
        self.armure = 0
        self.attaque = 10
        self.esquive = 5
        self.critique = 5
        self.energie = 5

    def attaque_normale(self):
        if self.energie - 2 < 0:
            print("Pas assez d'energie pour faire cela !")
            print("Vous vous préparez à encaisser le coup, mais vous regagnez 2 d'énergie !")
            self.energie += 2
            return 0
        else : 
            self.energie -= 2
            degat = self.attaque + r.randint(-2, 3)
            test_critique = r.randint(0, 100)
            if test_critique <= self.critique:
                degat *= 2
            return degat
    
    def attaque_lourde(self):
        if self.energie - 3 < 0:
            print("Pas assez d'energie pour faire cela !")
            print("Vous vous préparez à encaisser le coup, mais vous regagnez 2 d'énergie !")
            self.energie += 2
            return 0
        else : 
            self.energie -= 3
            degat = (self.attaque * 2) + r.randint(-2, 3)
            test_critique = r.randint(0, 100)
            if test_critique <= self.critique:
                degat *= 2
            return degat

    def soin(self):
        soins = r.randint(0, 20)
        self.hp += soins
        if self.hp > 100:
            self.hp = 100
        return soins  # Retourne les points de vie restaures
    def mediter(self):
        self.energie += 3
        if self.energie > 5:
            self.energie = 5

    def prendre_degats(self, degat):
        self.hp -= degat
        if self.hp < 0:
            self.hp = 0
        return self.hp > 0  # Retourne True si le joueur est toujours en vie
    
    def ameliorer_attributs(self):
        points = 5  # Nombre de points a distribuer apres chaque victoire
        print(f"Vous avez {points} points a distribuer entre vos attributs.")
        while points > 0:
            print(f"Points restants: {points}")
            print(f"Stats actuelles : Attaque : {self.attaque} | Armure : {self.armure} | Esquive : {self.esquive} | Critique : {self.critique}")
            choix = input("Choisissez un attribut a améliorer \n(1) Attaque \n(2) Armure \n(3) Esquive \n(4) Critique: ")
            if choix == "1":
                self.attaque += 1
                points -= 1
            elif choix == "2":
                self.armure += 1
                points -= 1
            elif choix == "3":
                self.esquive += 1
                points -= 1
            elif choix == "4":
                self.critique += 1
                points -= 1
            else:
                print("Choix invalide. Essayez a nouveau.")