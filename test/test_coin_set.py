import unittest
from coin import CoinSet


class TestCoinSet(unittest.TestCase):
    def test_CoinSet_flip(self):
        self.assertIsNotNone(CoinSet().flip())
        
    def test_coinset_get_face(self):
        self.assertIsNotNone(CoinSet().get_faces())
        