from common_commands import random_name_gen

class Player():
    def __init__(self, is_player):
        self.is_player = is_player
        self.name = 'default_name'
        self.money = 100
        self.bet = None

        if self.is_player:
            self.set_name()
        else:
            self.name = random_name_gen()
            

    def input_text(self):
        pass      
    def set_name(self):
        self.name = input("Input player name: ")
        return self.name
    def generate_name(self):
        return "randomly generated name"