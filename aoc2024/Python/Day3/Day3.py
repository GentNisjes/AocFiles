import re


with open("input.txt", 'r') as f:
    lines = f.readlines()  

arr = []
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

for line in lines:
    #arr.append(re.findall(pattern, line))
    print("without arr: ", re.findall(pattern, line))

# print(arr)
