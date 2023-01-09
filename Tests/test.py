import unittest
import random

from Class import CoffeeMaker, piece


class MyTestCase(unittest.TestCase):
    def test_monnaieInsuffisante(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece20 = piece.piece(20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(26, machine.stockCafe)  # add assertion here

    def test_cafeDecremente(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.coule_cafe()

        self.assertEqual(29, machine.stockCafe)

    def test_gobeletDecremente(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.coule_cafe()
        self.assertEqual(49, machine.stockGobelets)

    def test_demandeSucre(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.stockSucre = 100
        piece50 = piece.piece(50)
        machine.ajout_sucre()
        machine.ajouter_une_piece(piece50)

        self.assertEqual(99, machine.stockSucre)

    # def test_tropDeMonnaie(self):
    #     machine = CoffeeMaker()
    #     monnaieRendue = machine.insert_monnaie('60')
    #
    #     self.assertEqual(20, monnaieRendue )
    #
    # def test_nickel(self):
    #     machine = CoffeeMaker()
    #     machine.insert_monnaie('40')
    #
    #     self.assertEqual(1, machine.nbCafeServis)  #

    # Test Théophile
    def test_unGobeletDeuxDemandes(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockGobelets = 1
        machine.stockCafe = 30
        piece50 = piece.piece(50)

        cafe1 = machine.ajouter_une_piece(piece50)
        cafe2 = machine.ajouter_une_piece(piece50)

        self.assertTrue(cafe1)
        self.assertFalse(cafe2)
        self.assertEqual(machine.monnayeur.monnaie_rendue, piece50)

    def test_ajouterZeroDose(self):
        machine = CoffeeMaker.CoffeeMaker()
        dosesManquantes = 0
        machine.stockCafe = 30 - dosesManquantes

        machine.ajouter_cafe(dosesManquantes + 1)

        self.assertEqual(30, machine.stockCafe)

    def test_ajouterUneDose(self):
        machine = CoffeeMaker.CoffeeMaker()
        dosesManquantes = 1
        machine.stockCafe = 30 - dosesManquantes

        machine.ajouter_cafe(dosesManquantes + 1)

        self.assertEqual(30, machine.stockCafe)

    def test_ajouterTrenteDoses(self):
        machine = CoffeeMaker.CoffeeMaker()
        dosesManquantes = 30
        machine.stockCafe = 30 - dosesManquantes

        machine.ajouter_cafe(dosesManquantes + 1)

        self.assertEqual(30, machine.stockCafe)

    def test_ajouterZeroGobelet(self):
        machine = CoffeeMaker.CoffeeMaker()
        gobeletsManquants = 0
        machine.stockGobelets = 50 - gobeletsManquants

        machine.ajouter_gobelet(gobeletsManquants + 1)

        self.assertEqual(50, machine.stockGobelets)

    def test_ajouterUnGobelet(self):
        machine = CoffeeMaker.CoffeeMaker()
        gobeletsManquants = 1
        machine.stockGobelets = 50 - gobeletsManquants

        machine.ajouter_gobelet(gobeletsManquants + 1)

        self.assertEqual(50, machine.stockGobelets)

    def test_ajouterCinquanteGobelets(self):
        machine = CoffeeMaker.CoffeeMaker()
        gobeletsManquants = 50
        machine.stockGobelets = 50 - gobeletsManquants

        machine.ajouter_gobelet(gobeletsManquants + 1)

        self.assertEqual(50, machine.stockGobelets)

    # test Gabriel
    def test_moinsDe40Cts(self):
        machine = CoffeeMaker.CoffeeMaker()
        pieces = [1, 2, 5, 10, 10]
        pieceR = 0
        for i in range(4):
            pieceR += random.choice(pieces)

        self.assertLess(pieceR, 40)
        print("Monnaie insuffisante, rendre : " + str(pieceR))
        machine.ajouter_une_piece(piece.piece(pieceR))

    def test_totalSuperieurA40Cts(self):
        machine = CoffeeMaker.CoffeeMaker()
        pieces = [10, 10, 20, 20, 50]
        pieceR = 0
        for i in range(4):
            pieceR += random.choice(pieces)

        self.assertGreater(pieceR, 40)
        print("Argent donné : " + str(pieceR))
        machine.ajouter_une_piece(piece.piece(pieceR - 40))

    def test_40Et50Cts(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = 40
        piece50 = 50
        total = piece40+piece50

        self.assertGreater(total, 80)
        machine.coule_cafe()

    def test_limitePieces(self):
        machine = CoffeeMaker.CoffeeMaker()
        for i in range(4):
            piece10 = piece.piece(10)
            machine.ajouter_une_piece(piece10)
        piece20 = piece.piece(20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(machine.monnayeur.valeur_monnaie, 20)

    #Test Erwan
    def test_rendreMonnaie(self):
        machine = CoffeeMaker.CoffeeMaker()
        pieces = [1, 2, 5, 10, 20, 50, 100, 200]
        pieceR = 0
        for i in range(4):
            pieceR += random.choice(pieces)
        
        self.assertGreater(pieceR, 40)
        print("Monnaie donnée : " + str(pieceR))
        machine.ajouter_une_piece(piece.piece(pieceR))
        
    def test_annulation(self):
        machine = CoffeeMaker.CoffeeMaker()
        pieces = [1, 2, 5, 10, 20, 50, 100, 200]
        pieceR = 0
        for i in range(4):
            pieceR += random.choice(pieces)

        machine.cancelled = True
        print("Monnaie donnée : " + str(pieceR))
        machine.ajouter_une_piece(piece.piece(pieceR))
        self.assertEqual(machine.monnayeur.valeur_monnaie, pieceR)
            
    def test_plusDeGoblet(self):
        machine = CoffeeMaker.CoffeeMaker()
        pieces = [1, 2, 5, 10, 20, 50, 100, 200]
        pieceR = 0
        for i in range(4):
            pieceR += random.choice(pieces)
        machine.stockGobelets = 0
        print("Monnaie donnée : " + str(pieceR))
        machine.ajouter_une_piece(piece.piece(pieceR))
        self.assertEqual(machine.monnayeur.valeur_monnaie, pieceR)
   
    #Test Quentin
    def test_cafecoule(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(30)

        machine.ajouter_une_piece(piece40)
        self.assertEqual(machine.monnayeur.valeur_monnaie, piece40.valeur)

    def test_encaissement(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece50 = piece.piece(50)
        
        machine.ajouter_une_piece(piece50)

        self.assertEqual(machine.monnayeur.valeur_monnaie, piece50.valeur)
        print("Monnaie encaissée : " + str(piece50))
       

    def test_plusDeCafe(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(40)
        machine.stockCafe = 0
        print("Monnaie donnée : " + str(piece40))
        machine.ajouter_une_piece(piece40)
        self.assertEqual(machine.monnayeur.valeur_monnaie, piece40.valeur)

    def test_plusDeau(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(40)
        machine.stockEau = 0
        print("Monnaie donnée : " + str(piece40))
        machine.ajouter_une_piece(piece40)
        self.assertEqual(machine.monnayeur.valeur_monnaie, piece40.valeur)


    #Tests Hugo Divet
    def test_tassePresente(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        piece50 = piece.piece(50)
        machine.ajout_tasse()
        machine.ajouter_une_piece(piece50)

        self.assertEqual(50 , machine.stockGobelets)

    def test_remetCafe(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockCafe = 20
        machine.ajouter_cafe(20)

        self.assertEqual(30, machine.stockCafe)

    def test_remetGobelet(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockGobelets = 40
        machine.ajouter_gobelet(10)
        
        self.assertEqual(50, machine.stockGobelets)

    def test_plusGobeletsMaisTasse(self):
        machine = CoffeeMaker.CoffeeMaker()
        machine.stockGobelets = 0
        machine.stockCafe = 30
        piece20 = piece.piece(20)
        machine.ajout_tasse()
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(29, machine.stockCafe)

if __name__ == '__main__':
    unittest.main()
