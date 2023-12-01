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


def first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char
    raise ValueError("Line does not contain any digit.")


def last_digit(line: str) -> str:
    for char in reversed(line):
        if char.isdigit():
            return char
    raise ValueError("Line does not contain any digit.")

def first_digit_or_word(line: str) -> str:
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for digit_word, digit in digit_words.items():
            if line[i:].startswith(digit_word):
                return digit
    raise ValueError("Line does not contain any digit.")


def last_digit_or_word(line: str) -> str:
    for i in reversed(range(len(line))):
        if line[i].isdigit():
            return line[i]
        for digit_word, digit in digit_words.items():
            if line[i:].startswith(digit_word):
                return digit
    raise ValueError("Line does not contain any digit.")


part1 = sum((int(first_digit(line) + last_digit(line)) for line in lines))
part2 = sum((int(first_digit_or_word(line) + last_digit_or_word(line)) for line in lines))


print("Part 1:", part1)
print("Part 2:", part2)
