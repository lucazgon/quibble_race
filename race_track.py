import os
import time
from enum import Enum
from racer import Racer

class RaceTrack():
    def __init__(self,racers):
        self.racers = racers
        self.render = True
        pass
    def run(self):
        race = True
        winners = []

        while race == True:
            self.length = 20
            self.rows =[]

            #build track
            for racer in self.racers:
                # if the racer passed the goal w/ how fast their going
                if racer.x >= self.length:
                    racer.x = self.length -1
                    winners.append(racer)
                    race = False

                # build race track string
                row = []
                for i in range (0,self.length):
                    row.append("-")
                row[0] = "+"
                row[-1] = '#'
                row[racer.x] = f'{racer.name[0]}'

                # generate the names of racers / info
                row.append("|")
                row.append(racer.name)
                self.rows.append("".join(row))

                if race == False:
                    break
                racer.update()
            
            # render race track
            if self.render == True:
                os.system('clear')
                for row in self.rows:
                    print(row)
                time.sleep(.5)
        
        for winner in winners:
            winner.wins += 1
        for racer in self.racers:
            racer.games_played += 1
        return winners
        
        

# just junk
def color_text(text_input,color):
    return f"\033[1;{color}m{text_input}\033[0m\n"
    pass

class TerminalColors(Enum):
    CYAN = 36
    MAGENTA = 35
    YELLOW = 33

if __name__ == "__main__":

    a = Racer()
    b = Racer()
    c = Racer()
    a.x = 3
    c.x = 5
    racer_list = [a,b,c]
    my_track = RaceTrack(racer_list)
    my_track.render = False
    print(my_track.run())
    #print("\033[0;33mbold red text\033[0m\n")
