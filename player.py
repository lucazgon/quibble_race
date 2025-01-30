from common_commands import random_name_gen
from menu import input_validation

class Player():
    def __init__(self, is_player):
        self.is_player = is_player
        self.name = 'default_name'
        self.funds = 100
        self.racer_bet = None
        self.num_bet = 50

        if self.is_player:
            self.set_name()
        else:
            self.name = random_name_gen()
            
    def place_bet(self,racer,bet_amount):
        self.racer_bet = racer
        self.num_bet = bet_amount
        self.funds -= self.num_bet
        pass
    def input_text(self):
        pass      
    def set_name(self):
        print("Input player name: ")
        self.name = input_validation()
        #self.name = input("Input player name: ")
        return self.name
    def generate_name(self):
        return "randomly generated name"