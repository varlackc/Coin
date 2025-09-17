

class CoinSet:
    def __init__(self):
        self.coin_collection = []
        self.coin_faces = []
        self.coin_total_value = 0
        
    def add_coin(self, coin):
        # add a single coin to the coin set
        self.coin_collection.append(coin)
        
    def add_coins(self, coins):
        # add multiple coins to the coin set
        for i in range(len(coins)):
            self.coin_collection.append(coins[i])
        
    def get_faces(self):
        # reset the coin faces
        self.coin_faces = []
        for face in self.coin_collection:
            self.coin_faces.append(face.get_face())
        return self.coin_faces
    
    def set_faces(self, dice_faces):
        self.coin_faces = []
        for face in dice_faces:
            self.coin_faces.append(face)
        return self.coin_faces
    
    def flip(self):
        # reset the coin faces
        self.coin_faces = []
        for coin in self.coin_collection:
            self.coin_faces.append(coin.flip())
        return self.coin_faces
        