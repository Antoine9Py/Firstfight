# -*- coding: utf-8 -*-
import random as r

class Ennemi:
    
    def __init__(self):
        gobelins = {
        1: "Gurgle",
        2: "Snaggle",
        3: "Grimtooth",
        4: "Twitch",
        5: "Glimmer",
        6: "Razor",
        7: "Scuttle",
        8: "Boggle",
        9: "Hobble",
        10: "Murk"
        }
        adjectifs_gobelins = {
        1: "le névrosé",
        2: "le pas très malin",
        3: "le grincheux",
        4: "le tremblotant",
        5: "le scintillant",
        6: "le tranchant",
        7: "le furtif",
        8: "le confus",
        9: "le boiteux",
        10: "le sombre"
            }
        self.nom = gobelins[r.randint(1,10)] + " " + adjectifs_gobelins[r.randint(1,10)]
        self.hp = r.randint(50, 80)
        self.armure = r.randint(0, 5)
        self.attaque = r.randint(2, 8)
        self.esquive = r.randint(0, 10)
        self.critique = r.randint(0, 10)

    def dague(self):
        degat = self.attaque + r.randint(-2, 3)
        test_critique = r.randint(0, 100)
        if test_critique <= self.critique:
            degat *= 2
        return degat
    
    def epee(self):
        degat = (self.attaque * 2) + r.randint(-2, 3)
        test_critique = r.randint(0, 100)
        if test_critique <= self.critique:
            degat *= 2
        return degat

    def prendre_degats(self, degat):
        self.hp -= degat
        if self.hp < 0:
            self.hp = 0
        return self.hp > 0  # Retourne True si l'ennemi est toujours en vie