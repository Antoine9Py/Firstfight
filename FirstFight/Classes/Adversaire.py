# -*- coding: utf-8 -*-
import random as r

class Ennemi:
    def __init__(self):
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