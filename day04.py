import re
from collections import Counter

with open("input/day04.txt", "r") as f:
    lines = f.read().splitlines()
    
part1 = 0
wins = dict()
for line in lines:
    match = re.match(r"Card\s*(\d*): (.*) \| (.*)", line)
    if match:
        id, winning, have = match.groups()
        winning = {int(x) for x in winning.split()}
        have = {int(x) for x in have.split()}
        tickets_won = winning & have
        wins[int(id)] = len(tickets_won)
        if tickets_won:
            part1 += 2 ** (len(tickets_won) - 1) 

cards = Counter()
for card in wins:
    cards[card] += 1
    
MAX_CARDS = len(wins) + 1

def add_cards(card):
    for copy in range(card + 1, min(card + wins[card] + 1, MAX_CARDS+1)):
        cards[copy] += 1

for card in cards.elements():
    add_cards(card)
    

print("Part 1:", part1)
print("Part 2:", cards.total())