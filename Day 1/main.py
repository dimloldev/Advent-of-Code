with open(r"C:\Users\agapo\Documents\University\Year 1\Module 2\Advent of Code\Day 1\input.txt", "r") as f:
    file = f.read()

sum = 0
high = 0
mid = 0
low = 0
temp = 0

for i in file.splitlines():
    if i != '':
        sum += int(i)
    else:
        if sum > high:
            temp = high
            high = sum
            mid = temp
        elif sum > mid:
            temp = mid
            mid = sum
            low = temp
        elif sum > low:
            low = sum
        sum = 0
print(high + mid + low)