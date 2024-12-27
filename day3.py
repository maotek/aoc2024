import re

with open("day3.txt", "r") as f:
    data = "".join(f.read().splitlines())
    print(data)
    result = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    print(sum([int(a) * int(b) for a, b in result]))
    result = re.subn(r"don't\(\).*?(do\(\)|$)", "",  data)
    result = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", result[0])
    print(sum([int(a) * int(b) for a, b in result]))