
def get_neighbours(x, y, X, Y):
    result = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            tmp = []
            for k in range(4):
                if not (0 <= x + i * k < X and 0 <= y + j * k < Y):
                    break
                tmp.append((x + i * k, y + j * k))
            else:
                result.append(tmp)
    return result

def get_neighbours2(x, y):
    return [(x, y), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]


with open("day4.txt", "r") as f:
    data = [list(i) for i in f.read().splitlines()]

    # Part 1
    count = 0
    Y = len(data)
    X = len(data[0])
    for y in range(Y):
        for x in range(X):
            for indices in get_neighbours(x, y, X, Y):
                word = "".join([data[y_][x_] for x_, y_ in indices])
                if word == "XMAS":
                    count += 1
    print(count)

    # Part 2
    count = 0
    for y in range(1, Y - 1):
        for x in range(1, X - 1):
            word = "".join([data[y][x] for x, y in get_neighbours2(x, y)])
            if word in ["AMMSS", "ASSMM", "ASMSM", "AMSMS"]:
                count += 1
    print(count)