from itertools import combinations

with open("input/day11.txt") as f:
    lines = [[x for x in line] for line in f.read().splitlines()]

Pos = tuple[int, int]


def is_empty_col(col: int) -> bool:
    assert 0 <= col < len(lines[0])
    return all([line[col] == "." for line in lines])


def is_empty_row(row: int) -> bool:
    assert 0 <= row < len(lines)
    return all([x == "." for x in lines[row]])


def add_empty_cols(cols: list[int]):
    cols = sorted(cols, reverse=True)
    for line in lines:
        for col in cols:
            line.insert(col, ".")


def add_empty_rows(rows: list[int]):
    rows = sorted(rows, reverse=True)
    for row in rows:
        lines.insert(row, ["."] * len(lines[0]))


def expand_space():
    empty_cols = [i for i in range(len(lines[0])) if is_empty_col(i)]
    empty_rows = [i for i in range(len(lines)) if is_empty_row(i)]
    add_empty_cols(empty_cols)
    add_empty_rows(empty_rows)


def manhattan_dist(p1: Pos, p2: Pos) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


expand_space()
galaxies = []
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == "#":
            galaxies.append((row, col))

part1 = sum([manhattan_dist(p1, p2) for p1, p2 in combinations(galaxies, 2)])

print("Part 1:", part1)
