import time
import numpy as np
import sys

#delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/924076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
# Create the class
class pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defence = EVs['DEFENCE']
        self.bars = 20 # Amount of health bars
        
        
        
    def fight(self, pokemon2):
        # Allow two pokemon to fight each other
        
        # print fight information
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENCE/" self.defence)
        print("LVL/", 3*(1+np.mean([self.attack, self.defence])))
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("TYPE/", pokemon2.types)
        print("ATTACK/", pokemon2.attack)
        print("DEFENCE/" pokemon2.defence)
        print("LVL/", 3*(1+np.mean([pokemon2.attack, pokemon2.defence])))
        print("\nVS")
        
        time.sleep(2)
        
        # consider type advantages
        version = ["fire", "water", "grass"]

if __name__ '__main':
    pass