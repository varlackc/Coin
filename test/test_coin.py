"""
Program: Test Coin
Author: Maxwell Varlack
Description: This program is used to 
Test the Coin class.
"""
import unittest
from coin import Coin


class TestCoin(unittest.TestCase):
    """
    tests for the Coin class

    Args:
        unittest (_type_): _description_
    """
    def test_coin_flip(self):
        """
        test to verify that output is provided
        after fliping a coing
        """
        self.assertIsNotNone(Coin().flip())
    
    def test_coin_get_face(self):
        """
        test to verify that output is given
        after getting the face of the coin
        """
        self.assertIsNotNone(Coin().get_face())
    
    def test_coin_set_face(self):
        """
        test to verify that the face value
        is set properly
        """
        coin = Coin()
        coin.set_face("Head")
        self.assertEqual(coin.get_face(), "Head")
        
    def test_coin_get_head(self):
        """
        test to verify that the head value
        provides an output
        """
        self.assertIsNotNone(Coin().get_head())
 
    def test_coin_set_head(self):
        """
        test to verify that the head value
        can be modified
        """
        coin = Coin()
        coin.set_head("H")
        self.assertIsNotNone(coin.get_head())
        
    def test_coin_get_tails(self):
        """
        test to verify that the tails value
        can be modified
        """
        self.assertIsNotNone(Coin().get_tails())
    
    def test_coin_set_tails(self):
        # test to verify that the tails value
        # can be set
        coin = Coin()
        coin.set_tails("T")
        self.assertEqual(coin.get_tails(), "T")
        
    def test_coin_set_coin(self):
        # test to verify that the coin value
        # can be set
        coin = Coin()
        coin.set_coin("H", "T")
        self.assertEqual([coin.get_head(), coin.get_tails()], ["H","T"])
    
    def test_coin_get_coin(self):
        # test to verify that the coin value
        # can be reached
        coin = Coin()
        coin.set_coin("H", "T")
        self.assertEqual(coin.get_coin(), ["H", "T"])
        