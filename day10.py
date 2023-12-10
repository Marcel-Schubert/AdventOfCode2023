with open("input/day10.txt") as f:
    lines = f.read().splitlines()

Pos = tuple[int, int]


def find_start_pos() -> Pos:
    for row, line in enumerate(lines):
        for col, symbol in enumerate(line):
            if symbol == "S":
                return row, col
    raise (ValueError("No starting position found."))


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
            positions: list[Pos] = []
            if row + 1 < len(lines) and lines[row + 1][col] in "|LJ":
                positions.append((row + 1, col))
            if 0 <= col - 1 and lines[row][col - 1] in "-LF":
                positions.append((row, col - 1))
            if 0 <= row - 1 and lines[row - 1][col] in "|7F":
                positions.append((row - 1, col))
            if col + 1 < len(lines[row]) and lines[row][col + 1] in "-J7":
                positions.append((row, col + 1))
            if len(positions) != 2:
                raise (ValueError("Start position does not have exactly 2 possible neighbours."))
            return positions[0], positions[1]


open: list[Pos] = [find_start_pos()]
closed: set[Pos] = set()

# BFS
while open:
    pos = open.pop(0)
    closed.add(pos)
    for other in next_pos(pos):
        if other not in open and other not in closed:
            open.append(other)

part1 = len(closed) // 2

print("Part 1:", part1)
