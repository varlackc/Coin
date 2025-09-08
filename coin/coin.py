import random

class Coin:
    def __init__(self):
        self.face = "Head"
        self.head = "Head"
        self.tail = "Tails"
        self.value = "$25"
    
    def flip(self):
        self.face = random.choice([self.head, self.tail])
        return str(self.face)
    
    def get_face(self):
        return str(self.face)
    
    def set_face(self, value: str):
        self.face = value