"""
Program: Coin_set
Author: Maxwell Varlack
Description: This program is used to represent
the behaviour of multiple coins and to simulate 
coin operations on a set of coins.
"""


class CoinSet:
    """
    This class is used to hold multiple coins and make operations on the coins
    """
    def __init__(self) -> any:
        """
        Method to initialize the CoinSet class
        """
        self.coin_collection:list = []
        self.coin_faces:list = []
        self.coin_total_value:int = 0
        
    def add_coin(self, coin):
        """
        Add a single coin to the coin set
        """
        self.coin_collection.append(coin)
        
    def add_coins(self, coins):
        """
        Add multiple coins to the coin set
        """
        for i in range(len(coins)):
            self.coin_collection.append(coins[i])
        
    def get_faces(self):
        # reset the coin faces
        self.coin_faces:list = []
        for face in self.coin_collection:
            self.coin_faces.append(face.get_face())
        return self.coin_faces
    
    def set_faces(self, faces):
        # assign value to the faces of multiple coins
        self.coin_faces:list = []
        for face in faces:
            self.coin_faces.append(face)
        return self.coin_faces
    
    def flip(self):
        # reset the coin faces
        self.coin_faces:list = []
        for coin in self.coin_collection:
            self.coin_faces.append(coin.flip())
        return self.coin_faces
        