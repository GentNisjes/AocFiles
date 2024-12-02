with open("input.txt", 'r') as f:
    lines = f.readlines()  

left_list = []
right_list = []

for line in lines:
    line = line.strip()
    parts = line.split()
    left_list.append(int(parts[0]))
    right_list.append(int(parts[1]))

# Part 1: Calculating the total sum
total_sum = 0

for a, b in zip(left_list, right_list):  # Loop through both lists simultaneously
    total_sum += abs(a - b)

print("Part 1 Total Sum:", total_sum)

# Part 2: calculate multiplicators
total_mult = 0

for number in left_list:
    count = right_list.count(number)  
    total_mult += count * number

print("Part 2 Total Multiplicators Sum:", total_mult)
