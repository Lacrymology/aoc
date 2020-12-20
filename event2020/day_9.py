from os import path
from parser import parse
from itertools import combinations

curdir = path.dirname(__file__)

with open(path.join(curdir, "day_9.input")) as f:
    cypher = parse(f, int)


def is_sum(data: list, index: int):
    """
    Returns whether the value of `data` at `index` is the sum of 2 of the previous 25 values
    """
    val = data[index]
    slice = data[index - 25 : index]
    # print(f"is_sum({val}, {slice}) (len: {len(slice)}")
    for a, b in combinations(data[index - 25 : index], 2):
        # print(f"a: {a} + b: {b} = {a + b}")
        if a != b:
            if a + b == data[index]:
                return True
    # print("not sum")
    return False


def part_1():
    for ix, val in enumerate(cypher[25:], 25):
        # print(f"=============")
        # print(f"Test {val} in {ix}")
        if not is_sum(cypher, ix):
            return val


def part_2():
    invalid = part_1()
    start = 0
    end = 1

    while start < len(cypher):
        # print(f"test {start}:{end}")
        slice = cypher[start:end]
        total = sum(slice)
        if total == invalid:
            return min(slice), max(slice)
        if total > invalid:
            start += 1
            end = start + 1
        else:
            end += 1


print(f"Part 1: {part_1()}")
print(f"Part 2: {sum(part_2())}")