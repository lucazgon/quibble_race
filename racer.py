import random

from common_commands import random_name_gen

class Racer():
    def __init__(self):
        self.name = random_name_gen()
        self.speed = random.randint(1,3)
        self.acceleration = None
        self.wins = 0
        self.games_played = 0
        self.x = 0
    
    def update(self):
        self.x += self.speed
        pass