file = open("")


# Part 1 

left_list = []
right_list = []

# line_count = 0

for line in file:
    line = line.strip()
    parts = line.split()
    left_list.append(parts[0])
    right_list.append(parts[1])

# # print("left list: ", left_list)
# # print("right list: ", right_list) 

# left_list.sort()
# right_list.sort()

# print("left list: ", left_list)
# print("right list: ", right_list) 

# total_sum = 0

# for i in range(0,len(left_list)):
#     if (left_list[i] > right_list[i]):
#         total_sum += int(left_list[i]) - int(right_list[i])
#     else:
#         total_sum += int(right_list[i]) - int(left_list[i])

# print(total_sum)

# Part 2

multiplicators = [0] * len(left_list)
total_mult = 0

for i in range(0,len(left_list)):
    number = left_list[i]
    for comp_num in right_list:
        if comp_num == number: multiplicators[i] += 1
    
    total_mult += multiplicators[i] * int(left_list[i])

# print(multiplicators)
print(total_mult)


