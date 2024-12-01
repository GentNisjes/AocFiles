file = open("aoc-day1.txt")

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
word_list = ["zero", 0, "one", 1, "two", 2, "three", 3, "four", 4, "five", 5, "six", 6, "seven", 7, "eight", 8, "nine", 9]
num_array = []
line_count = 0
number_count = 0
total_count = 0
number_string = ""
string = ""

for line in file:
    num_array = []
    
    for char in line:
        if char in num_list:
            num_array.append(int(char))
        else:
            string += char
            if string in word_list:
                index = word_list.index(string)
                string = ""
                num_array.append(int(word_list[index + 1]))
        
        print(num_array)


    if len(num_array) == 1:
        number_count += int(num_array[0])
        print("the number count at line " + str(line_count) + " is : " + str(number_count))

    elif not num_array:             # or len(num_array) == 0:
        number_count += 0
        print("the number count at line " + str(line_count) + " is : zero")

    else:
        first_number = num_array[0]
        second_number = num_array[len(num_array) - 1]
        number_string = str(first_number) + str(second_number)
        

        number_count += int(number_string)
        print("the number count at line " + str(line_count) + " is : " + str(number_count))

    line_count += 1
    total_count += number_count
    print("the total count equals to: " + str(total_count))
    number_count = 0
    

print (total_count)