with open("input/day06.txt", "r") as f:
    times, distances = f.read().splitlines()
    
times = [int(x) for x in times.split()[1:]]
distances = [int(x) for x in distances.split()[1:]]

def compute_distance(time_pressed, time_total):
    return time_pressed * (time_total - time_pressed)

part1 = 1
for time, distance in zip(times, distances):
    wins = [i for i in range(time+1) if compute_distance(i, time) > distance]
    part1 *= len(wins)

time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))

print("Part 1:", part1)
part2 = len([i for i in range(time+1) if compute_distance(i, time) > distance])
print("Part 2:", part2)