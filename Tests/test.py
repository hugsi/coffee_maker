import unittest

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
        piece5 = piece.piece(2)
        machine.ajouter_une_piece(piece5)
        machine.ajouter_une_piece(piece5)
        machine.ajouter_une_piece(piece5)
        machine.ajouter_une_piece(piece5)

        self.assertEqual(14, machine.monnayeur.monnaie_rendue)

    def test_totalSuperieurA40Cts(self):
        for i in range(1, 5):
            machine = CoffeeMaker.CoffeeMaker()
            for j in range(i):
                piece10 = piece.piece(40)
                machine.ajouter_une_piece(piece10)

            self.assertTrue(machine.coule_cafe())  # café servi

    def test_40Et50Cts(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(40)
        piece50 = piece.piece(50)
        machine.ajouter_une_piece(piece40)
        machine.ajouter_une_piece(piece50)

        self.assertTrue(machine.coule_cafe())  # 1er café servi

        #self.assertEqual(90, machine.monnayeur.encaisse)  # 90 cts encaissés

    def test_limitePieces(self):
        machine = CoffeeMaker.CoffeeMaker()
        for i in range(4):
            piece10 = piece.piece(10)
            machine.ajouter_une_piece(piece10)
        piece20 = piece.piece(20)
        machine.ajouter_une_piece(piece20)

        self.assertEqual(machine.monnayeur.monnaie_rendue, 20)
        ##self.assertFalse(machine.coule_cafe())  # aucun café servi

    #Test Quentin
    def test_cafecoule(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(30)

        machine.ajouter_une_piece(piece40)

    def test_encaissement(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece50 = piece.piece(50)

        self.assertEqual(50, machine.ajouter_une_piece(piece50))
        self.assertTrue(machine.coule_cafe())

    def test_plusDeCafe(self):
        machine = CoffeeMaker.CoffeeMaker()
        piece40 = piece.piece(40)
        machine.stockCafe = 0
        machine.ajouter_une_piece(piece40)


if __name__ == '__main__':
    unittest.main()
