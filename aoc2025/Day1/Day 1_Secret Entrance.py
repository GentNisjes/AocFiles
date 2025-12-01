import math


class Solver:
    def __init__(self, input_file):
        self.data = self.load_input(input_file)
    
    def load_input(self, filename):
        """Helper to read and parse input"""
        with open(filename, "r") as f:
            return [line.strip() for line in f]
    
    def part1(self):
        """Solve part 1"""
        dial_position = 50
        code = 0
        for move in self.data:
            # direction, steps = move[:1], move[1:]
            # steps = int(steps)
            # if direction == "L":
            #     dial_position = (dial_position - steps) % 100
            # elif direction == "R":
            #     dial_position = (dial_position + steps) % 100
            # if dial_position == 0:
            #     code += 1
            # else:
            #     code += 0

            direction, steps = move[0], int(move[1:])
            dial_position = (dial_position + (steps if direction == "R" else -steps)) % 100
            code += (dial_position == 0)

        return code
    
    def part2(self):
        """Solve part 2"""
        dial_position = 50
        code = 0
        for move in self.data:
            direction, steps = move[0], int(move[1:])
            code += steps // 100 # handle the full rotations
            
            if direction == "R":
                if (dial_position + steps) % 100 < dial_position:
                    code += 1
            else:  # L
                if ((dial_position - steps) % 100 > dial_position) and (dial_position != 0):
                    code += 1
                elif (dial_position - steps) % 100 == 0:
                    code += 1

            dial_position = (dial_position + (steps if direction == "R" else -steps)) % 100

        return code

# Usage:
solver = Solver('input.txt')
print(solver.part1())
print(solver.part2())