import re


with open("/Users/Stijn/OneDrive - KU Leuven/PERSONAL/Rommel/AocFiles/aoc2024/Python/Day3/input.txt", 'r') as f:
    lines = f.readlines()  

arr = []
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
print(lines)

for line in lines:
    arr.append(re.findall(pattern, line))


