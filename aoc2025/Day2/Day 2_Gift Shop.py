class Solver:
    def __init__(self, input_file):
        self.data = self.load_input(input_file)
    
    def load_input(self, filename):
        """Helper to read and parse input"""
        with open(filename) as f:
            return f.read().strip().split(',')
    
    def part1(self):
        """Solve part 1"""
        range_str = ""
        code = 0
        for range_str in self.data:
            start, end = map(int, range_str.split('-'))
            for number in range(start, end + 1):
                num_str = str(number)
                length = len(num_str)
                
                # Even-length numbers: Check if halves are equal
                if length % 2 == 0:
                    half = length // 2
                    if num_str[:half] == num_str[half:]:
                        code += int(num_str)
                
                # Odd-length numbers should be ignored as per the original logic (pt1)
                # else:
                #     if (len(set(num_str)) == 1) and (len(num_str) != 1): 
                #         code += int(num_str)
                
        return code
    
    def part2(self):
        """Solve part 2"""
        pass

# Usage:
solver = Solver('input.txt')
print(solver.part1())
print(solver.part2())