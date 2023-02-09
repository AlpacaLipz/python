# Project by Randy, Peyton and Miguel

from classes.ninja import Ninja
from classes.pirate import Pirate
import random

jackie_chan = Ninja("Jackie Chan")

jack_sparrow = Pirate("Jack Sparrow")

while jackie_chan.health > 0 and jack_sparrow.health > 0:
    print("Jackie Chan squares up on a drunk Jack Sparrow")
    response = ""

    while not response == "1" and not response == "2":
        response = input('What does Jackie Chan do?\n 1.) Throw Hands?\n 2.) Dodge/Weave\n >>>')

        if response == "1":
            jackie_chan.attack(jack_sparrow)
        elif response == "2":
            jackie_chan.counter(jack_sparrow)
        else:
            print(">>> Jackie Chan doesn't run away PICK AGAIN!!")


        dice_roll = random.randint(1,2)
        if dice_roll == 1:
            jack_sparrow.attack(jackie_chan)
        else: 
            jack_sparrow.counter(jackie_chan)

# print("Jackie Chan", jackie_chan.health)
# print("Jack Sparrow", jack_sparrow.health)
if jackie_chan.health > 0:
    print("Your hands prevailed!!")
if jack_sparrow.health > 0:
    print("Your hands failed!!")
if jack_sparrow.health > 0 and jackie_chan.health > 0:
    print("Double Fatality, there's no winners in ninjas vs pirates")

