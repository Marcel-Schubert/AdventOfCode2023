with open("input/day09.txt", "r") as f:
    lines = f.read().splitlines()

part1 = 0
part2 = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    diffs = [[y - x for x, y in zip(nums[:-1], nums[1:])]]
    while any([x != 0 for x in diffs[-1]]):
        diffs.append([y - x for x, y in zip(diffs[-1][:-1], diffs[-1][1:])])
    for diff_low, diff_high in zip(reversed(diffs[1:]), reversed(diffs[:-1])):
        diff_high.insert(0, diff_high[0] - diff_low[0])
        diff_high.append(diff_high[-1] + diff_low[-1])
    prev_num = nums[0] - diffs[0][0]
    next_num = nums[-1] + diffs[0][-1]
    # for diff in diffs:
    #     print(diff)
    # print(prev_num, next_num)
    part1 += next_num
    part2 += prev_num

print("Part 1:", part1)
print("Part 2:", part2)
