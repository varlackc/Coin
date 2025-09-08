import unittest
from coin import Coin

class TestCoin(unittest.TestCase):
    def test_coin_flip(self):
        self.assertIsNotNone(Coin().flip())