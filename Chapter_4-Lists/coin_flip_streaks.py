"""Coin Flip Streaks"""

import random

numberOfStreaks = 0


for experimentNumber in range(10000):
    for flip in range(100):
        flip_list = []
        coin_side = random.randint(0, 1)
        if coin_side == 0:
            flip_list.append("H")
        else:
            flip_list.append("T")
    print(flip_list)


#print("Chance of streake: %s%%" % (numberOfStreaks / 100))
