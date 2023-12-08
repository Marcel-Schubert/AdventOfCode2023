import re
from math import lcm
with open("input/day08.txt", "r") as f:
    lines = f.read().splitlines()

instructions, _, *lines = lines
map = dict()
for line in lines:
    mat = re.match(r"(...) = \((...), (...)\)", line)
    if mat is not None:
        key, left, right = mat.groups()
        map[key] = (left, right)

def get_instruction(i):
    return 0 if instructions[i%len(instructions)] == "L" else 1

pos = 'AAA'
part1 = 0
while pos != 'ZZZ':
    pos = map[pos][get_instruction(part1)]
    part1 += 1
    
positions =  [pos for pos in map if pos[-1] == "A"]
cycles = []
for p1 in positions:
    z_offset = []
    i = 0
    p2 = map[p1][get_instruction(i)]
    i += 1
    in_cycle = False
    while p2 != p1:
        if p2[-1] == "Z":
            cycles.append(i)
            break
        p2 = map[p2][get_instruction(i)]
        i += 1
part2 = lcm(*cycles)
    
print("Part 1:", part1)
print("Part 2:", part2)