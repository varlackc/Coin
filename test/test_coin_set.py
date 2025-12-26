"""
Program: Test Coin Set
Author: Maxwell Varlack
Description: This program is used to 
Test the Coin Set class.
"""
import unittest
from coin import CoinSet, Coin


class TestCoinSet(unittest.TestCase):
    """
    Tests for the CoinSet class

    Args:
        unittest (_type_): _description_
    """
    def test_CoinSet_add_coin(self) -> None:
        """
        test to verify that the
        coin value can be added
        """
        c1 = Coin()
        cs = CoinSet()
        cs.add_coin(c1)
        self.assertGreater(len(cs.coin_collection), 0)
        
    def test_CoinSet_add_coins(self) -> None:
        """
        test to verify that multiple
        coins could be added
        """
        c1 = Coin()
        c2 = Coin()
        cs = CoinSet()
        cs.add_coins([c1, c2])
        self.assertGreater(len(cs.coin_collection), 1)

    def test_CoinSet_flip(self) -> None:
        """
        test to verify that the
        coins could be flipped
        """
        self.assertIsNotNone(CoinSet().coin_collection)
        
    def test_coinset_get_faces(self) -> None:
        """
        test to verify that the faces for
        the coinset could be aquired.
        """
        self.assertIsNotNone(CoinSet().get_faces())
        
    def test_coinset_set_face(self) -> None:
        """
        Docstring for test_coinset_set_face
        :param self: test to verify that the face of the coinset can be assigned
        """
        coin_A = Coin()
        coin_B = Coin()
        coin_set_A = CoinSet()
        self.assertEqual(coin_set_A.set_faces(["H", "H"]), ["H", "H"])
        