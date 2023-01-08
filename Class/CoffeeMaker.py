from Class import monnayeur, piece


class CoffeeMaker:

    def __init__(self):
        self.stockCafe = 30
        self.stockGobelets = 50
        self.stockSucre = 100
        self.demandeSucre = 0
        self.stockEau = 0
        self.besoinGobelet = 1
        self.monnayeur = monnayeur.Monnayeur()
        self.cancelled = False

    def coule_cafe(self):
        if self.stockGobelets >= 1 & self.cancelled is False:
            self.stockCafe -= 1
            self.stockGobelets -= 1
            self.stockSucre -= self.demandeSucre
            self.demandeSucre = 0
            print('Je fais couler un café')
            return True
        else:
            return False

    def ajout_tasse(self):
        self.besoinGobelet = 0
        print("Il y a une tasse")

    def ajout_sucre(self):
        if self.demandeSucre < 5:
            self.demandeSucre += 1 
            print("J'ajoute du sucre")

    def ajouter_une_piece(self, monnaie):
        if (self.stockCafe > 0 | self.stockGobelets > 0 | self.cancelled is not False): 
            self.monnayeur.ajouter_monnaie(monnaie)
            if self.monnayeur.check_monnaie() == 1:
                self.coule_cafe()
        else:
            self.monnayeur.valeur_monnaie = monnaie.valeur
            self.monnayeur.rendre_monnaie()
            if(self.cancelled is True):
                print("Commande Annulée")
            if(self.stockCafe == 0):
                print("Plus de café")
            if(self.stockGobelets == 0):
                print("Plus de gobelet")
            

    def ajouter_cafe(self, doses):
        if self.stockCafe + doses > 30:
            # ne pas dépasser le max de doses
            self.stockCafe = 30
        else:
            self.stockCafe += doses

    def ajouter_gobelet(self, gobelets):
        if (self.stockGobelets + gobelets > 30):
            # ne pas dépasser le max de gobelets
            self.stockGobelets = 50
        else:
            self.stockGobelets += gobelets
