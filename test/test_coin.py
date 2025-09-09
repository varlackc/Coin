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
        
    def test_coin_get_head(self):
        self.assertIsNotNone(Coin().get_head())
 
    def test_coin_set_head(self):
        coin = Coin()
        coin.set_head("H")
        self.assertIsNotNone(coin.get_head())
        
    def test_coin_get_tails(self):
        self.assertIsNotNone(Coin().get_tails())
    
    def test_coin_set_tails(self):
        coin = Coin()
        coin.set_tails("T")
        self.assertEqual(coin.get_tails(), "T")