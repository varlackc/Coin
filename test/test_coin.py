import unittest
from coin import Coin

class TestCoin(unittest.TestCase):
    def test_coin_flip(self):
        self.assertIsNotNone(Coin().flip())
    
    def test_coin_get_face(self):
        self.assertIsNotNone(Coin().get_face())
    
    def test_coin_set_face(self):
        coin = Coin()
        coin.set_face("Head")
        self.assertEqual(coin.get_face(), "Head")
        