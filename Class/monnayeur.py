from Variables import constant
from Class import piece


class Monnayeur:

    def __init__(self):
        self.nombre_piece = list()
        self.valeur_monnaie = 0
        self.monnaie_rendue = 0

    def rendre_monnaie(self, monnaie):
        print("Monnaie rendue: " + str(monnaie))
        self.monnaie_rendue = monnaie

    def ajouter_monnaie(self, monnaie: piece):
        self.valeur_monnaie += monnaie.valeur
        self.nombre_piece.append(monnaie)

    def check_monnaie(self):
        if 4 == len(self.nombre_piece) & self.valeur_monnaie < constant.COFFEE_PRICE:
            print("Nombre maximal de pieces atteintes")
            self.rendre_monnaie(self.valeur_monnaie)
        for i in self.nombre_piece:
            #self.valeur_monnaie = i.valeur + self.valeur_monnaie
            if int(self.valeur_monnaie) >= int(constant.COFFEE_PRICE):
                self.monnaie_rendue = int(self.valeur_monnaie) - int(constant.COFFEE_PRICE)
                if int(self.monnaie_rendue) > 0:
                    self.rendre_monnaie(self.monnaie_rendue)
                return 1
            elif int(self.valeur_monnaie) < int(constant.COFFEE_PRICE):
                return 0