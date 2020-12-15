from parser import parse


def parse_group(v):
    return [set(a for a in person) for person in v.strip().split("\n")]


with open("day_6.input") as f:
    groups = parse(f.read().split("\n\n"), parse_group)

# for group in groups:
#     print(group)


group_answers = []
for group in groups:
    union = group[0]
    for person in group[1:]:
        union = union | person
    group_answers.append(union)

print(sum(len(group) for group in group_answers))

all_yes = []

for group in groups:
    intersect = group[0]
    for person in group[1:]:
        intersect = intersect & person
    all_yes.append(intersect)

print(sum(len(group) for group in all_yes))
