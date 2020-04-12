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
'''
    temp_list = []

    for value in flip_list:
        if len(temp_list) == 0:
            temp_list.append(value)
        elif value in temp_list and len(temp_list) < 6:
            temp_list.append(value)
        elif len(temp_list) == 6:
            numberOfStreaks += 1
            del temp_list[:]
'''
for c in range(len(flip_list)):
    current = checker
    checker = flip_list[c]
    if current == checker:
        counter += 1
    elif current != checker:
        counter = 0
    if counter == 6:
        numberOfStreaks += 1


print("Chance of streake: %s%%" % (numberOfStreaks / 100))
