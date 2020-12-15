# with open("day_4.input", "r") as file:
#     input = file.read()

passports = []
passport = {}
for line in open("day_4.input", "r"):
    print(repr(line))
    if not line.strip():
        if passport:
            passports.append(passport)
            print(passport)
            passport = {}
    else:
        for kv in line.strip().split(" "):
            k, v = kv.split(":")
            passport[k] = v

if passport:
    passports.append(passport)
    print(passport)


import re


def valid_hgt(v):
    hgt, unit = int(v[:-2]), v[-2:]
    assert unit in {"cm", "in"}, f"{unit} not a valid unit"
    if unit == "cm":
        assert 150 <= hgt <= 193, f"{hgt}{unit} not a valid height"
    if unit == "in":
        assert 59 <= hgt <= 76, f"{hgt}{unit} not a valid height"


def valid_hcl(v):
    assert re.match(r"^#[0-9a-f]{6,6}$", v), f"{v} not a valid hcl"


def valid_ecl(v):
    assert v in {
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    }, f"{v} not a valid ecl"


def valid_pid(v):
    assert re.match(r"^[0-9]{9,9}$", v), f"{v} not a valid pid"


def validate_range(fr, to):
    def _validate(v):
        assert int(v) in range(fr, to), f"Out of range {v}, {fr}..{to}"

    return _validate


valid_keys = {
    "byr": validate_range(1920, 2003),  # (Birth Year)
    "iyr": validate_range(2010, 2021),  # (Issue Year)
    "eyr": validate_range(2020, 2031),  # (Expiration Year)
    "hgt": valid_hgt,  # (Height)
    "hcl": valid_hcl,  # (Hair Color)
    "ecl": valid_ecl,  # (Eye Color)
    "pid": valid_pid,  # (Passport ID)
    "cid": lambda _: True,  # (Country ID)
}

valid = 0

for passport in passports:
    print(".")
    wanted_keys = set(valid_keys.keys()) - {"cid"}

    is_valid = True

    if not all(key in passport for key in wanted_keys):
        print(f"Missing keys: {wanted_keys - set(passport.keys())}")
        is_valid = False

    for k, v in passport.items():
        try:
            valid_keys[k](v)
        except Exception as e:
            print(f"Error: {e}, ({k}:{v})")
            is_valid = False

    if is_valid:
        valid += 1
    else:
        print(f"Invalid passport {passport}")


print(f"Total: {len(passports)}, valid: {valid}")
