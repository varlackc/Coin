import unittest
from coin import CoinSet, Coin


class TestCoinSet(unittest.TestCase):
    def test_CoinSet_add_coin(self):
        c1 = Coin()
        cs = CoinSet()
        cs.add_coin(c1)
        self.assertGreater(len(cs.coin_collection), 0)
        
    def test_CoinSet_add_coins(self):
        c1 = Coin()
        c2 = Coin()
        cs = CoinSet()
        cs.add_coins([c1, c2])
        self.assertGreater(len(cs.coin_collection), 1)

    def test_CoinSet_flip(self):
        self.assertIsNotNone(CoinSet().coin_collection)
        
    def test_coinset_get_faces(self):
        self.assertIsNotNone(CoinSet().get_faces())
        
    def test_coinset_set_face(self):
        coin_A = Coin()
        coin_B = Coin()
        coin_set_A = CoinSet()
        self.assertEqual(coin_set_A.set_faces(["H", "H"]), ["H", "H"])
        