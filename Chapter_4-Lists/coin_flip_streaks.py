"""Coin Flip Streaks"""

import random

numberOfStreaks = 0
counter = 0
current = None
checker = None

for experimentNumber in range(10000):
    flip_list = []
    for flip in range(100):
        coin_side = random.randint(0, 1)
        if coin_side == 0:
            flip_list.append("H")
        else:
            flip_list.append("T")

    for value in flip_list:
        if current is None:
            current = value
            counter += 1
        else:
            checker = value
            if current == checker:
                current = checker
                counter += 1
            else:
                current = checker
                counter = 0
        if counter == 6:
            numberOfStreaks += 1
            counter = 0

print("Chance of streake: %s%%" % (numberOfStreaks / 100))
