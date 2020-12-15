from parser import parse


def fbrltobin(v):
    for pair in [("F", "0"), ("B", "1"), ("L", "0"), ("R", "1")]:
        v = v.replace(*pair)

    return int(v, 2)


with open("day_5.input") as f:
    values = parse(f, fbrltobin)

print(max(values))

values = sorted(values)
print(values)

for ix, val in enumerate(values[1:-1], 1):
    if values[ix - 1] != val - 1 or values[ix + 1] != val + 1:
        print(val)
