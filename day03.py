from collections import defaultdict

with open("input/day03.txt", "r") as f:
    lines: list[str] = f.read().splitlines()


def is_part(row, start, end):
    def is_symbol(row, col) -> bool:
        if not (0 <= row < len(lines)):
            return False
        if not (0 <= col < len(lines[row])):
            return False
        char = lines[row][col]
        return char != "." and not char.isdigit()

    # row above
    if any(is_symbol(row-1, i) for i in range(start-1, end+1)):
        return True
    # same row
    if is_symbol(row, start-1) or is_symbol(row, end):
        return True
    # row below
    if any(is_symbol(row+1, i) for i in range(start-1, end+1)):
        return True
    return False


def add_to_adjacent_stars(num, row, start, end):
    def is_star(row, col):
        if not (0 <= row < len(lines)):
            return False
        if not (0 <= col < len(lines[row])):
            return False
        return lines[row][col] == "*"

    # row above
    for i in range(start-1, end+1):
        if is_star(row-1, i):
            star_adjacent_numbers[(row-1, i)].append(num)
    # same row
    if is_star(row, start-1):
        star_adjacent_numbers[(row, start-1)].append(num)
    if is_star(row, end):
        star_adjacent_numbers[(row, end)].append(num)
    # row below
    for i in range(start-1, end+1):
        if is_star(row+1, i):
            star_adjacent_numbers[(row+1, i)].append(num)


star_adjacent_numbers = defaultdict(lambda: [])

part1 = 0
for i, line in enumerate(lines):
    scanning_num: bool = False
    for j, char in enumerate(line):
        if char.isdigit():
            if not scanning_num:
                scanning_num = True
                num = ""
                start_pos = j
            num += char
        else:
            if scanning_num:
                scanning_num = False
                end_pos = j
                if is_part(i, start_pos, end_pos):
                    part1 += int(num)
                add_to_adjacent_stars(int(num), i, start_pos, end_pos)
    if scanning_num:
        scanning_num = False
        end_pos = len(line)
        if is_part(i, start_pos, end_pos):
            part1 += int(num)
        add_to_adjacent_stars(int(num), i, start_pos, end_pos)

part2 = 0
for numbers in star_adjacent_numbers.values():
    if len(numbers) == 2:
        part2 += numbers[0] * numbers[1]

print("Part 1:", part1)
print("Part 2:", part2)
