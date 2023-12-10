with open("input/day10.txt") as f:
    lines = f.read().splitlines()

Pos = tuple[int, int]


def find_start_pos() -> Pos:
    for row, line in enumerate(lines):
        for col, symbol in enumerate(line):
            if symbol == "S":
                return row, col
    raise (ValueError("No starting position found."))


def replace_s_pos(pos: Pos):
    row, col = pos
    assert lines[row][col] == "S"
    possibilities = {x for x in "|-LJF7"}
    # below connects
    if row + 1 < len(lines) and lines[row + 1][col] in "|LJ":
        possibilities &= {x for x in "|F7"}
    # left connects
    if 0 <= col - 1 and lines[row][col - 1] in "-LF":
        possibilities &= {x for x in "-7J"}
    # above connects
    if 0 <= row - 1 and lines[row - 1][col] in "|7F":
        possibilities &= {x for x in "|LJ"}
    # right connects
    if col + 1 < len(lines[row]) and lines[row][col + 1] in "-J7":
        possibilities &= {x for x in "-LF"}
    if len(possibilities) != 1:
        raise (ValueError("Start position does not have exactly 2 possible neighbours."))
    replacement = possibilities.pop()
    lines[row] = lines[row][:col] + replacement + lines[row][col + 1 :]


def next_pos(pos: Pos) -> tuple[Pos, Pos]:
    row, col = pos
    symbol = lines[row][col]
    match symbol:
        case "|":
            return (row + 1, col), (row - 1, col)
        case "-":
            return (row, col + 1), (row, col - 1)
        case "L":
            return (row, col + 1), (row - 1, col)
        case "J":
            return (row, col - 1), (row - 1, col)
        case "7":
            return (row + 1, col), (row, col - 1)
        case "F":
            return (row + 1, col), (row, col + 1)
        case ".":
            raise ValueError("It should be possible to reach a . position.")
        case "S":
            replace_s_pos(pos)
            return next_pos(pos)


start_pos = find_start_pos()
replace_s_pos(start_pos)
open: list[Pos] = [start_pos]
closed: set[Pos] = set()

# BFS
while open:
    pos = open.pop(0)
    closed.add(pos)
    for other in next_pos(pos):
        if other not in open and other not in closed:
            open.append(other)

part1 = len(closed) // 2

part2 = 0
inside = False
for row, line in enumerate(lines):
    for col, symbol in enumerate(line):
        if (row, col) in closed:
            if symbol in "|F7":
                inside = not inside
        elif inside:
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
