from Variables import constant
from Class import piece


class Monnayeur:

    def __init__(self):
        self.list_piece = list()
        self.valeur_monnaie = 0

    def rendre_monnaie(self):
        print("Monnaie rendue: " + str(self.valeur_monnaie))
        self.valeur_monnaie = 0
        self.list_piece.clear()

    def ajouter_monnaie(self, monnaie: piece):
        self.valeur_monnaie += monnaie.valeur
        self.list_piece.append(monnaie)

    def check_monnaie(self):
        if 4 == len(self.list_piece) & self.get_valeur_monnaie() < constant.COFFEE_PRICE:
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

            self.rendre_monnaie()
        if self.get_valeur_monnaie() >= int(constant.COFFEE_PRICE):
            self.payer_cafe()
            if int(self.valeur_monnaie) > 0:
                self.rendre_monnaie()
            return 1
        print('Crédit insuffisant, monnaie : ', self.get_valeur_monnaie())
        return 0

    def get_valeur_monnaie(self):
        valeur = int(0)
        for i in self.list_piece:
            valeur += i.valeur
        return valeur

    def payer_cafe(self):
        self.valeur_monnaie = int(self.valeur_monnaie) - int(constant.COFFEE_PRICE)

