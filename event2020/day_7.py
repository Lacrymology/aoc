from os import path
from parser import parse

curdir = path.dirname(__file__)


def parse_rule(v):
    # print(f"rule: {v}")
    outer, inner = v.split(" bags contain ")
    inner.strip(".")
    bags = []

    if inner != "no other bags.":
        bags_descs = inner.split(", ")
        # print(f"outer: {outer} [bags: {bags_descs}]")
        for bag_desc in bags_descs:
            num = int(bag_desc[0].strip())
            bag = bag_desc[1:].strip(" .")
            if bag.endswith("bags"):
                bag = bag[: -len("bags")]
            if bag.endswith("bag"):
                bag = bag[: -len("bag")]
            bags.append((bag.strip(" ."), num))
            # print(f"bag: {bag_desc}: ({num}, {bag})")

    ret = {outer: {bag: num for bag, num in bags}}

    # print(f"ret: {ret}")
    return ret


with open(path.join(curdir, "day_7.input")) as f:
    bag_rules = parse(f, parse_rule)

rules = {}

for bag in bag_rules:
    rules.update(bag)

# print(rules)

can_contain_gold = set()

cont = True

while cont:
    cont = False
    for bag, bag_rules in rules.items():
        # print(f"test {bag} with {bag_rules}")
        if "shiny gold" in bag_rules or any(
            b in can_contain_gold for b in bag_rules.keys()
        ):
            if bag not in can_contain_gold:
                # print(f"add {bag} because {bag_rules}")
                cont = True
                can_contain_gold.add(bag)
                # print(f"can contain: {can_contain_gold}")

print(len(can_contain_gold))


def needs_to_contain(bag, rules):
    """return the number of bags this bag needs to contain"""
    total = 0
    print(f"bag: {bag}, rule: {rules[bag]}")
    for ibag, cnt in rules[bag].items():
        print(f"ibag: {ibag}, cnt: {cnt}")
        total += cnt * (needs_to_contain(ibag, rules) + 1)
    print(f"returning {total} for {bag}")
    return total


print(needs_to_contain("shiny gold", rules))