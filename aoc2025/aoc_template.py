class Solver:
    def __init__(self, input_file):
        self.data = self.load_input(input_file)
    
    def load_input(self, filename):
        """Helper to read and parse input"""
        with open(filename) as f:
            return f.read().strip()
    
    def part1(self):
        """Solve part 1"""
        pass
    
    def part2(self):
        """Solve part 2"""
        pass

# Usage:
solver = Solver('input.txt')
print(solver.part1())
print(solver.part2())