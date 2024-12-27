from collections import defaultdict

def swap(d, i, j):
    tmp = d[i]
    d[i] = d[j]
    d[j] = tmp

with open("day5.txt", "r") as f:
    data = f.read().split('\n\n')
    rules = data[0].splitlines()
    updates = data[1].splitlines()

    m = defaultdict(list)
    for rule in rules:
        k, v = rule.split("|")
        m[k].append(v)

    updates = [i.split(",") for i in updates]
    incorrect = []

    # Part 1
    sm = 0
    for update in updates:
        for i in range(len(update)):
            for j in range(i):
                if update[j] in m[update[i]]:
                    break
            else:
                continue
            incorrect.append(update)
            break
        else:
            sm += int(update[int((len(update) - 1) / 2)])
    print(sm)

    # Part 2
    sm = 0
    for update in incorrect:
        i = 0
        while i < len(update):
            for j in range(i):
                if update[j] in m[update[i]]:
                    swap(update, i, j)
                    i = 0
                    break
            i += 1
        sm += int(update[int((len(update) - 1) / 2)])
    print(sm)