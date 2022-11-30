from monnayeur import Monnayeur
import piece


class CoffeeMaker:

    def __init__(self):
        self.stockCafe = 30
        self.stockGobelets = 50
        self.stockSucre = 100
        self.demandeSucre = 0
        self.monnayeur = Monnayeur()

    def coule_cafe(self):
        self.stockCafe -= 1
        self.stockGobelets -= 1
        self.stockSucre -= self.demandeSucre
        self.demandeSucre = 0
        print('Je fais couler un café')

    def ajout_sucre(self):
        self.demandeSucre += 1 
        print("J'ajoute du sucre")

    def ajouter_une_piece(self, monnaie: piece):
        self.monnayeur.ajouter_monnaie(monnaie)
        if self.monnayeur.check_monnaie() == 1:
            self.coule_cafe()
        else:
            print('Crédit insuffisant : ' + str(self.monnayeur.valeur_monnaie))

