def safe(lst):
    inc = 1 if lst[1] > lst[0] else 0
    for i in range(1, len(lst)):
        if not 1 <= lst[i - (1 - inc)] - lst[i - inc] <= 3:
            return False
    return True

def safe2(lst):
    lists = [lst[:i] + lst[i+1:] for i in range(len(lst))]
    return True if any(map(safe, lists)) else False

with open("day2.txt", "r") as f:
    data = f.read().splitlines()
    data = [list(map(int, i.split())) for i in data]
    part1 = len(list(filter(safe, data)))
    print(part1)
    unsafe = list(filter(lambda x: not safe(x), data))
    part2 = len(list(filter(safe2, unsafe))) + part1
    print(part2)