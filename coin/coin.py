import random


class Coin:
    def __init__(self):
        self.face = "Head"
        self.head = "Head"
        self.tail = "Tails"
        self.value = "$0.25"
    
    def flip(self):
        self.face = random.choice([self.head, self.tail])
        return str(self.face)
    
    def get_face(self):
        return str(self.face)
    
    def set_face(self, value: str):
        self.face = value
        
    def get_head(self):
        return self.head
    
    def set_head(self, head: str):
        self.head = head
        
    def get_tails(self):
        return self.tail
    
    def set_tails(self, tails):
        self.tail = tails
        
    def set_coin(self, head, tail):
        self.head = head
        self.tail = tail
        self.face = self.head
        
    def get_coin(self):
        return [self.head, self.tail]
