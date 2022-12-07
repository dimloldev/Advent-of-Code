import os
from collections import deque

with open(f"{os.path.join(os.path.split(os.getcwd())[0], 'Advent of Code/Day 6')}/input.txt", 'r') as file:
    counter = 0
    four_chars = deque([])
    while True:
        char = file.read(1)
        four_chars.append(char)
        if counter >= 14:  # Change 14 to 4 for part1
            four_chars.popleft()
        counter += 1
        if len(set(four_chars)) == 14:  # Change 14 to 4 for part1
            break
    print(counter)