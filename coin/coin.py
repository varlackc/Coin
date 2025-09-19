import random


class Coin:
    """
    Section to represent individual coins
    """
    def __init__(self):
        self.face = "Head"
        self.head = "Head"
        self.tail = "Tails"
        self.value = "$0.25"
    
    def flip(self):
        # This method is used to flip coins
        self.face = random.choice([self.head, self.tail])
        return str(self.face)
    
    def get_face(self):
        # This method is used to get the face value on the coin
        return str(self.face)
    
    def set_face(self, value: str):
        # This method is used to change the face value on the coin
        self.face = value
        
    def get_head(self):
        # This method is used to get the value in the head section of the coin
        return self.head
    
    def set_head(self, head: str):
        # This method is used to assign the value in the head section of the coin
        self.head = head
        
    def get_tails(self):
        # This method shows the cointent of the tails value
        return self.tail
    
    def set_tails(self, tails):
        # this method sets a value for the tails of the coin
        self.tail = tails
        
    def set_coin(self, head, tail):
        # set the head and tail values to a coin in one method
        self.head = head
        self.tail = tail
        self.face = self.head
        
    def get_coin(self):
        # get the head and tail values in a given coin
        return [self.head, self.tail]
