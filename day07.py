from collections import Counter

with open("input/day07.txt", "r") as f:
    lines = f.read().splitlines()

games = {hand: int(bid) for hand, bid in (line.split() for line in lines)}

SYMBOLS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def get_symbol_rank(symbol):
    SYMBOLS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    return SYMBOLS.index(symbol)

def get_symbol_rank_p2(symbol):
    SYMBOLS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    return SYMBOLS.index(symbol)

def get_hand_type(hand: str, p2: bool = False) -> int:
    counter = Counter(hand)
    num_jokers = 0
    if p2:
        num_jokers = counter["J"]
        counter["J"] = 0
    c1, *c2 = counter.most_common(2)
    count1 = c1[1] + num_jokers
    count2 = c2[0][1] if c2 else 0
    match count1, count2:
        case 5, 0:
            return 1
        case 4, 1:
            return 2
        case 3, 2:
            return 3
        case 3, 1:
            return 4
        case 2, 2:
            return 5
        case 2, 1:
            return 6
        case 1, 1:
            return 7
    raise ValueError("Hand did not match any type.")
    
ordered = sorted(list(games.keys()), reverse=True, key = lambda hand: (get_hand_type(hand), [get_symbol_rank(c) for c in hand]))
ordered_p2 = sorted(list(games.keys()), reverse=True, key = lambda hand: (get_hand_type(hand, p2=True), [get_symbol_rank_p2(c) for c in hand]))
part1 = sum((rank * games[hand] for rank, hand in enumerate(ordered, start=1)))
part2 = sum((rank * games[hand] for rank, hand in enumerate(ordered_p2, start=1)))

print("Part 1:", part1)
print("Part 2:", part2)