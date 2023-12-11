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


empty_cols = [i for i in range(len(lines[0])) if is_empty_col(i)]
empty_rows = [i for i in range(len(lines)) if is_empty_row(i)]


def distance(p1: Pos, p2: Pos, space_expansion: int = 2) -> int:
    r1, c1 = p1
    r2, c2 = p2
    # we do not care if r1 or r2 is included, since this line can never be empty
    dist = 0
    if r1 > r2:
        r1, r2 = r2, r1
    for i in range(r1, r2):
        dist += space_expansion if i in empty_rows else 1
    if c1 > c2:
        c1, c2 = c2, c1
    for i in range(c1, c2):
        dist += space_expansion if i in empty_cols else 1
    return dist


galaxies = []
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == "#":
            galaxies.append((row, col))

part1 = sum([distance(p1, p2) for p1, p2 in combinations(galaxies, 2)])
part2 = sum([distance(p1, p2, 1_000_000) for p1, p2 in combinations(galaxies, 2)])

print("Part 1:", part1)
print("Part 2:", part2)
