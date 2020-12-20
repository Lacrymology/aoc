from os import path
from parser import parse

curdir = path.dirname(__file__)


class InfiniteLoopError(Exception):
    """
    To be raised when a program detects an infinite loop
    """

    def __init__(self, cp, accum):
        self.cp = cp
        self.accum = accum

    def __str__(self):
        print(f"Infinite Loop Detected: cp: {self.cp}, acc: {self.accum}")


class Process:
    def __init__(self, code: list):
        self._code = code

        self._accum = 0
        self._cp = 0
        self._visited_instrs = set()

        self._fixed = False

    def execute(self):
        while 0 <= self._cp < len(self._code):
            if self._cp in self._visited_instrs:
                raise InfiniteLoopError(self._cp, self._accum)

            self._visited_instrs.add(self._cp)
            self.execute_next()
        return self._accum

    def execute_next(self):
        instr, param = self._code[self._cp]
        # print(f"{self._cp:0>3d}: {instr} {param}")

        if instr == "nop":
            self._cp += 1
        elif instr == "acc":
            self._accum += param
            self._cp += 1
        elif instr == "jmp":
            self._cp += param

    @classmethod
    def parse_instr(cls, line):
        # print(line)
        instr, param = line.split()
        return [instr, int(param)]


with open(path.join(curdir, "day_8.input")) as f:
    code = parse(f, Process.parse_instr)


def flip(instr):
    if instr == "nop":
        return "jmp"
    elif instr == "jmp":
        return "nop"
    else:
        raise ValueError(instr)


def part_1(code):
    """
    Runs the code, and returns the raised exception's accum value if an infinite loop is encountered.
    Otherwise it'll return None (this would be unexpected)
    """
    process = Process(code)
    try:
        # will either run the whole program, or raise InfiniteLoopError
        process.execute()
    except InfiniteLoopError as e:
        return e.accum


def part_2(code):
    """
    Goes through the whole code, each time it encounters a `jmp` or a `nop`, it flips it
    over and runs the new code. If the process finishes correctly, it returns the returned number,
    if it raises InfiniteLoopError, it flips back, and goes on trying
    """
    for idx, instr in enumerate(code):
        if instr[0] in ("nop", "jmp"):
            old = instr[0]
            code[idx][0] = flip(old)
            process = Process(code)
            try:
                return process.execute()
            except InfiniteLoopError:
                code[idx][0] = old


print(f"Part 1: {part_1(code)}")
print(f"Part 2: {part_2(code)}")
