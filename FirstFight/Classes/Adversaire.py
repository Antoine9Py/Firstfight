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
        10: "Murk",
        11: "Grub",
        12: "Squelch",
        13: "Stinktooth",
        14: "Muncher",
        15: "Slobber",
        16: "Fang",
        17: "Goober",
        18: "Sneak",
        19: "Sniffle",
        20: "Pustule",
        21: "Sludge",
        22: "Crud",
        23: "Splat",
        24: "Wart",
        25: "Maggot",
        26: "Slime",
        27: "Squirm",
        28: "Gobbo",
        29: "Rustle",
        30: "Mucus"
        }
        adjectifs_gobelins = {
        1: "le névrosé",
        2: "le pas très malin",
        3: "le mono-neurone",
        4: "le sournois",
        5: "le scintillant",
        6: "le manchot",
        7: "celui-avec-un-truc-en-plus",
        8: "le confus",
        9: "le boiteux",
        10: "le-pas-très-éclairé",
        11: "le morveux",
        12: "le raté",
        13: "le psychopathe",
        14: "le kamikaze",
        15: "le toxico",
        16: "le nécrophile",
        17: "le zombie",
        18: "le mutilé",
        19: "le catatonique",
        20: "le dément",
        21: "le sodomite de chèvres",
        22: "le platiste",
        23: "l'arriéré"
            }     
        self.nom = gobelins[r.randint(1,10)] + " " + adjectifs_gobelins[r.randint(1,10)] + " fils de " + gobelins[r.randint(1,10)] + " " + adjectifs_gobelins[r.randint(1,10)]
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