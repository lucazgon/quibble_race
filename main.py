# import
from player import Player
from racer import Racer
import pdb
import random
import time

# maybe menu / input handler should be separate
# display menu, input needs: 0-20
# 
def input_handler(list):
    # print a menu
    for obj in list:
        print(f"{list.index(obj)}) {obj}")

    active = True
    while active == True:
        user_input = int(input())

        # print(type(user_input))
        if user_input == "q":
            break
            pass
        if user_input >= 0 and user_input <= len(list):
            active = False
        else:
            print(f"input, not accepted. expecting: a number between 0 - {len(list)-1}")
            
        
    return list[user_input]



# main
def main():

    #
    racer_list = []
    racer_current_list = []

    player_list = []
    num_players_list =[1,2,3,4]
    num_players = 1
    max_players = 4
    num_racers = 6
    num_rounds = 6
    cur_round = 0
    cur_season = 0

    # first time
    print ("### Welcome to Quibble Race! ###")

    while True:
        #print(f"season: {cur_season}")
        
        print(f"How many human players? (max: {max_players})")
        num_players = int(input())

        for i in range (0,num_players):
            player_list.append(Player(True))
        num_comp_players = max_players - num_players
        for i in range (0,num_comp_players):
            player_list.append(Player(False))

        for i in range (0,num_racers):
            racer_list.append(Racer())
        
        # primary game loop
        while cur_round < num_rounds:
            round_winners = []
            racer_current_list = []
            pot = 0

            # grab random racers from list
            for i in range(0,3):
                racer_current_list.append(racer_list[random.randint(0,len(racer_list)-1)].name)

            # pre race betting
            print("\n\n")
            print('#### Betting Phase ####')
            print(f"round: {cur_round} time to bet!")
            for player in player_list:
                print(f"{player.name}'s turn!")
                print("place bets on a racer!")
                if player.is_player == True:
                    player.bet = input_handler(racer_current_list)
                else:
                    time.sleep(1)
                    player.bet = random.randint(0, len(racer_current_list)-1)

                player.money -= 50
                pot += 50
            
            # race
            '''
            eventually racers will have stats / win losses and things
            '''
            print("\n")
            print('#### Racing Phase ####')
            curr_winner = racer_current_list[random.randint(0,len(racer_current_list)-1)]
            print(f"{curr_winner} wins!")
            
            # post race
            print('\n')
            print('#### Post Race Phase ####')
            for player in player_list:
                if player.bet == curr_winner:
                    round_winners.append(player)
            
            if len(round_winners) > 0:
                winnings = pot / len(round_winners)
                for player in round_winners:
                    player.money += winnings
                    print(f'{player.name} won {winnings} money!')
            else:
                print("no winners :'C")
            
            
            time.sleep(2)
                    # divide the pot among players who won

            cur_round += 1

        print('betting season over!, play again w/ same settings or different?')
        # what things need to change / remain the same
        # name of player, which ones are computer


if __name__ == "__main__":
    main()