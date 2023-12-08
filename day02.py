import re
from math import prod

with open("input/day02.txt", "r") as f:
    lines = f.readlines()

color_max = {"red": 12, "green": 13, "blue": 14}


def build_game_dicts(game_str: str) -> list[dict[str, int]]:
    game_dicts: list[dict[str, int]] = []
    game: list[str] = game_str.split("; ")
    for reveal in game:
        reveal = reveal.split(", ")
        d = {}
        for color_count in reveal:
            count, color = color_count.split()
            d[color] = int(count)
        game_dicts.append(d)
    return game_dicts


def parse_line(line: str) -> None:
    if not line:
        return
    match = re.match(r"Game (\d+): (.*)", line)
    if match is None:
        raise ValueError("Line was invalid")
    game_id, game = match.groups()
    game_id = int(game_id)
    games[game_id] = build_game_dicts(game)


def is_possible(game: list[dict[str, int]]) -> bool:
    for reveal in game:
        for color, count in reveal.items():
            if count > color_max[color]:
                return False
    return True


def get_power(game: list[dict[str, int]]) -> int:
    return prod(max(reveal[color] for reveal in game if color in reveal) for color in color_max)


games: dict[int, list[dict[str, int]]] = dict()
for line in lines:
    parse_line(line)

part1 = sum(game_id for game_id, game in games.items() if is_possible(game))
part2 = sum(get_power(game) for _, game in games.items())

print("Part 1:", part1)
print("Part 2:", part2)
