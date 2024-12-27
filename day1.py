from collections import Counter

with open("day1.txt", "r") as f:
    # Part 1
    left, right = map(sorted, list(zip(*[list(map(int, line.split())) for line in f.read().splitlines()])))
    print(sum([abs(a - b) for a,b in zip(left, right)]))
    # Part 2
    cnt_left, cnt_right = Counter(left), Counter(right)
    print(sum([i * cnt_left[i] * cnt_right[i] for i in cnt_left.keys()]))