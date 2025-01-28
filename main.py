# import
from player import Player
from racer import Racer
import pdb
import random

def input_handler(list):
    # print a menu
    for obj in list:
        print(f"{list.index(obj)}) {obj}")

    active = True
    while active == True:
        user_input = int(input())

        # print(type(user_input))
        if user_input >= 0 and user_input <= len(list):
            active = False
        else:
            print(f"input, not accepted. expecting: {expected_type}")
            
        
    return user_input

# main
def main():

    racer_list = []
    racer_current_list = []

    player_list = []
    num_players = 1
    num_racers = 6

    print ("welcome to quibble race!")
    print("how many players?")
    num_players = input_handler("str")
    
    
    print(num_players)
    print('is that correct? y/n')
    if input() != "y":
        # go back to is that correct?
        pass

    player_list.append(Player(True))
    for i in range (0,len(num_players)):
        #pdb.set_trace()
        player_list.append(Player(False))

    for i in range (0,num_racers):
        racer_list.append(Racer())

    #for player in player_list:
    print("place bets on a racer!")
    # make random list of racers
    for i in range(0,2):
        racer_current_list.append(racer_list[random.randint(0,len(racer_list))])
    #let each player pick one
    for player in player_list:
        print(player.name)
        print(racer_current_list)
        player_input = input('which quib?')
        print(racer_current_list[int(player_input)])

    print(" race 1 starting / results!")
    print(racer_current_list[random.randint(0,len(racer_list)-1)])



if __name__ == "__main__":
    main()