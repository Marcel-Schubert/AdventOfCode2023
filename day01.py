with open("input/day01.txt", "r") as f:
    lines = f.readlines()

digit_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_digit(line: str, first: bool, allow_words: bool) -> str:
    positions = range(len(line))
    if not first:
        positions = reversed(positions)
    for i in positions:
        if line[i].isdigit():
            return line[i]
        if allow_words:
            for digit_word, digit in digit_words.items():
                if line[i:].startswith(digit_word):
                    return digit
    raise ValueError("Line does not contain any digit.")


part1 = sum((int(get_digit(line, first=True, allow_words=False) +
            get_digit(line, first=False, allow_words=False))for line in lines))
part2 = sum((int(get_digit(line, first=True, allow_words=True) +
            get_digit(line, first=True, allow_words=True))for line in lines))


print("Part 1:", part1)
print("Part 2:", part2)
