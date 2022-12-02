with open(r"C:\Users\agapo\Documents\University\Year 1\Module 2\Advent of Code\Day 2\input.txt", "r") as f:
    file = f.read()

#Part 1
choice = ""
win = 6
draw = 3
sum = 0

for i in file.splitlines():
    x = i.split(None, 2)
    if x[0] == "A" and x[1] == "X":
        sum += 1
        sum += draw
    elif x[0] == "A" and x[1] == "Y":
        sum += 2
        sum += win
    elif x[0] == "A" and x[1] == "Z":
        sum += 3
    elif x[0] == "B" and x[1] == "X":
        sum += 1
    elif x[0] == "B" and x[1] == "Y":
        sum += 2
        sum += draw
    elif x[0] == "B" and x[1] == "Z":
        sum += 3
        sum += win
    elif x[0] == "C" and x[1] == "X":
        sum += 1
        sum += win
    elif x[0] == "C" and x[1] == "Y":
        sum += 2
    elif x[0] == "C" and x[1] == "Z":
        sum += 3
        sum += draw

print ("Part 1: " + str(sum))

#Part 2
sum = 0
for i in file.splitlines():
    x = i.split(None, 2)
    if x[0] == "A" and x[1] == "X":
        sum += 3
    elif x[0] == "A" and x[1] == "Y":
        sum += 1
        sum += draw
    elif x[0] == "A" and x[1] == "Z":
        sum += 2
        sum += win
    elif x[0] == "B" and x[1] == "X":
        sum += 1
    elif x[0] == "B" and x[1] == "Y":
        sum += 2
        sum += draw
    elif x[0] == "B" and x[1] == "Z":
        sum += 3
        sum += win
    elif x[0] == "C" and x[1] == "X":
        sum += 2
    elif x[0] == "C" and x[1] == "Y":
        sum += 3
        sum += draw
    elif x[0] == "C" and x[1] == "Z":
        sum += 1
        sum += win

print ("Part 2: " + str(sum))