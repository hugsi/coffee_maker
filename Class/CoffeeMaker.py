from Class import monnayeur, piece


class CoffeeMaker:

    def __init__(self):
        self.stockCafe = 30
        self.stockGobelets = 50
        self.stockSucre = 100
        self.demandeSucre = 0
        self.monnayeur = monnayeur.Monnayeur()

    def coule_cafe(self):
        if self.stockGobelets >= 1:
            self.stockCafe -= 1
            self.stockGobelets -= 1
            self.stockSucre -= self.demandeSucre
            self.demandeSucre = 0
            print('Je fais couler un café')
            return True
        else:
            return False

    def ajout_sucre(self):
        self.demandeSucre += 1 
        print("J'ajoute du sucre")

    def ajouter_une_piece(self, monnaie):
        self.monnayeur.ajouter_monnaie(monnaie)
        if self.monnayeur.check_monnaie() == 1:
            cafeCoule = self.coule_cafe()
            if cafeCoule == False:
                self.monnayeur.rendre_monnaie(monnaie)
                return False
            return True
        else:
            print('Crédit insuffisant : ' + str(self.monnayeur.valeur_monnaie))
            return False

    def ajouter_cafe(self,doses):
        if (self.stockCafe+doses>30):
            # ne pas dépasser le max de doses
            self.stockCafe = 30
        else:
            self.stockCafe += doses

    def ajouter_gobelet(self,gobelets):
        if (self.stockGobelets+gobelets>30):
            # ne pas dépasser le max de gobelets
            self.stockGobelets = 50
        else:
            self.stockGobelets += gobelets

