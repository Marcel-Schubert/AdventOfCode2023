with open("input/day05.txt", "r") as f:
    lines = f.read().split("\n\n")

initial_seeds, *maps = lines
initial_seeds = [int(x) for x in initial_seeds.split()[1:]]

mappings = []
for map in maps:
    map = map.splitlines()[1:]
    mapping = []
    for rng in map:
        mapping.append([int(x) for x in rng.split()])
    mapping.sort(key=lambda x: x[1])
    mappings.append(mapping)


def seed_to_location(x):
    for mapping in mappings:
        x = apply_mapping(mapping, x)
    return x


def apply_mapping(mapping, x):
    for dest, src, length in mapping:
        if src <= x < src + length:
            return dest - src + x
    return x


def apply_mapping_to_range(mapping, r_start, r_length):
    """Assumes that the ranges are sorted by ascending source start"""
    ranges = []
    for dest, src, length in mapping:
        if src > r_start:
            chunk_size = min(src - r_start, r_length)
            ranges.append((r_start, chunk_size))
            r_start += chunk_size
            r_length -= chunk_size
            if not r_length:
                break
        if src <= r_start < src + length:
            chunk_size = min(r_length, length - (r_start - src))
            ranges.append((dest + r_start - src, chunk_size))
            r_start += chunk_size
            r_length -= chunk_size
            if not r_length:
                break
    if r_length:
        ranges.append((r_start, r_length))
    return ranges


def seed_range_to_min_location(seed_ranges):
    current = seed_ranges
    for mapping in mappings:
        next = []
        for start, length in current:
            next += apply_mapping_to_range(mapping, start, length)
        current = next
    return min([start for start, _ in current])


locations = [seed_to_location(x) for x in initial_seeds]
part1 = min(locations)

seed_ranges = []
while initial_seeds:
    start, length, *initial_seeds = initial_seeds
    seed_ranges.append((start, length))

part2 = seed_range_to_min_location(seed_ranges)

print("Part 1:", part1)
print("Part 2:", part2)
