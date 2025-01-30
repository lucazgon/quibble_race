import os
import time
from enum import Enum
from racer import Racer

class RaceTrack():
    def __init__(self,racers):
        self.racers = racers
        pass
    def run(self):
        race = True
        winners = []

        while race == True:
            self.length = 20
            self.rows =[]

            #os.system('clear')
            #build track
            for racer in self.racers:
                if racer.x >= self.length:
                    #print("ENDRACE")
                    racer.x = self.length -1
                    winners.append(racer)
                    race = False

                row = []
                for i in range (0,self.length):
                    row.append("-")
                row[0] = "+"
                row[-1] = '#'
                row[racer.x] = f'{racer.name[0]}'
                row.append("|")
                row.append(racer.name)
                self.rows.append("".join(row))

                if race == False:
                    break
                #hmmm
                racer.update()
            
            for row in self.rows:
                print(row)
            
            #racer.update()
            time.sleep(.5)
            #print('suck me')
            #return winners
            '''
            build an empty track with a start and finish symbol
            take tHE x position of the racer and the first letter, num racers also
            '''
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
    my_track = RaceTrack(racer_list).run()
    #print("\033[0;33mbold red text\033[0m\n")
