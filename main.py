# import
from player import Player
from racer import Racer
from race_track import RaceTrack
from menu import menu, input_validation
import pdb
import random
import time

# main
def main():

    racer_list = []
    racer_current_list = []
    player_list = []
    num_players_list = [1,2,3,4]
    num_players = 1
    max_players = 4
    num_racers = 6
    num_rounds = 1
    cur_round = 0
    cur_season = 0
    winnings = 0

    # first time
    print ("### Welcome to Quibble Race! ###")

    while True:
        print(f"Season: {cur_season}")
        
        print(f"How many human players? (max: {max_players})")
        num_players = menu(num_players_list)

        for i in range (0,num_players):
            player_list.append(Player(True))
        num_comp_players = max_players - num_players
        for i in range (0,num_comp_players):
            player_list.append(Player(False))

        # generate racers
        for i in range (0,num_racers):
            racer_list.append(Racer())
        
        # primary game loop
        while cur_round < num_rounds:
            round_winners = []
            round_winners.clear()
            racer_current_list = []
            racer_current_list.clear()
            racer_current_list = racer_list.copy()
            pot = 0

            # grab random racers from list
            for i in range(0,3):
                #racer_current_list.append(racer_list[random.randint(0,len(racer_list)-1)].name)
                racer_current_list.remove(racer_current_list[random.randint(0,len(racer_current_list)-1)])
            # pre race betting
            print('\n#### Betting Phase ####')
            print(f"round: {cur_round} time to bet!")
            for player in player_list:
                print(f"{player.name}'s turn!")
                
                if player.is_player == True:
                    print("place bets on a racer!")
                    player.place_bet(menu(racer_current_list),int(input("how much?:\n>")))
                    # how to pass in 
                else:
                    time.sleep(1)
                    random_racer = racer_current_list[random.randint(0, len(racer_current_list)-1)]
                    player.place_bet(random_racer,player.num_bet)
                print(f"{player.name} has bet {player.num_bet} on {player.racer_bet.name}")
                # this will have to change lol
                #player.funds -= 50
                pot += player.num_bet
            
            # race
            '''
            eventually racers will have stats / win losses and things
            '''
            print('\n#### Racing Phase ####')
            #curr_winner = racer_current_list[random.randint(0,len(racer_current_list)-1)]
            newRace = RaceTrack(racer_current_list)
            winners = newRace.run()
            
            for winner in winners:
                print(f"{winner.name} wins!")
            
                # post race
                print('\n#### Post Race Phase ####')
                for player in player_list:
                    if player.racer_bet == winner:
                        round_winners.append(player)
            
            if len(round_winners) > 0:
                winnings = pot / len(round_winners)
                for player in round_winners:
                    # change it to net instead of total (since the money spent coming back isn't really winning)
                    player.funds += winnings
                    print(f'{player.name} won {winnings - player.num_bet} money!')
            else:
                print("no winners :'C")
            
            # current stats
            print("")
            for player in player_list:
                print(f"{player.name} has {player.funds} funds")
            
            time.sleep(2)
                    # divide the pot among players who won

            cur_round += 1

        print('betting season over!, play again w/ same settings or different?')
        # what things need to change / remain the same
        # name of player, which ones are computer


if __name__ == "__main__":
    main()