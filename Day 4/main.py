with open(r"C:\Users\agapo\Documents\University\Year 1\Module 2\Advent of Code\Day 4\input.txt", "r") as f:
    file = f.read()

#Part 1
sum = 0

for line in file.splitlines():
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    if a <= x and b >= y or x <= a and y >= b:
        sum += 1

print("Part 1: " + str(sum))

#Part 2
sum = 0

for line in file.splitlines():
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    if set(range(a, b + 1)) & set(range(x, y + 1)):
        sum += 1

print("Part 2: " + str(sum))