import unittest

from CoffeeMaker import CoffeeMaker
from piece import piece


class MyTestCase(unittest.TestCase):
    def test_monnaieInsuffisante(self):
        machine = CoffeeMaker()
        piece20 = piece(20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(28, machine.stockCafe)  # add assertion here

    def test_cafeDecremente(self):
        machine = CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.coule_cafe()
        
        self.assertEqual(29, machine.stockCafe)
        
    def test_gobeletDecremente(self):
        machine = CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.coule_cafe()
        self.assertEqual(49, machine.stockGobelets)
        

    def test_demandeSucre(self):
        machine = CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        machine.stockSucre = 100
        piece50 = piece(50)
        machine.ajout_sucre()
        machine.ajouter_une_piece(piece50)
        
        self.assertEqual(99, machine.stockSucre)
        
    def test_tassePresente(self):
        machine = CoffeeMaker()
        machine.stockCafe = 30
        machine.stockGobelets = 50
        piece50 = piece(50)
        machine.ajout_tasse()
        machine.ajouter_une_piece(piece50)

        self.assertEqual(50 , machine.stockGobelets)

    def test_remetCafe(self):
        machine = CoffeeMaker()
        machine.stockCafe = 20
        machine.ajout_cafe(10)

        self.assertEqual(30, machine.stockCafe)

    def test_remetGobelet(self):
        machine = CoffeeMaker()
        machine.stockGobelets = 40
        machine.ajout_gobelets(10)
        
        self.assertEqual(50, machine.stockGobelets)

    def test_plusGobeletsMaisTasse(self):
        machine = CoffeeMaker()
        machine.stockGobelets = 0
        machine.stockCafe = 30
        piece20 = piece(20)
        machine.ajout_tasse()
        machine.ajouter_une_piece(piece20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(29, machine.stockCafe)
        

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

        

if __name__ == '__main__':
    unittest.main()